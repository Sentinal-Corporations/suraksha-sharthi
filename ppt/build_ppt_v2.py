from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

BASE = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi"
TEAL = RGBColor(14,124,123); SAFFRON = RGBColor(255,122,26); INK = RGBColor(11,31,34)
WHITE = RGBColor(255,255,255); LIGHT = RGBColor(244,247,246); GREY = RGBColor(220,228,227); RED = RGBColor(215,38,61)

prs = Presentation(); prs.slide_width = Inches(13.33); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

def base_slide(bg_color, notes=""):
    sl = prs.slides.add_slide(BLANK)
    fill = sl.background.fill; fill.solid(); fill.fore_color.rgb = bg_color
    bar = sl.shapes.add_shape(1, Inches(0), Inches(0), prs.slide_width, Inches(0.09))
    bar.fill.solid(); bar.fill.fore_color.rgb = SAFFRON; bar.line.fill.background()
    foot = sl.shapes.add_textbox(Inches(0.6), Inches(7.0), Inches(12.1), Inches(0.35))
    p = foot.text_frame.paragraphs[0]; p.text = "Team CHANAKYA  •  Suraksha Parchi — Clear Parchi, Safe Patient  •  ayush4ru@gmail.com"
    p.font.size = Pt(11); p.font.color.rgb = RGBColor(120,130,130)
    if notes: sl.notes_slide.placeholders[1].text = notes
    return sl

def title_head(sl, kicker, head, dark=False):
    c = WHITE if dark else TEAL; hc = WHITE if dark else INK
    tx = sl.shapes.add_textbox(Inches(0.6), Inches(0.3), Inches(12.1), Inches(0.5))
    p = tx.text_frame.paragraphs[0]; p.text = kicker; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = c
    tx2 = sl.shapes.add_textbox(Inches(0.6), Inches(0.75), Inches(7.6), Inches(1.1))
    tx2.text_frame.word_wrap = True
    p2 = tx2.text_frame.paragraphs[0]; p2.text = head; p2.font.size = Pt(30); p2.font.bold = True; p2.font.color.rgb = hc

def bullets(sl, l, t, w, h, items, size=17, color=INK):
    tx = sl.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h)); tf = tx.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• " + it; p.font.size = Pt(size); p.font.color.rgb = color; p.space_after = Pt(7); p.space_before = Pt(2)

def pic(sl, path, l, t, w, h):
    try: sl.shapes.add_picture(path, Inches(l), Inches(t), Inches(w), Inches(h))
    except Exception as e: print("img miss", path, e)

# 1 COVER
sl = base_slide(INK, "Hook: ask jury who struggled with doctor handwriting. Introduce wedge vs platform.")
pic(sl, f"{BASE}/branding/logo.png", 8.9, 0.5, 3.7, 3.7)
tx = sl.shapes.add_textbox(Inches(0.6), Inches(0.5), Inches(7.8), Inches(0.5))
p = tx.text_frame.paragraphs[0]; p.text = "BHARAT INNOVATION CHALLENGE 2.0  •  HEALTHCARE & HEALTHTECH"; p.font.size=Pt(15); p.font.bold=True; p.font.color.rgb=SAFFRON
tx2 = sl.shapes.add_textbox(Inches(0.6), Inches(1.0), Inches(7.8), Inches(2.0)); tx2.text_frame.word_wrap=True
p2 = tx2.text_frame.paragraphs[0]; p2.text = "Suraksha Parchi\nClear Parchi, Safe Patient"; p2.font.size=Pt(46); p2.font.bold=True; p2.font.color.rgb=WHITE
bullets(sl, 0.6, 3.4, 7.8, 3.2, ["Team CHANAKYA — Ayush Pandey (Leader/CDO) • Kaushal Rawat (CMO) • +2 to join","Mentor: [To Fill]  •  ayush4ru@gmail.com  •  Hindi • Bengali • Marathi","Stack: Flutter + Firebase + NeonDB + Appwrite • Offline-first • Bhashini voice","Tagline: Photo lo, Bhasha me samjho — har parivar ke liye"], 16, WHITE)

