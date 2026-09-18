import os, wave, struct
from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio
import imageio_ffmpeg

BASE = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi"
B = f"{BASE}/branding"; M = f"{BASE}/mvp"; A = f"{M}/audio"
W, H, FPS = 1280, 720, 20
CAPS = [
 ["Har ghar ki problem", "Photo lo, Bhasha me samjho", "Team CHANAKYA • BIC 2.0"],
 ["60% handwritten parchis", "50% galat dose • 1L deaths/yr", "10L ASHAs, zero tool"],
 ["English + internet must", "Cursive fail • chatbot guess", "Hamara gap-fill: 5-in-1"],
 ["Scan → Read → Samjhao → Yaad", "Hindi • Bengali • Marathi", "Timetable + RED alerts"],
 ["Real messy parchi", "62% → 87% smart read", "Human tap-confirm"],
 ["Disease Grade-5 words", "Voice hi/bn/mr + pictograms", "Illiterate-friendly"],
 ["Dolo + Crocin = overdose", "RED alert fires live", "High-risk = refer only"],
 ["Jan Aushadhi −50-70%", "Ayushman Rs 5L cashless", "108 • 112 • 104 tap-call"],
 ["Hybrid OCR + 14MB AI", "Verified DB, zero hallucination", "Offline-first, phone me hi"],
 ["Adherence +40% pilot", "500 families, 1 PHC", "Aaj parchi, kal Sehat File"],
]
def font(s):
    try: return ImageFont.truetype("arial.ttf", s)
    except: return ImageFont.load_default()

def scene_len(i):
    w = wave.open(f"{A}/scene{i}.wav"); n = w.getnframes(); fr = w.getframerate()
    w.close(); return n / fr

def frame(imgf, title, lines, idx, total, tfrac):
    img = Image.new("RGB", (W, H), "#232326"); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 86], fill="#3A3A3C")
    d.text((40, 18), "SURAKSHA PARCHI • TEAM CHANAKYA", font=font(30), fill="#F3DFC2")
    d.text((W - 40, 18), f"{idx + 1}/{total}", font=font(28), anchor="ra", fill="#B9B2A0")
    d.rectangle([0, 86, W, 92], fill="#C96A1B")
    try:
        im = Image.open(f"{B}/{imgf}").convert("RGB"); im.thumbnail((520, 480))
        img.paste(im, (60, 140))
    except Exception as e: print("img", e)
    d.text((640, 150), title, font=font(44), fill="#F5EFE3")
    y = 230
    for ln in lines:
        d.text((640, y), "•  " + ln, font=font(30), fill="#D8D2C2"); y += 56
    d.text((640, 560), "♪ Narration on — Hindi lines on screen", font=font(24), fill="#8f8a7d")
    pw = int(W * tfrac); d.rectangle([0, H - 14, pw, H], fill="#C96A1B")
    d.rectangle([pw, H - 14, W, H], fill="#3A3A3C")
    return img

def parse(i):
    t = open(f"{A}/scene{i}.txt", encoding="utf-8").read().splitlines()
    img = [l[4:] for l in t if l.startswith("IMG=")][0]
    cap = [l[4:] for l in t if l.startswith("CAP=")][0]
    return img, cap

import numpy as np
tmp = f"{M}/demo_silent.mp4"
wr = imageio.get_writer(tmp, fps=FPS, codec="libx264", quality=7)
durs = []
for i in range(10):
    imgf, title = parse(i)
    dur = scene_len(i) + 1.2
    durs.append(dur)
    nfr = int(dur * FPS)
    for f in range(nfr):
        fr = frame(imgf, title, CAPS[i], i, 10, (sum(durs[:-1]) + f / FPS) / (sum(durs) + 0.01))
        wr.append_data(np.array(fr))
    print(f"scene{i}: {dur:.1f}s")
wr.close()

# concat audio with 0.6s gaps (match +1.2s video pad: 0.6 lead-in already by pad distribution)
auds = []
params = None
for i in range(10):
    w = wave.open(f"{A}/scene{i}.wav")
    if params is None: params = (w.getnchannels(), w.getsampwidth(), w.getframerate())
    auds.append(w.readframes(w.getnframes())); w.close()
ch, sw, fr = params
gap = struct.pack("<" + "h" * int(fr * 1.2) * ch, *([0] * int(fr * 1.2) * ch)) if sw == 2 else b"\x00" * int(fr * 1.2) * ch * sw
raw = gap.join(auds) + gap
out_w = f"{M}/demo_audio.wav"
o = wave.open(out_w, "wb"); o.setnchannels(ch); o.setsampwidth(sw); o.setframerate(fr)
o.writeframes(raw); o.close()

ff = imageio_ffmpeg.get_ffmpeg_exe()
out = f"{M}/demo_video_full.mp4"
import subprocess
subprocess.run([ff, "-y", "-i", tmp, "-i", out_w, "-c:v", "copy", "-c:a", "aac", "-shortest", out], check=True)
print("saved:", out, os.path.getsize(out) // 1024, "KB")
