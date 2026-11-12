#!/usr/bin/env python3
"""Generate one image with ChatGPT's image tool through the Codex CLI (ChatGPT subscription login).

Usage: python3 tools/gpt_image.py <out.png> "<prompt>"
No Higgsfield credits are used. Login once with: codex login --device-auth
"""
import os
import shutil
import subprocess
import sys
import tempfile

out, prompt = os.path.abspath(sys.argv[1]), sys.argv[2]
ws = tempfile.mkdtemp(prefix="gptimg_", dir=os.environ.get("GPT_IMAGE_TMP"))
instr = ("Use your image generation tool to create ONE image and save it in the current folder as result.png. "
         "Do not write code to draw it. Image: " + prompt)
subprocess.run(["codex", "exec", "--skip-git-repo-check", "-s", "workspace-write", instr], cwd=ws, check=True,
               timeout=900, stdout=subprocess.DEVNULL)
src = os.path.join(ws, "result.png")
if not os.path.exists(src):
    sys.exit("no image produced")
shutil.move(src, out)
print(out)
