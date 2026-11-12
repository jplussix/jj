#!/usr/bin/env python3
"""Free local transcription with OpenAI Whisper (Korean), word timestamps.

Usage: python3 tools/transcribe.py [--model medium] file.mp4 [file2 ...]
Writes <file>.whisper.txt next to each input and prints segments.
Model weights download from openaipublic.azureedge.net (allowed host) into ~/.cache/whisper.
"""
import argparse
import whisper

ap = argparse.ArgumentParser()
ap.add_argument("--model", default="medium")
ap.add_argument("files", nargs="+")
a = ap.parse_args()
m = whisper.load_model(a.model, device="cpu")
for f in a.files:
    r = m.transcribe(f, language="ko", word_timestamps=True, fp16=False, condition_on_previous_text=False)
    lines = [f"[{s['start']:6.2f}-{s['end']:6.2f}] {s['text'].strip()}" for s in r["segments"]]
    out = "\n".join(lines)
    with open(f + ".whisper.txt", "w", encoding="utf-8") as fh:
        fh.write(out + "\n")
    print(f"== {f}\n{out}\n", flush=True)