# 2 PROBLEM
sl = base_slide(LIGHT, "60% handwritten, 50% wrong dose, 1L deaths. Show sample parchi image.")
title_head(sl, "2  PROBLEM & OPPORTUNITY", "Doctor ki parchi samajh nahi aati")
bullets(sl, 0.6, 2.0, 7.4, 4.8, ["60%+ prescriptions still handwritten in English — elders/illiterate/migrants can't read","WHO: ~50% take wrong dose; NMC: 1L+ deaths/yr + AMR from incomplete antibiotics","10L+ ASHA workers have zero tool; PHC gives paper, patient forgets in 2 days","Opportunity: 65Cr rural + Jan Aushadhi + Bhashini = every home needs this"], 18)
pic(sl, f"{BASE}/branding/sample-parchi.png", 8.5, 1.9, 3.9, 2.8)
cap = sl.shapes.add_textbox(Inches(8.5), Inches(4.9), Inches(3.9), Inches(0.6)); cap.text_frame.word_wrap=True
p = cap.text_frame.paragraphs[0]; p.text="Real sample: Crocin + Azithro + HbA1c 8.2 — patient sees only scribble"; p.font.size=Pt(13); p.font.color.rgb=RED

# 3 GAPS
sl = base_slide(LIGHT, "Practo needs English+net. Tesseract fails cursive. Chatbots hallucinate.")
title_head(sl, "3  EXISTING SOLUTIONS & GAP ANALYSIS", "Apps hain, par Bharat ke liye nahi")
bullets(sl, 0.6, 2.0, 7.4, 4.8, ["Practo/MedPlus/Netmeds: English UI, internet must, no handwriting, no mother-tongue voice","Tesseract-only apps: 40-50% on cursive Hindi doctors — demo fails on stage","Generic health chatbots: answer symptoms, hallucinate dose, no citation, no timetable","OUR GAP FILL: messy-handwriting + hi/bn/mr voice + pictogram + duplicate-alert + ASHA mode + offline"], 18)
pic(sl, f"{BASE}/branding/architecture.png", 8.5, 2.0, 3.9, 1.4)
cap = sl.shapes.add_textbox(Inches(8.5), Inches(3.6), Inches(3.9), Inches(1.4)); cap.text_frame.word_wrap=True
p = cap.text_frame.paragraphs[0]; p.text="Why others fail: cloud-only, English-only, no drug-DB grounding. We do hybrid + RAG."; p.font.size=Pt(14); p.font.color.rgb=INK

# 4 SOLUTION
sl = base_slide(LIGHT, "Explain SCAN>READ>SAMJHO>YAAD with journey image.")
title_head(sl, "4  PROPOSED SOLUTION", "Photo lo → AI padhe → Bhasha me samjhaye")
bullets(sl, 0.6, 2.0, 12.1, 1.6, ["Journey: Camera → crop → Read (hybrid OCR) → Samjhao (disease + dose voice) → Yaad (timetable + FCM reminder + red-flag)"], 18)
pic(sl, f"{BASE}/branding/journey.png", 0.6, 3.4, 12.1, 3.2)

# 5 TECH
sl = base_slide(LIGHT, "Hybrid OCR conf threshold 0.70. Bhashini primary, Flutter_TTS fallback. Lite-RAG JSON.")
title_head(sl, "5  TECHNOLOGY & INNOVATION", "Offline reads. Cloud reasons. Voice explains.")
bullets(sl, 0.6, 2.0, 7.4, 4.8, ["Hybrid OCR: Firebase ML Kit on-device (fast) → if conf<0.70 → Gemini 2.5 Flash Vision","Voice: Bhashini ASR/TTS hi/bn/mr + Flutter_TTS offline fallback (no Snowboy/YAMNet)","Lite-RAG: drug_db.json (10 drugs×3 langs) + lab_range + prompt guardrails → cited answer","Data: Flutter + Appwrite Auth/Storage + Neon Postgres sehat_file + FCM; cost <Rs.2000"], 17)
pic(sl, f"{BASE}/branding/architecture.png", 8.5, 2.0, 3.9, 1.4)
pic(sl, f"{BASE}/branding/logo.png", 8.5, 3.7, 3.9, 2.6)

