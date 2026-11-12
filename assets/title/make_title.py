import os, subprocess, sys, math, random
from PIL import Image, ImageFilter, ImageChops, ImageEnhance

ROOT = "/home/user/jj"
SCR = os.environ.get("SCRATCH", "/tmp/title_build")
BG = f"{ROOT}/assets/title/title_bg.mp4"
LOGO = f"{ROOT}/assets/title/title_a.png"
SFX = f"{ROOT}/audio/sfx/title_sting_b.mp3"
OUT = f"{ROOT}/assets/title/title_sequence_720p.mp4"
OUT480 = f"{ROOT}/assets/title/title_sequence_480p.mp4"
FRAMES = f"{SCR}/title_frames"
W, H, FPS = 1280, 720, 24
HIT = 2.2          # title slam time (s)
SFX_START = HIT - 0.5  # drum hit sits at 0.5s inside the sfx file
FADE_START = 5.3

os.makedirs(FRAMES, exist_ok=True)
for f in os.listdir(FRAMES):
    os.remove(os.path.join(FRAMES, f))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", BG, "-vf", f"scale={W}:{H},fps={FPS}",
                f"{FRAMES}/bg_%04d.png"], check=True)
bgs = sorted(f for f in os.listdir(FRAMES) if f.startswith("bg_"))

# Title layer: scale logo to 80% width, add warm gold glow behind the ink so it reads on dark red.
logo = Image.open(LOGO).convert("RGBA")
bbox = logo.getbbox()
logo = logo.crop(bbox)
tw = int(W * 0.72)
logo = logo.resize((tw, int(logo.height * tw / logo.width)), Image.LANCZOS)
alpha = logo.split()[-1]
glow = Image.new("RGBA", logo.size, (255, 190, 90, 0))
glow.putalpha(alpha.filter(ImageFilter.GaussianBlur(14)).point(lambda a: int(a * 0.85)))
pad = 60
title = Image.new("RGBA", (logo.width + pad * 2, logo.height + pad * 2), (0, 0, 0, 0))
title.alpha_composite(glow, (pad, pad))
title.alpha_composite(glow, (pad, pad))
title.alpha_composite(logo, (pad, pad))
cx, cy = W // 2, int(H * 0.40)  # above the gate silhouette

random.seed(7)
n = len(bgs)
for i, name in enumerate(bgs):
    t = i / FPS
    frame = Image.open(os.path.join(FRAMES, name)).convert("RGBA")
    if t >= HIT:
        k = min(1.0, (t - HIT) / 0.25)
        ease = 1 - (1 - k) ** 3
        scale = 1.35 - 0.35 * ease
        if t > HIT + 0.25:  # slow settle drift after the slam
            scale = 1.0 + 0.03 * (t - HIT - 0.25) / (FADE_START - HIT)
        a = ease
        sw, sh = int(title.width * scale), int(title.height * scale)
        layer = title.resize((sw, sh), Image.LANCZOS)
        if a < 1:
            layer.putalpha(layer.split()[-1].point(lambda v: int(v * a)))
        shake = max(0.0, 1 - (t - HIT) / 0.35)
        dx = int(random.uniform(-8, 8) * shake)
        dy = int(random.uniform(-6, 6) * shake)
        frame.alpha_composite(layer, (cx - sw // 2 + dx, cy - sh // 2 + dy))
        flash = max(0.0, 1 - (t - HIT) / 0.18) * 0.55
        if flash > 0:
            white = Image.new("RGBA", frame.size, (255, 236, 210, int(255 * flash)))
            frame.alpha_composite(white)
    if t >= FADE_START:
        f = min(1.0, (t - FADE_START) / (6.0 - FADE_START))
        frame = Image.blend(frame, Image.new("RGBA", frame.size, (0, 0, 0, 255)), f)
    frame.convert("RGB").save(os.path.join(FRAMES, f"out_{i:04d}.png"))

dur = n / FPS
ms = int(SFX_START * 1000)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{FRAMES}/out_%04d.png",
                "-i", SFX, "-filter_complex",
                f"[1:a]adelay={ms}|{ms},apad,atrim=0:{dur:.3f},afade=t=out:st={FADE_START}:d={dur-FADE_START:.3f}[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", OUT], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", OUT, "-vf", "scale=854:480", "-c:v", "libx264",
                "-pix_fmt", "yuv420p", "-crf", "18", "-c:a", "copy", OUT480], check=True)
print("frames", n, "duration", round(dur, 2))
