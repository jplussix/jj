#!/usr/bin/env python3
"""Draft an episode's script and clip prompts with Gemini, validate them, and loop on fixes.

Usage:
    python3 tools/episode_writer.py --episode 2
    python3 tools/episode_writer.py --episode 2 --model gemini-pro-latest --max-rounds 3
    python3 tools/episode_writer.py --episode 2 --validate-only

Inputs (all from the repo):
    tools/brief_header.md          format rules, written once
    docs/characters.md, docs/setting.md, storyboard/ep01/clips.md (voice table, example clip)
    scripts/ep{N-1}.md             previous episode script
    storyboard/ep{N}/brief.md      what this episode must contain

Outputs:
    scripts/ep{N}.md, storyboard/ep{N}/clips.md   (written only when Gemini returns both files)
    storyboard/ep{N}/review.md                    validator report for every round
    storyboard/ep{N}/gemini_raw_round{K}.md       raw model output per round

The Gemini key is never read here: the session's network proxy injects it into requests
to generativelanguage.googleapis.com. A placeholder bearer token is sent and overwritten.
"""
import argparse
import datetime
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_episode import validate  # noqa: E402


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def demote(text, n=2):
    return re.sub(r"^(#+)", lambda m: "#" * (len(m.group(1)) + n), text, flags=re.M)


def build_brief(prev_ep, label=None):
    header = read("tools/brief_header.md")
    chars = read("docs/characters.md")
    setting = read("docs/setting.md")
    clips1 = read("storyboard/ep01/clips.md")
    voices = re.search(r"## 목소리 고정 문구\n(.*?)\n---", clips1, re.S).group(1).strip()
    example = re.search(r"(## 클립 05B.*?)\n## 클립 06A", clips1, re.S).group(1).strip()
    prev = read(f"scripts/ep{prev_ep:02d}.md")
    out = header
    out += "\n## 부록 A. 인물 설정\n\n"
    out += ("IDENTITY 블록은 이미지 생성 원본이다. 인물 이해에만 쓰고 클립 프롬프트에 외형을 다시 묘사하지 않는다. "
            "job 번호와 voice_id는 무시한다.\n\n")
    out += "### 시댄스 목소리 문구 (클립 [Audio]에 글자 그대로)\n\n" + voices + "\n"
    out += "| 김종서 | `a deep, calm, commanding voice of a man in his fifties, few words, never raised` |\n\n"
    out += demote(chars)
    out += "\n\n---\n\n## 부록 B. 키 문장\n\n부록 A 맨 위 '키 관계' 표와 김종서 항목의 키 문장을 쓴다.\n\n---\n\n"
    out += f"## 부록 C. {label or f'앞 화({prev_ep}화) 대본 — 형식과 톤의 기준, 이야기 연결'}\n\n" + demote(prev)
    out += "\n\n---\n\n## 부록 D. 클립 예시 (클립 형식의 기준)\n\n" + demote(example, 1)
    out += "\n\n---\n\n## 부록 E. 세계관\n\n" + demote(setting) + "\n"
    return out


FALLBACK = ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-3-flash-preview", "gemini-flash-latest"]


def _post(model, messages, max_tokens):
    body = json.dumps({"model": model, "messages": messages, "max_tokens": max_tokens,
                       "temperature": 0.8}).encode("utf-8")
    req = urllib.request.Request(API, data=body, method="POST", headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer proxy-injected",  # overwritten by the session proxy
    })
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read().decode("utf-8"))