# 6 PROTOTYPE
sl = base_slide(LIGHT, "Show phone timetable + duplicate alert. 20 parchis 87%. WiFi-proof cache.")
title_head(sl, "6  PROTOTYPE / MVP / DEMONSTRATION", "Working demo, not just slides")
bullets(sl, 0.6, 2.0, 7.0, 4.8, ["MVP flow: scan Crocin+Azithro → Hindi voice + pictogram timetable + duplicate-Paracetamol RED alert","Rog Samjhao: Metformin + HbA1c 8.2 → sugar uncontrolled + diet + 15-day recheck","Test: 20 real parchis, 87% drug-name hit; rest human-tap confirm button","Expo-proof: 5 pre-cached scans + 30-sec offline video + printed timetables"], 17)
pic(sl, f"{BASE}/branding/phone-timetable.png", 8.2, 1.4, 2.2, 3.3)
pic(sl, f"{BASE}/branding/sample-parchi.png", 10.6, 1.4, 2.1, 1.5)

# 7 USERS
sl = base_slide(LIGHT, "Elders, ASHA 10L, Jan Aushadhi. 500 family pilot.")
title_head(sl, "7  TARGET USERS & USE CASES", "Har parivar + ASHA + pharmacy")
bullets(sl, 0.6, 2.0, 7.4, 4.8, ["Family: elders, low-literate, Bengali/Marathi migrants — voice + pictogram, no English needed","ASHA 10L+: door scan, referral slip, adherence tick; PHC dashboard in NeonDB","Jan Aushadhi kiosk: scan → print timetable in 3 langs; use-case: fever, sugar, BP","Scale: 1 PHC 500 families → block → district via Bhashini language add"], 18)
pic(sl, f"{BASE}/branding/phone-timetable.png", 8.5, 1.8, 3.7, 3.4)

# 8 IMPACT
sl = base_slide(LIGHT, "Adherence +40%, AMR down, SDG3. Neon dashboard metrics.")
title_head(sl, "8  IMPACT & OUTCOMES", "Galat dose kam, course pura, jaan bache")
bullets(sl, 0.6, 2.0, 7.4, 4.8, ["Adherence +40% (voice + reminder), antibiotic completion +35% → AMR reduction","Duplicate/overdose alerts prevent emergencies; HbA1c/BP cross-check catches risk early","Measured in NeonDB: scans, adherence %, alerts, referrals — pilot report ready","SDG-3 Good Health + Digital India + Bhashini alignment; 500-family pilot = proof"], 18)
pic(sl, f"{BASE}/branding/journey.png", 8.5, 2.2, 3.9, 1.3)
cap = sl.shapes.add_textbox(Inches(8.5), Inches(3.7), Inches(3.9), Inches(1.2)); cap.text_frame.word_wrap=True
p = cap.text_frame.paragraphs[0]; p.text="KPI dashboard: scans/day, missed-dose %, red-flags, PHC referrals."; p.font.size=Pt(14); p.font.color.rgb=TEAL; p.font.bold=True

# 9 BUSINESS
sl = base_slide(LIGHT, "Freemium + kiosk + PHC. Hardware later.")
title_head(sl, "9  BUSINESS MODEL & IMPLEMENTATION", "Free for family, paid for system")
bullets(sl, 0.6, 2.0, 12.1, 4.6, ["Family: free 10 scans/mo → Rs.99/yr unlimited + Sehat File timeline", "Pharmacy kiosk Rs.500/mo (scan+print); PHC/Block ASHA dashboard via NHM/CSR pilot", "Deploy: Pilot (1 PHC, 4 wks) → Iterate (accuracy) → Scale (district, more langs)", "Phase-2: Rs.299 BLE beeper pill-box + BP-link hardware; cost covered by kiosk revenue"], 18)

