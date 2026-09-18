from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio, os
BASE = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi"
B = f"{BASE}/branding"; OUT = f"{BASE}/mvp/demo_video.mp4"
W,H = 1280,720; FPS=30
def font(s):
    try: return ImageFont.truetype("arial.ttf", s)
    except: return ImageFont.load_default()
def frame(bg_img, top, sub):
    img = Image.new("RGB",(W,H),"#0B1F22"); d = ImageDraw.Draw(img)
    try:
        im = Image.open(bg_img).convert("RGB"); im.thumbnail((560,460))
        img.paste(im,(80,140))
    except Exception as e: print("bg miss", e)
    d.rounded_rectangle([700,120,1210,600], radius=24, fill="white")
    d.multiline_text((955,300), top, font=font(44), anchor="mm", fill="#0B1F22", align="center", spacing=8)
    d.multiline_text((955,450), sub, font=font(28), anchor="mm", fill="#0E7C7B", align="center", spacing=6)
    d.text((640,40),"SURAKSHA PARCHI • TEAM CHANAKYA", font=font(30), anchor="mm", fill="#FF7A1A")
    return img
scenes=[
 (f"{B}/logo.png","Doctor ki parchi\nsamajh nahi aati?","Team CHANAKYA • BIC 2.0"),
 (f"{B}/sample-parchi.png","Crocin + Azithro\nscribble me?","50% galat dose • 1L deaths/yr"),
 (f"{B}/journey.png","Photo lo\nAI padhta hai","ML Kit offline → Gemini Vision"),
 (f"{B}/phone-timetable.png","Subah • Dopahar • Raat\npictogram timetable","Hindi • Bengali • Marathi voice"),
 (f"{B}/architecture.png","Duplicate dose?\nRED alert!","Dolo + Crocin = overdose warning"),
 (f"{B}/logo.png","Clear Parchi\nSafe Patient","ayush4ru@gmail.com • Pilot: 500 families"),
]
wr = imageio.get_writer(OUT, fps=FPS, codec="libx264", quality=8)
for bg, top, sub in scenes:
    fr = frame(bg, top, sub)
    import numpy as np
    arr = np.array(fr)
    for _ in range(FPS*5): wr.append_data(arr)
wr.close(); print("saved:", OUT, os.path.getsize(OUT))
