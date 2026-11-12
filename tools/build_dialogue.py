#!/usr/bin/env python3
"""Lay pre-made dialogue lines onto one track at the times the clip's timeline expects.

Usage: python3 tools/build_dialogue.py out.mp3 DURATION file@START [file@START ...]
The result is fed to Seedance as an audio reference so every line keeps its fixed voice.
"""
import subprocess
import sys

out, dur = sys.argv[1], float(sys.argv[2])
items = [(a.rsplit("@", 1)[0], float(a.rsplit("@", 1)[1])) for a in sys.argv[3:]]
inputs, fc = [], []
for k, (f, t) in enumerate(items):
    inputs += ["-i", f]
    fc.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=mono,adelay={int(t*1000)}|{int(t*1000)}[a{k}]")
fc.append("".join(f"[a{k}]" for k in range(len(items))) + f"amix=inputs={len(items)}:normalize=0,apad=whole_dur={dur},atrim=0:{dur}[o]")
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[o]",
                "-ac", "1", "-b:a", "192k", out], check=True)
print(out)