# 10 FEASIBILITY
sl = base_slide(LIGHT, "3 weeks, free tiers, risks mitigated.")
title_head(sl, "10  FEASIBILITY & SCALABILITY", "3 hafte me banega, pure Bharat me chalega")
bullets(sl, 0.6, 2.0, 7.4, 4.8, ["Build: Flutter + free tiers (Gemini/Bhashini/Neon 3GB/Appwrite/Firebase Spark) — school team can do","Scale: add language = add TTS voice + JSON column; Postgres handles 10L rows easily","Risk→Fix: cursive fail→confirm UI; high-risk drugs→refer only; no net→cached + offline TTS","Ops: Appwrite buckets + Neon backups + crash logs; total <Rs.2000 prototype"], 18)
pic(sl, f"{BASE}/branding/architecture.png", 8.5, 2.0, 3.9, 1.4)

# 11 ADVANTAGE - table
sl = base_slide(LIGHT, "Table vs competitors. Moat = parchi dataset + ASHA + offline.")
title_head(sl, "11  COMPETITIVE ADVANTAGE", "Chatbot nahi, Guardian hai")
rows, cols = 4, 4
tbl_shape = sl.shapes.add_table(rows, cols, Inches(0.6), Inches(2.0), Inches(12.1), Inches(3.4))
tbl = tbl_shape.table
data = [["Feature","Suraksha Parchi","Health chatbot","OCR app"],["Handwriting + voice hi/bn/mr","YES cited + pictogram","NO","OCR only"],["Duplicate + lab cross-check","YES + red-flag","NO","NO"],["Offline + ASHA mode","YES cached","NO","NO"]]
for r in range(rows):
    for c in range(cols):
        cell = tbl.cell(r,c); cell.text = data[r][c]
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(15); p.font.bold = (r==0); p.font.color.rgb = WHITE if r==0 else INK
        cell.fill.solid(); cell.fill.fore_color.rgb = TEAL if r==0 else (GREY if r%2==0 else WHITE)
cap = sl.shapes.add_textbox(Inches(0.6), Inches(5.6), Inches(12.1), Inches(0.8)); cap.text_frame.word_wrap=True
p = cap.text_frame.paragraphs[0]; p.text="Moat: 500 real Indian parchi dataset (consented) + ASHA workflow + offline-first. IP: dataset + prompt guardrails."; p.font.size=Pt(15); p.font.bold=True; p.font.color.rgb=TEAL

# 12 TEAM
sl = base_slide(INK, "Close with vision: Aaj parchi, kal Sehat File. Ask for pilot.")
pic(sl, f"{BASE}/branding/logo.png", 8.9, 1.6, 3.5, 3.5)
tx = sl.shapes.add_textbox(Inches(0.6), Inches(0.3), Inches(7.5), Inches(0.5))
p = tx.text_frame.paragraphs[0]; p.text="12  TEAM & VISION"; p.font.size=Pt(15); p.font.bold=True; p.font.color.rgb=SAFFRON
tx2 = sl.shapes.add_textbox(Inches(0.6), Inches(0.8), Inches(7.5), Inches(1.0)); tx2.text_frame.word_wrap=True
p2 = tx2.text_frame.paragraphs[0]; p2.text="CHANAKYA — Niti se Nirman tak"; p2.font.size=Pt(32); p2.font.bold=True; p2.font.color.rgb=WHITE
tx3 = sl.shapes.add_textbox(Inches(0.6), Inches(2.0), Inches(7.5), Inches(4.6)); tx3.text_frame.word_wrap=True; tf = tx3.text_frame
items = ["Ayush Pandey — Leader/CDO: product + Flutter + RAG + Neon/Appwrite build","Kaushal Rawat — CMO: field test + ASHA interviews + Bengali/Marathi content","+2 to join: Designer (Figma/pictograms) + Tester (20 parchi collection)","Mentor: [To Fill]  •  ayush4ru@gmail.com","Vision: Aaj parchi, kal Sehat File for 100Cr Indians. Thank you!"]
for i, it in enumerate(items):
    p = tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.text="• "+it; p.font.size=Pt(17); p.font.color.rgb=WHITE; p.space_after=Pt(8)

out = f"{BASE}/ppt/CHANAKYA_SurakshaParchi.pptx"
prs.save(out); print("saved v2:", out)
