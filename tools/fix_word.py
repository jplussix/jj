#!/usr/bin/env python3
"""Replace one mispronounced word in a clip's audio with a replacement recording.

Usage: python3 tools/fix_word.py in.mp4 out.mp4 word.wav START:END [START:END ...]
Each window's original audio is ducked to 8% and the replacement word, time-stretched to the
window length and level-matched to the original, is laid on top. Video is copied untouched.
"""
import subprocess
import sys


def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout)


def mean_db(f, ss=None, to=None):
    cmd = ["ffmpeg", "-hide_banner"] + (["-ss", str(ss), "-to", str(to)] if ss is not None else []) + ["-i", f, "-af", "volumedetect", "-f", "null", "-"]
    out = subprocess.run(cmd, capture_output=True, text=True).stderr
    return float(out.split("mean_volume:")[1].split("dB")[0])


src, out, word = sys.argv[1:4]
wins = [tuple(map(float, w.split(":"))) for w in sys.argv[4:]]
wlen = dur(word)
duck = "+".join(f"between(t,{a:.3f},{b:.3f})" for a, b in wins)
fc = [f"[0:a]aresample=48000,volume='if({duck},0.08,1)':eval=frame[base]"]
labels = []
for k, (a, b) in enumerate(wins):
    gain = mean_db(src, a, b) - mean_db(word)
    tempo = max(0.5, min(2.0, wlen / (b - a)))
    fc.append(f"[1:a]aresample=48000,atempo={tempo:.4f},volume={gain:.2f}dB,afade=t=in:d=0.02,afade=t=out:st={(b-a)-0.04:.3f}:d=0.04,"
              f"adelay={int(a*1000)}|{int(a*1000)}[w{k}]")
    labels.append(f"[w{k}]")
fc.append("[base]" + "".join(labels) + f"amix=inputs={1+len(labels)}:normalize=0:duration=first[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-i", word, "-filter_complex", ";".join(fc),
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", out], check=True)
print(out)
