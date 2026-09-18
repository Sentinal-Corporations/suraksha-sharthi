from PIL import Image, ImageDraw, ImageFont
import os
OUT = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi\branding"
os.makedirs(OUT, exist_ok=True)
W,H = 800,800
def font(s): 
    try: return ImageFont.truetype("arial.ttf", s)
    except: return ImageFont.load_default()

# 1. logo.png - shield style
img = Image.new("RGB",(W,H),"#0B1F22"); d = ImageDraw.Draw(img)
d.rounded_rectangle([180,90,620,560], radius=60, fill="#0E7C7B", outline="white", width=8)
d.rounded_rectangle([300,170,500,400], radius=18, fill="white")
d.rounded_rectangle([300,170,500,220], radius=18, fill="#FF7A1A")
for i,y in enumerate([250,280,310,340]): d.rounded_rectangle([320, y, 480 if i%2==0 else 440, y+14], radius=7, fill="#0B1F22" if i<3 else "#0E7C7B")
d.text((400,470),"SURAKSHA PARCHI", font=font(44), anchor="mm", fill="white")
d.text((400,520),"PHOTO LO • BHASHA ME SAMJHO", font=font(26), anchor="mm", fill="#FF7A1A")
d.text((400,580),"TEAM CHANAKYA", font=font(30), anchor="mm", fill="white")
d.text((400,630),"HI • BN • MR", font=font(28), anchor="mm", fill="white")
img.save(f"{OUT}/logo.png"); print("logo.png")

# 2. phone mock timetable
img2 = Image.new("RGB",(600,900),"#F4F7F6"); d2 = ImageDraw.Draw(img2)
d2.rounded_rectangle([150,60,450,860], radius=50, fill="#0B1F22")
d2.rounded_rectangle([165,75,435,845], radius=40, fill="white")
d2.rounded_rectangle([165,75,435,170], radius=40, fill="#0E7C7B")
d2.text((300,120),"Subah • Dopahar • Raat", font=font(26), anchor="mm", fill="white")
rows=[("☀ Subah 8AM","Crocin 650 — 1 goli","#0E7C7B"),("☁ Dopahar 2PM","Azithro 500 — 1 goli","#FF7A1A"),("🌙 Raat 9PM","Crocin 650 — 1 goli","#0E7C7B")]
y=220
for t,s,c in rows:
    d2.rounded_rectangle([185, y, 415, y+150], radius=18, fill="white", outline=c, width=5)
    d2.text((300, y+45), t, font=font(26), anchor="mm", fill="black")
    d2.text((300, y+95), s, font=font(22), anchor="mm", fill="black")
    y+=175
d2.rounded_rectangle([185, y, 415, y+70], radius=14, fill="#D7263D")
d2.text((300, y+35),"⚠ Duplicate dose alert!", font=font(22), anchor="mm", fill="white")
img2.save(f"{OUT}/phone-timetable.png"); print("phone")

# 3. journey diagram
img3 = Image.new("RGB",(1200,400),"white"); d3 = ImageDraw.Draw(img3)
steps=[("1 SCAN","parchi photo","#0E7C7B"),("2 READ","Hybrid OCR","#FF7A1A"),("3 SAMJHO","hi/bn/mr voice","#0E7C7B"),("4 YAAD","reminder+alert","#D7263D")]
x=40
for t,s,c in steps:
    d3.rounded_rectangle([x,80,x+250,300], radius=24, fill=c)
    d3.text((x+125,170),t, font=font(36), anchor="mm", fill="white")
    d3.text((x+125,225),s, font=font(26), anchor="mm", fill="white")
    if x<900: d3.text((x+265,190),">", font=font(60), fill="black")
    x+=290
img3.save(f"{OUT}/journey.png"); print("journey")

# 4. architecture strip
img4 = Image.new("RGB",(1200,420),"#0B1F22"); d4 = ImageDraw.Draw(img4)
boxes=[("Flutter\nCamera","#0E7C7B"),("ML Kit\n+Gemini\nVision","#FF7A1A"),("NeonDB\n+Appwrite","#0E7C7B"),("Bhashini\nVoice","#FF7A1A")]
x=40
for t,c in boxes:
    d4.rounded_rectangle([x,90,x+250,320], radius=24, fill=c)
    d4.multiline_text((x+125,205),t, font=font(30), anchor="mm", fill="white", align="center", spacing=6)
    if x<900: d4.text((x+262,190),">", font=font(55), fill="white")
    x+=290
img4.save(f"{OUT}/architecture.png"); print("arch")

# 5. parchi sample (fake handwritten style)
img5 = Image.new("RGB",(700,500),"white"); d5 = ImageDraw.Draw(img5)
d5.rectangle([0,0,700,90], fill="#0E7C7B")
d5.text((350,45),"Dr. Sharma  •  Rx", font=font(36), anchor="mm", fill="white")
d5.text((60,150),"Tab. Crocin 650 — 1-0-1 x 5 days", font=font(30), fill="black")
d5.text((60,220),"Tab. Azithro 500 — 1-0-0 x 3 days", font=font(30), fill="black")
d5.text((60,290),"Syp. Cough — 2 tsp night", font=font(30), fill="black")
d5.text((60,380),"HbA1c 8.2 • BP 150/95", font=font(28), fill="#D7263D")
img5.save(f"{OUT}/sample-parchi.png"); print("parchi")
