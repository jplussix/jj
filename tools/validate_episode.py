#!/usr/bin/env python3
"""Check an episode script and its clip prompts against the production rules.

Errors block acceptance; warnings are reported but do not. Rules come from
tools/brief_header.md, docs/characters.md and storyboard/ep01/clips.md.

Usage: python3 tools/validate_episode.py scripts/ep02.md storyboard/ep02/clips.md
"""
import os
import re
import sys

SECTIONS = ["[Generation Goal]", "[Reference Material Roles]", "[Subjects and Relationships]",
            "[Event Script]", "[Visual and Camera Treatment]", "[Audio]", "[Maintain Consistency]"]

# English name used in prompts -> Korean name used in the voice table
NAMES = {
    "Park Mansu": "박만수", "Han Igyeom": "한이겸", "Cheon Bongsu": "천봉수", "Jo Yun": "조윤",
    "Jeongsuk": "정숙", "Haeun": "하은", "Executive Choi": "최 상무", "Office Manager": "관리소장",
    "Kim Jongseo": "김종서",
}
SPEECH_VERBS = r"(?:speaks|says|asks|shouts|whispers|mutters|answers|calls|groans|replies)"
BOILERPLATE_NEG = ["Do not use the grey background or the panel layout", "not a fixed keyframe",
                   "Do not use the image background"]


