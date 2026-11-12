#!/usr/bin/env python3
"""Episode 1 rough cut: join finished clips, burn subtitles, add BGM (ducked) and gag SFX.

Order: clip01 (with inner monologue) -> title -> "열여덟 시간 전" card -> clip02A -> clip05A.
Subtitle times come from the ElevenLabs transcripts of each clip (word timestamps).
Output: renders/ep01/ep01_roughcut_v1.mp4
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = os.environ.get("CUT_TMP", "/tmp/roughcut")
os.makedirs(TMP, exist_ok=True)
R = lambda p: os.path.join(ROOT, p)  # noqa: E731

SEGMENTS = [  # (file, duration)
    ("renders/ep01/clip01_take1_vo.mp4", 25.056),
    ("assets/title/title_sequence_480p.mp4", 6.042),
    ("CARD", 2.0),
    ("renders/ep01/clip02a_take2.mp4", 25.056),
    ("renders/ep01/clip05a_take1.mp4", 30.080),
]
starts, t = [], 0.0
for _, d in SEGMENTS:
    starts.append(t)
    t += d
TOTAL = t
S01, STITLE, SCARD, S02A, S05A = starts

# (start, end, style, text) — times relative to each clip, shifted below
SUBS = [
    (S01 + 0.8, S01 + 5.0, "Place", "세종 16년(1434), 함길도 북방 삭풍진"),
    (S01 + 1.5, S01 + 4.4, "Inner", "(속마음) 여기 어디야. 웬 불이 저렇게 많아."),
    (S01 + 9.2, S01 + 11.9, "Line", "적이 육천입니다. 아군은 팔백입니다."),
    (S01 + 11.95, S01 + 14.95, "Inner", "(속마음) 육천? 팔백? …재고 얘긴가."),
    (S01 + 15.05, S01 + 17.7, "Line", "장군, 명을 내리소서."),
    (S01 + 18.0, S01 + 20.7, "Inner", "(속마음) 장군? 나한테 하는 소리야?"),
    (SCARD + 0.2, SCARD + 1.9, "Card", "열여덟 시간 전"),
    (S02A + 0.42, S02A + 3.6, "Line", "부장님… 아니, 선배님. 저도 마음이 안 좋습니다."),
    (S02A + 4.68, S02A + 6.95, "Line", "최 대리… 아, 상무님."),
    (S02A + 7.6, S02A + 9.8, "Line", "우리 애 취직할 때까지만요. 일 년만."),
    (S02A + 10.7, S02A + 12.3, "Line", "본사 결재가 어제 끝났어요."),
    (S02A + 17.0, S02A + 18.7, "Line", "제가 여기서 이십칠 년입니다."),
    (S02A + 19.2, S02A + 21.2, "Line", "그래서 위로금도 넉넉히 넣었습니다."),
    (S05A + 3.6, S05A + 5.0, "Line", "아이고…"),
    (S05A + 9.0, S05A + 10.4, "Line", "안 아프네."),
    (S05A + 26.6, S05A + 28.3, "Line", "누구세요."),
]
SFX = [  # (time, file, volume)
    (S01 + 20.9, "audio/sfx/gag_crickets.mp3", 0.9),
    (S05A + 27.4, "audio/sfx/gag_boing.mp3", 0.8),
]
BGM = [  # (file, start, end, source offset, volume)
    ("audio/bgm/02_joseon_tension.mp3", S01, S01 + 25.0, 0.0, 0.30),
    ("audio/bgm/05_bittersweet.mp3", SCARD, S02A + 25.0, 0.0, 0.26),
    ("audio/bgm/03_mansu_fumble.mp3", S05A + 5.0, S05A + 30.0, 0.0, 0.24),
]


def ts(x):
    h, m = int(x // 3600), int(x % 3600 // 60)
    return f"{h}:{m:02d}:{x % 60:05.2f}"


def write_ass(path):
    head = """[Script Info]
ScriptType: v4.00+
PlayResX: 854
PlayResY: 480

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Line,NanumGothic,26,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,2.4,0,2,30,30,26,1
Style: Inner,NanumGothic,25,&H0060E8FF,&H0060E8FF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,2.4,0,2,30,30,26,1
Style: Place,NanumMyeongjo,22,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,1.8,0,7,34,30,30,1
Style: Card,NanumMyeongjo,38,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,2,0,1,0,0,5,30,30,30,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(head)
        for a, b, st, txt in SUBS:
            fade = r"{\fad(300,300)}" if st in ("Place", "Card") else r"{\fad(80,80)}"
            f.write(f"Dialogue: 0,{ts(a)},{ts(b)},{st},,0,0,0,,{fade}{txt}\n")


def run(cmd):
    subprocess.run(cmd, check=True)


def main():
    norm = []
    for i, (src, dur) in enumerate(SEGMENTS):
        out = os.path.join(TMP, f"seg{i}.mp4")
        if src == "CARD":
            run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=black:s=854x480:r=24:d={dur}",
                 "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo", "-t", str(dur),
                 "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", out])
        else:
            run(["ffmpeg", "-v", "error", "-y", "-i", R(src), "-vf", "scale=854:480,fps=24,setsar=1",
                 "-af", "aresample=48000,aformat=channel_layouts=stereo", "-t", str(dur),
                 "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-c:a", "aac", "-b:a", "192k", out])
        norm.append(out)
    lst = os.path.join(TMP, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in norm)
    base = os.path.join(TMP, "base.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])

    ass = os.path.join(TMP, "subs.ass")
    write_ass(ass)

    inputs = ["-i", base]
    fc = ["[0:a]asplit=2[dia][key]"]
    mix = ["[dia]"]
    n = 1
    bgm_labels = []
    for k, (f, a, b, off, vol) in enumerate(BGM):
        inputs += ["-ss", str(off), "-i", R(f)]
        d = b - a
        fc.append(f"[{n}:a]atrim=0:{d:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=1.0,afade=t=out:st={d-1.5:.3f}:d=1.5,"
                  f"volume={vol},adelay={int(a*1000)}|{int(a*1000)},apad=whole_dur={TOTAL:.3f}[b{k}]")
        bgm_labels.append(f"[b{k}]")
        n += 1
    fc.append("".join(bgm_labels) + f"amix=inputs={len(bgm_labels)}:normalize=0[bgm]")
    fc.append("[bgm][key]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=450[bgmd]")
    mix.append("[bgmd]")
    for k, (tm, f, vol) in enumerate(SFX):
        inputs += ["-i", R(f)]
        fc.append(f"[{n}:a]volume={vol},adelay={int(tm*1000)}|{int(tm*1000)}[s{k}]")
        mix.append(f"[s{k}]")
        n += 1
    fc.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,volume=2.4dB,alimiter=limit=0.84:level=false[aout]")
    fc.append(f"[0:v]ass={ass}[vout]")
    out = R("renders/ep01/ep01_roughcut_v1.mp4")
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out])
    print(f"{out} ({TOTAL:.1f}s)")


if __name__ == "__main__":
    main()
