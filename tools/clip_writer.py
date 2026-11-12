#!/usr/bin/env python3
"""Have Gemini (re)write specific clips of an episode, validate them, and merge them in.

Gemini gets: the format guide and references (build_brief), the current episode script,
the clips already approved before the target (as continuity), the existing draft of the
target clips (if any), and optionally the full user<->Claude chat log.

Usage:
    python3 tools/clip_writer.py --episode 1 --clips 02A 02B
    python3 tools/clip_writer.py --episode 1 --clips 02A 02B --with-chat --dry-run

Output blocks expected from Gemini:  === CLIP: 02A ===  followed by the full clip section.
Each round's raw output and the review go to storyboard/epNN/gemini/.
"""
import argparse
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from episode_writer import ROOT, build_brief, call_gemini, read  # noqa: E402
from validate_episode import Report, validate_clips  # noqa: E402

CHAT_LOG = "handoff/chat_log.md"


def clip_sections(clips_md):
    """Return {clip_id: section_text} for '## 클립 ID — ...' sections."""
    out = {}
    parts = re.split(r"(?=^## 클립 \S+ — )", clips_md, flags=re.M)
    for p in parts:
        m = re.match(r"## 클립 (\S+) — ", p)
        if m:
            body = re.split(r"\n---\s*\n(?=## |\Z)", p)[0].rstrip() + "\n"
            out[m.group(1)] = body
    return out


def parse_clips(text):
    parts = re.split(r"^=== CLIP: (\S+) ===\s*$", text, flags=re.M)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        body = parts[i + 1].strip("\n")
        body = re.sub(r"^```(?:markdown|md)\n", "", body)
        body = re.sub(r"\n```\s*$", "", body) if body.count("```") % 2 else body
        out[parts[i].strip()] = body.strip() + "\n"
    return out


def merge(clips_md, new):
    for cid, section in new.items():
        old = clip_sections(clips_md).get(cid)
        if old:
            clips_md = clips_md.replace(old.rstrip("\n"), section.rstrip("\n"), 1)
        else:
            clips_md = clips_md.rstrip() + "\n\n" + section
    return clips_md


def norm(s):
    return re.sub(r"[\s.,!?…~'\"“”‘’·]", "", s)


