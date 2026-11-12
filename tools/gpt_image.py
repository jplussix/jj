#!/usr/bin/env python3
"""Generate one image with ChatGPT's image tool through the Codex CLI (ChatGPT subscription login).

Usage: python3 tools/gpt_image.py <out.png> "<prompt>" [reference.png ...]
No Higgsfield credits are used. Login once with: codex login --device-auth
"""
import os
import shutil
import subprocess
import sys
import tempfile

out, prompt = os.path.abspath(sys.argv[1]), sys.argv[2]
refs = [os.path.abspath(r) for r in sys.argv[3:]]
ws = tempfile.mkdtemp(prefix="gptimg_", dir=os.environ.get("GPT_IMAGE_TMP"))
instr = ("Use your image generation tool to create ONE image and save it in the current folder as result.png. "
         "Do not write code to draw it. Image: " + prompt)
cmd = ["codex", "exec", "--skip-git-repo-check", "-s", "workspace-write"]
for r in refs:
    cmd += ["-i", r]
if refs:
    instr += " Use the attached image(s) as the identity reference: keep the same face exactly."
subprocess.run(cmd + ["--", instr] if refs else cmd + [instr], cwd=ws, check=True,
               timeout=900, stdout=subprocess.DEVNULL)
src = os.path.join(ws, "result.png")
if not os.path.exists(src):
    sys.exit("no image produced")
shutil.move(src, out)
print(out)
