#!/usr/bin/env python3
"""Export the user's messages and the assistant's prose replies from a Claude Code session log.

Tool calls, tool results, thinking and system notes are dropped, so the output is the
conversation as the user saw it: decisions, feedback and explanations.

Usage: python3 tools/export_chat.py <session.jsonl> handoff/chat_log.md
"""
import json
import re
import sys


def text_of(content):
    if isinstance(content, str):
        return content
    out = []
    for part in content or []:
        if isinstance(part, dict) and part.get("type") == "text":
            out.append(part.get("text", ""))
    return "\n".join(out)


def clean_user(t):
    t = re.sub(r"<system-reminder>.*?</system-reminder>", "", t, flags=re.S)
    t = re.sub(r"<local-command-[a-z]+>.*?</local-command-[a-z]+>", "", t, flags=re.S)
    t = re.sub(r"<command-[a-z]+>.*?</command-[a-z]+>", "", t, flags=re.S)
    t = re.sub(r"This is how Claude Code surfaces messages.*", "", t, flags=re.S)
    t = t.replace("The user sent a new message while you were working:", "")
    return t.strip()


def main(src, dst):
    turns = []
    with open(src, encoding="utf-8") as f:
        for line in f:
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = ev.get("message") or {}
            role = msg.get("role") or ev.get("type")
            if ev.get("isMeta") or ev.get("isSidechain"):
                continue
            if role == "user":
                content = msg.get("content")
                if isinstance(content, list) and any(isinstance(p, dict) and p.get("type") == "tool_result" for p in content):
                    # mid-turn user messages arrive inside tool results as text parts
                    t = "\n".join(p.get("text", "") for p in content if isinstance(p, dict) and p.get("type") == "text")
                else:
                    t = text_of(content)
                t = clean_user(t)
                if t and not t.startswith("Tool loaded") and not t.startswith("Stop hook feedback"):
                    turns.append(("사용자", t))
            elif role == "assistant":
                t = text_of(msg.get("content")).strip()
                if len(t) > 40:  # skip short progress notes between tool calls
                    turns.append(("Claude", t))
    with open(dst, "w", encoding="utf-8") as f:
        f.write("# 지금까지의 대화 기록 (사용자 ↔ Claude)\n\n")
        f.write("도구 실행 기록은 빠져 있다. 결정 사항은 뒤에 나온 것이 앞의 것을 덮는다.\n\n")
        for who, t in turns:
            f.write(f"## {who}\n\n{t}\n\n")
    print(f"{len(turns)} turns -> {dst}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