def check_dialogue(script, new, rep):
    """Hallucination check: every spoken line {..} in a clip must come from the script."""
    script_n = norm(re.sub(r"\([^)]*\)", "", script))
    for cid, sec in new.items():
        for line in re.findall(r"\{([^}]*)\}", sec):
            for sent in re.split(r"(?<=[.?!])\s+", line):
                if norm(sent) and norm(sent) not in script_n:
                    rep.err(f"클립 {cid}", f"대본에 없는 대사(환각 의심): {{{sent}}}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--clips", nargs="+", required=True)
    ap.add_argument("--model", default="agy:gemini-4-argon-high")
    ap.add_argument("--allow-fallback", action="store_true", help="use Flash models if the main model is unavailable")
    ap.add_argument("--max-rounds", type=int, default=3)
    ap.add_argument("--with-chat", action="store_true", help="append the user<->Claude chat log")
    ap.add_argument("--note", default="", help="extra instruction for this run")
    ap.add_argument("--dry-run", action="store_true", help="write the prompt only, do not call Gemini")
    ap.add_argument("--fresh", action="store_true", help="do not show the existing draft of the target clips")
    ap.add_argument("--no-merge", action="store_true", help="review only; leave clips.md unchanged")
    a = ap.parse_args()

    ep = a.episode
    script_rel = f"scripts/ep{ep:02d}.md"
    clips_rel = f"storyboard/ep{ep:02d}/clips.md"
    gdir = os.path.join(ROOT, f"storyboard/ep{ep:02d}/gemini")
    os.makedirs(gdir, exist_ok=True)
    clips_md = read(clips_rel)
    sections = clip_sections(clips_md)
    order = list(sections)
    first = min(order.index(c) for c in a.clips if c in order) if any(c in order for c in a.clips) else len(order)
    approved = [sections[c] for c in order[:first]][-2:]  # the two clips right before the target
    drafts = [] if a.fresh else [sections[c] for c in a.clips if c in sections]

    system = build_brief(ep, label=f"이번 화({ep}화) 대본 — 클립의 원본")
    if a.with_chat:
        system += "\n\n---\n\n## 부록 F. 지금까지 사용자와 Claude가 나눈 대화\n\n제작 결정과 사용자 취향의 근거다. 뒤에 나온 결정이 앞의 것을 덮는다.\n\n" + read(CHAT_LOG)
    system += ("\n\n---\n\n## 클립 단위 작업 출력 형식\n\n이번 작업은 대본 전체가 아니라 지정된 클립만 쓴다. "
               "클립마다 `=== CLIP: ID ===` 한 줄로 시작하고, 그 아래에 `## 클립 ID — 장소 (N초)`부터 7장 형식 그대로의 클립 섹션 전문을 낸다. "
               "설명이나 인사는 쓰지 않는다.\n")
    user = f"{ep}화의 클립 {', '.join(a.clips)}를 써라. 대본(부록 C)의 해당 장면을 그대로 옮긴다. 대본에 없는 대사를 만들지 않는다.\n"
    if approved:
        user += "\n## 바로 앞의 확정 클립 (연속성 참고)\n\n" + "\n".join(approved)
    if drafts:
        user += "\n## 기존 초안 (규칙 위반이 있으면 고쳐서 다시 쓴다)\n\n" + "\n".join(drafts)
    if a.note:
        user += "\n## 추가 지시\n\n" + a.note + "\n"
    with open(os.path.join(gdir, "last_prompt.md"), "w", encoding="utf-8") as f:
        f.write(system + "\n\n=====USER=====\n\n" + user)
    print(f"prompt: system {len(system)} chars, user {len(user)} chars")
    if a.dry_run:
        return

    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log = [f"# 클립 {', '.join(a.clips)} 자동 작성 기록 ({stamp})", f"- 모델: `{a.model}`", f"- 대화 기록 포함: {a.with_chat}", ""]
    rep, new = None, {}
    for rnd in range(1, a.max_rounds + 1):
        print(f"[round {rnd}] {a.model} ...", flush=True)
        text, finish, usage = call_gemini(a.model, messages, 30000, a.allow_fallback)
        with open(os.path.join(gdir, f"{stamp}_round{rnd}.md"), "w", encoding="utf-8") as f:
            f.write(text)
        new = parse_clips(text)
        missing = [c for c in a.clips if c not in new]
        rep = Report()
        if missing:
            rep.err("출력", f"클립 블록 없음: {missing} (finish_reason={finish})")
        else:
            validate_clips(ROOT, "\n\n".join(new[c] for c in a.clips), rep)
            check_dialogue(read(script_rel), new, rep)
            rep.warnings = [w for w in rep.warnings if not w.startswith("[클립] 클립 합계")]
        log.append(f"## 라운드 {rnd}\n\n- 토큰: {usage}\n\n{rep.text()}\n")
        print(rep.summary(), flush=True)
        if rep.ok:
            break
        messages += [{"role": "assistant", "content": text},
                     {"role": "user", "content": "검수에서 아래 문제가 나왔다. 고쳐서 지정 클립 전부를 같은 형식으로 다시 내라.\n\n" + rep.errors_text()}]
    with open(os.path.join(gdir, f"{stamp}_review.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(log))
    if rep and rep.ok and a.no_merge:
        print("passed review; not merged (--no-merge)")
    elif rep and rep.ok:
        with open(os.path.join(ROOT, clips_rel), "w", encoding="utf-8") as f:
            f.write(merge(clips_md, {c: new[c] for c in a.clips}))
        print(f"merged {a.clips} into {clips_rel}")
    else:
        print("not merged: review failed; see review file")
        sys.exit(1)


if __name__ == "__main__":
    main()