class Report:
    def __init__(self):
        self.errors, self.warnings, self.stats = [], [], {}

    def err(self, where, msg):
        self.errors.append(f"[{where}] {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"[{where}] {msg}")

    @property
    def ok(self):
        return not self.errors

    def summary(self):
        return f"errors={len(self.errors)} warnings={len(self.warnings)} stats={self.stats}"

    def errors_text(self):
        return "\n".join(f"- {e}" for e in self.errors)

    def text(self):
        out = [f"**결과: {'통과' if self.ok else '수정 필요'}** (오류 {len(self.errors)}, 경고 {len(self.warnings)})", ""]
        out.append("통계: " + ", ".join(f"{k} {v}" for k, v in self.stats.items()))
        if self.errors:
            out += ["", "오류:"] + [f"- {e}" for e in self.errors]
        if self.warnings:
            out += ["", "경고:"] + [f"- {w}" for w in self.warnings]
        return "\n".join(out)


def load_rules(root):
    chars = open(os.path.join(root, "docs/characters.md"), encoding="utf-8").read()
    clips1 = open(os.path.join(root, "storyboard/ep01/clips.md"), encoding="utf-8").read()
    voices = {}
    for m in re.finditer(r"^\| ([^|]+?) \| `([^`]+)` \|", clips1, re.M):
        name = re.sub(r"\s*\(.*?\)", "", m.group(1)).strip()
        voices[name] = m.group(2)
    m = re.search(r"## 김종서.*?\*\*목소리\*\*: `([^`]+)`", chars, re.S)
    if m:
        voices["김종서"] = m.group(1)
    heights = {}
    for m in re.finditer(r"`The top of ([A-Z][\w ]+?)'s head reaches (?:only )?([A-Z][\w ]+?)'s [a-z]+\.`", chars):
        heights[frozenset((m.group(1), m.group(2)))] = m.group(0).strip("`").rstrip(".")
    identities = re.findall(r"\*\*IDENTITY\*\*\n```\n(.+?)\n```", chars, re.S)
    id_sentences = [s.strip() for blk in identities for s in re.split(r"(?<=\.)\s+", blk) if len(s.strip()) > 30]
    return voices, heights, id_sentences


def validate_script(script, rep):
    where = "대본"
    if not re.search(r"^# 조선만수록 — \d+화", script, re.M):
        rep.err(where, "첫 줄 제목이 `# 조선만수록 — N화 「부제」` 형식이 아님")
    for h in ("## 등장인물", "## 장면 배분"):
        if h not in script:
            rep.err(where, f"`{h}` 섹션 없음")
    scenes = re.findall(r"^## 씬 \d+\. .+ — .+$", script, re.M)
    if not scenes:
        rep.err(where, "`## 씬 N. 장소 — 시간` 형식의 씬이 없음")
    rep.stats["씬"] = len(scenes)
    total = 0
    for m in re.finditer(r"^\*\*([^*\n]+)\*\*\n((?:.+\n?)+?)(?=\n|\Z)", script, re.M):
        name, line = m.group(1).strip(), m.group(2).strip()
        if name in ("자막",) or name.startswith("끝"):
            continue
        if "(속마음)" in name and name != "박만수(속마음)":
            rep.err(where, f"속마음 표기는 `**박만수(속마음)**`만 쓴다: `{name}`")
        total += len(line.replace(" ", ""))
        if len(line) > 70:
            rep.warn(where, f"대사가 김 ({len(line)}자): {name}: {line[:40]}…")
    rep.stats["대사(공백 제외)"] = total
    if total < 700 or total > 3000:
        rep.warn(where, f"대사량 {total}자: 1화는 약 970자(6분 40초). 7~9분 목표와 맞는지 확인")


def validate_clips(root, clips, rep):
    voices, heights, id_sentences = load_rules(root)
    blocks = re.split(r"^## 클립 (?=\S+ — )", clips, flags=re.M)[1:]
    if not blocks:
        rep.err("클립", "`## 클립 NN — 장소 (N초)` 형식의 클립이 없음")
        return
    total = 0
    for b in blocks:
        head = b.splitlines()[0]
        cid = head.split(" ")[0]
        where = f"클립 {cid}"
        m = re.search(r"\((\d+)초\)", head)
        if not m:
            rep.err(where, "제목에 `(N초)` 길이가 없음")
        else:
            sec = int(m.group(1))
            total += sec
            if sec > 30:
                rep.err(where, f"{sec}초: 30초 이하로 나눌 것")
            if sec < 4:
                rep.err(where, f"{sec}초: 4초 이상")
        if not re.search(r"^\*\*참조\*\*:", b, re.M):
            rep.err(where, "`**참조**:` 줄 없음")
        pm = re.search(r"```\n(\[Generation Goal\].*?)```", b, re.S)
        if not pm:
            rep.err(where, "7칸 프롬프트 코드블록 없음")
            continue
        p = pm.group(1)
        pos = [p.find(s) for s in SECTIONS]
        if -1 in pos:
            rep.err(where, "빠진 칸: " + ", ".join(s for s, i in zip(SECTIONS, pos) if i == -1))
        elif pos != sorted(pos):
            rep.err(where, "7칸 순서가 틀림")
        lines = re.findall(r"\{([^}]*)\}", p)
        if len(lines) > 8:
            rep.err(where, f"대사 {len(lines)}줄: 8줄 이하로")
        outside = re.sub(r"\{[^}]*\}|\"[^\"]*\"|: [가-힣][^.\n]*\.", "", p)  # dialogue, quoted on-screen text
        if re.search(r"[가-힣]", outside):
            hangul = re.findall(r"[가-힣][가-힣\s]*", outside)[:3]
            rep.err(where, f"프롬프트에 대사 밖 한글이 있음(영어로): {hangul}")
        if re.search(r"\b(480p|720p|1080p|16:9|9:16|\d+\s*(?:seconds?|secs?))\b", p):
            rep.err(where, "길이·화면비·해상도는 프롬프트에 쓰지 않는다")
        for s in id_sentences:
            if s in p:
                rep.err(where, f"인물 외형을 다시 묘사함(참조가 정함): \"{s[:50]}…\"")
                break
        audio = p[p.find("[Audio]"):p.find("[Maintain Consistency]")] if "[Audio]" in p else ""
        event = p[p.find("[Event Script]"):p.find("[Visual and Camera Treatment]")] if "[Event Script]" in p else ""
        speakers = {en for en in NAMES if re.search(rf"\b{re.escape(en)}\b[^.{{]*?\b{SPEECH_VERBS}\b", event + audio)}
        for en in speakers:
            ko = NAMES[en]
            v = voices.get(ko)
            if v and v not in audio:
                rep.err(where, f"{ko}({en})가 말하는데 [Audio]에 목소리 문구가 글자 그대로 없음: `{v}`")
        subj = p[p.find("[Subjects and Relationships]"):p.find("[Event Script]")]
        present = {en for en in NAMES if en in subj}
        needed = [(pair, s) for pair, s in heights.items() if pair <= present]
        missing = [s for _, s in needed if s not in p]
        if needed and len(missing) == len(needed):
            rep.err(where, f"키 문장이 하나도 없음. 예: `{missing[0]}.`")
        elif missing:
            rep.warn(where, f"키 문장 일부 빠짐: {missing}")
        neg = p
        for bp in BOILERPLATE_NEG:
            neg = neg.replace(bp, "")
        negs = re.findall(r"\b(?:no|not|never|without|don't)\b[^.]{0,30}", neg, re.I)
        if negs:
            rep.warn(where, f"부정문 확인(긍정 상태로 바꾸는 게 좋음): {negs[:2]}")
        if "Kim Jongseo" in p and re.search(r"Kim Jongseo[^.]*(trips|falls over|slips|stumbles|panics|squeals)", p):
            rep.err(where, "김종서를 개그 대상으로 씀")
    rep.stats["클립"] = len(blocks)
    rep.stats["클립 합계(초)"] = total
    if total < 360 or total > 660:
        rep.warn("클립", f"클립 합계 {total}초: 7~9분(420~540초) 목표 확인")


def validate(root, script, clips):
    rep = Report()
    validate_script(script, rep)
    validate_clips(root, clips, rep)
    return rep


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    s = open(os.path.join(root, sys.argv[1]), encoding="utf-8").read()
    c = open(os.path.join(root, sys.argv[2]), encoding="utf-8").read()
    r = validate(root, s, c)
    print(r.text())
    sys.exit(0 if r.ok else 1)