def call_gemini(model, messages, max_tokens):
    """Call Gemini; retry 503/429-rate with backoff, then fall back to other models.

    A free-tier quota of 0 for a model (paid-only model) skips straight to the fallback.
    Returns (text, finish_reason, usage) and records the model actually used in usage.
    """
    import time
    import urllib.error
    for m in [model] + [f for f in FALLBACK if f != model]:
        for attempt in range(4):
            try:
                data = _post(m, messages, max_tokens)
                choice = data["choices"][0]
                usage = dict(data.get("usage", {}), model=m)
                return choice["message"]["content"], choice.get("finish_reason"), usage
            except urllib.error.HTTPError as e:
                msg = e.read().decode("utf-8", "replace")
                if e.code == 429 and "limit: 0" in msg:
                    print(f"  {m}: not available on this key's tier, trying next model", flush=True)
                    break
                if e.code in (429, 500, 503) and attempt < 3:
                    wait = 20 * (attempt + 1)
                    print(f"  {m}: HTTP {e.code}, retry in {wait}s", flush=True)
                    time.sleep(wait)
                    continue
                print(f"  {m}: HTTP {e.code}: {msg[:200]}", flush=True)
                break
    raise RuntimeError("all Gemini models failed")


def split_files(text):
    parts = re.split(r"^=== FILE: (.+?) ===\s*$", text, flags=re.M)
    files = {}
    for i in range(1, len(parts) - 1, 2):
        body = parts[i + 1].strip("\n")
        body = re.sub(r"^```(?:markdown|md)?\n", "", body)
        body = re.sub(r"\n```\s*$", "", body)
        files[parts[i].strip()] = body.strip() + "\n"
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--model", default="gemini-pro-latest")
    ap.add_argument("--max-rounds", type=int, default=3)
    ap.add_argument("--max-tokens", type=int, default=60000)
    ap.add_argument("--validate-only", action="store_true")
    a = ap.parse_args()

    ep = a.episode
    script_path = f"scripts/ep{ep:02d}.md"
    clips_path = f"storyboard/ep{ep:02d}/clips.md"
    outdir = os.path.join(ROOT, f"storyboard/ep{ep:02d}")
    os.makedirs(outdir, exist_ok=True)

    if a.validate_only:
        rep = validate(ROOT, read(script_path), read(clips_path))
        print(rep.text())
        sys.exit(0 if rep.ok else 1)

    request = read(f"storyboard/ep{ep:02d}/brief.md")
    messages = [
        {"role": "system", "content": build_brief(ep - 1)},
        {"role": "user", "content": f"{ep}화를 작성해라. 파일 경로는 `{script_path}`, `{clips_path}`.\n\n## 이번 화 요청\n\n{request}"},
    ]
    review_log = [f"# {ep}화 자동 작성 검수 기록\n", f"- 모델: `{a.model}`", f"- 시작: {datetime.datetime.now().isoformat(timespec='seconds')}\n"]
    rep = None
    for rnd in range(1, a.max_rounds + 1):
        print(f"[round {rnd}] calling {a.model} ...", flush=True)
        text, finish, usage = call_gemini(a.model, messages, a.max_tokens)
        with open(os.path.join(outdir, f"gemini_raw_round{rnd}.md"), "w", encoding="utf-8") as f:
            f.write(text)
        files = split_files(text)
        missing = [p for p in (script_path, clips_path) if p not in files]
        if missing:
            note = f"출력에 파일 블록이 없음: {', '.join(missing)} (finish_reason={finish})"
            review_log.append(f"## 라운드 {rnd}\n\n- {note}\n")
            print(note)
            messages += [{"role": "assistant", "content": text},
                         {"role": "user", "content": f"{note}. 형식대로 두 파일 전문을 `=== FILE: 경로 ===` 블록으로 다시 내라."}]
            continue
        rep = validate(ROOT, files[script_path], files[clips_path])
        review_log.append(f"## 라운드 {rnd}\n\n- 토큰: {usage}\n- finish_reason: {finish}\n\n{rep.text()}\n")
        print(rep.summary(), flush=True)
        for p in (script_path, clips_path):
            with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f:
                f.write(files[p])
        if rep.ok:
            break
        messages += [{"role": "assistant", "content": text},
                     {"role": "user", "content": "검수에서 아래 문제가 나왔다. 전부 고쳐서 두 파일 전문을 다시 내라. "
                      "문제없는 부분은 그대로 둔다.\n\n" + rep.errors_text()}]
    with open(os.path.join(outdir, "review.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(review_log))
    sys.exit(0 if rep and rep.ok else 1)


if __name__ == "__main__":
    main()
