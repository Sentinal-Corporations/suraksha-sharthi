import os, wave, struct, re, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio
import imageio_ffmpeg

BASE = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi"
S = f"{BASE}/mvp/shots"; B = f"{BASE}/branding"; M = f"{BASE}/mvp"; A2 = f"{M}/audio2"
W, H, FPS = 1280, 720, 20
# shot file, title, 3 caption lines
SCENES = [
 ("07_desktop.png", "HOOK — har ghar ki problem", ["Haathon se likhi parchi", "Kaun padhega dose?", "Team CHANAKYA • BIC 2.0"], "cover"),
 ("01_landing.png", "PROBLEM — 50% galat dose", ["60% handwritten parchis", "1L deaths/yr • AMR risk", "10L ASHAs, zero tool"], "pan"),
 ("02_fill_ocr.png", "DEMO 1 — Scan to Read", ["Real messy parchi", "62% → 87% smart read", "Human tap-confirm"], "pan"),
 ("03_result.png", "DEMO 2 — Rog Samjhao", ["Grade-5 words, hi/bn/mr", "Voice + pictogram timetable", "Anpadh-friendly"], "pan"),
 ("04_alert.png", "DEMO 3 — Duplicate RED alert", ["Dolo + Crocin = overdose", "Alert fires live", "High-risk = refer only"], "pan"),
 ("05_suvidha.png", "SUVIDHA — sarkari sahayata", ["Jan Aushadhi −50-70%", "Ayushman Rs 5L cashless", "108 • 112 • 104 tap-call"], "pan"),
 ("06_drawer.png", "TRUST — menu + privacy", ["Privacy • Agreement • Help", "One-tap delete", "Offline-first for gaon"], "pan"),
 ("02_fill_ocr.png", "DEMO 4 — simple form", ["Naam optional, phone reminders", "Bhasha: hi/bn/mr + lakshan", "Chips fix → Main result"], "rev"),
 ("05_suvidha.png", "SUVIDHA 2 — helplines", ["108 • 112 • 104 • 14555", "Ek tap Call button", "Ayushman card steps"], "rev"),
 ("logo.png", "TECH + TEAM — Needle-2", ["14MB on-device AI", "Verified DB, zero guess", "Aaj parchi, kal Sehat File"], "zoom"),
]
def font(s):
    try: return ImageFont.truetype("arial.ttf", s)
    except: return ImageFont.load_default()

def dur_mp3(i):
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    out = subprocess.run([ff, "-i", f"{A2}/h{i}.mp3"], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out.stderr)
    h, mnt, s = int(m.group(1)), int(m.group(2)), float(m.group(3))
    return h * 3600 + mnt * 60 + s

def load_shot(f):
    for d in (S, B):
        p = f"{d}/{f}"
        if os.path.exists(p): return Image.open(p).convert("RGB")
    raise FileNotFoundError(f)

def frame_pan(shot, title, lines, idx, total, f, nfr, tfrac, rev=False):
    img = Image.new("RGB", (W, H), "#232326"); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 78], fill="#3A3A3C")
    d.text((36, 16), "SURAKSHA PARCHI • REAL APP DEMO", font=font(28), fill="#F3DFC2")
    d.text((W - 36, 16), f"{idx + 1}/{total}", font=font(26), anchor="ra", fill="#B9B2A0")
    d.rectangle([0, 78, W, 84], fill="#C96A1B")
    # right: phone footage, slow vertical pan
    pw, ph = 430, 600
    sc = pw / shot.width
    sh = Image.fromarray(np.array(shot.resize((pw, int(shot.height * sc)))))
    maxy = max(0, sh.height - ph)
    prog = f / max(1, nfr - 1)
    y0 = int(maxy * (1 - prog)) if rev else int(maxy * prog)
    crop = sh.crop((0, y0, pw, y0 + ph))
    img.paste(crop, (W - pw - 50, 100))
    d.rounded_rectangle([W - pw - 50, 100, W - 50, 700], radius=26, outline="#C96A1B", width=4)
    # left: captions
    d.text((50, 130), title, font=font(42), fill="#F5EFE3")
    y = 220
    for ln in lines:
        d.text((50, y), "•  " + ln, font=font(30), fill="#D8D2C2"); y += 60
    d.text((50, 560), "♪ Hinglish narration on", font=font(24), fill="#8f8a7d")
    pw2 = int(W * tfrac); d.rectangle([0, H - 12, pw2, H], fill="#C96A1B")
    return img

def frame_cover(f, title, lines, idx, total, z, tfrac):
    base = load_shot(f)
    zw, zh = int(W * z), int(H * z)
    im = base.resize((W, H)).resize((zw, zh)).resize((W, H))
    img = im.convert("RGB"); d = ImageDraw.Draw(img, "RGBA")
    d.rectangle([0, H - 260, W, H], fill=(20, 20, 22, 210))
    d.text((50, H - 230), title, font=font(44), fill="#F5EFE3")
    y = H - 160
    for ln in lines:
        d.text((50, y), "•  " + ln, font=font(28), fill="#D8D2C2"); y += 48
    d.text((W - 36, 24), f"{idx + 1}/{total}", font=font(26), anchor="ra", fill="#F5EFE3")
    pw2 = int(W * tfrac); d.rectangle([0, H - 12, pw2, H], fill="#C96A1B")
    return img

durs = [dur_mp3(i) + 1.2 for i in range(10)]
total = sum(durs)
tmp = f"{M}/demo2_silent.mp4"
wr = imageio.get_writer(tmp, fps=FPS, codec="libx264", quality=7)
done = 0.0
for i, (f, title, lines, kind) in enumerate(SCENES):
    nfr = int(durs[i] * FPS)
    if kind in ("pan", "rev"):
        shot = load_shot(f)
        for fr in range(nfr):
            wr.append_data(np.array(frame_pan(shot, title, lines, i, 10, fr, nfr, (done + fr / FPS) / total, rev=(kind == "rev"))))
    else:
        for fr in range(nfr):
            z = 1.0 + 0.08 * (fr / max(1, nfr - 1))
            wr.append_data(np.array(frame_cover(f, title, lines, i, 10, z, (done + fr / FPS) / total)))
    done += durs[i]
    print(f"scene{i}: {durs[i]:.1f}s")
wr.close()

# concat mp3 + 1.0s silence gaps (matches +1.2 video pad via -shortest)
ff = imageio_ffmpeg.get_ffmpeg_exe()
sil = f"{M}/sil.mp3"
subprocess.run([ff, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "1.0", sil], check=True, capture_output=True)
lst = f"{M}/concat.txt"
with open(lst, "w") as fh:
    for i in range(10):
        fh.write(f"file '{A2}/h{i}.mp3'\nfile '{os.path.basename(sil)}'\n")
aud = f"{M}/demo2_audio.mp3"
subprocess.run([ff, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", aud], check=True, capture_output=True)
out = f"{M}/demo_video_app.mp4"
subprocess.run([ff, "-y", "-i", tmp, "-i", aud, "-c:v", "copy", "-c:a", "aac", "-shortest", out], check=True, capture_output=True)
print("saved:", out, os.path.getsize(out) // 1024, "KB")
