from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

TEAL = RGBColor(14,124,123); SAFFRON = RGBColor(255,122,26); INK = RGBColor(11,31,34); WHITE = RGBColor(255,255,255); LIGHT = RGBColor(244,247,246); RED = RGBColor(215,38,61)

prs = Presentation(); prs.slide_width = Inches(13.33); prs.slide_height = Inches(7.5)
def bg(slide, color):
    fill = slide.background.fill; fill.solid(); fill.fore_color.rgb = color
def add_bar(slide, top=0):
    from pptx.util import Inches as I
    shp = slide.shapes.add_shape(1, I(0), I(top), prs.slide_width, I(0.08)); shp.fill.solid(); shp.fill.fore_color.rgb = SAFFRON; shp.line.fill.background()
def textbox(slide, l, t, w, h, text, size=20, bold=False, color=INK, align=PP_ALIGN.LEFT):
    tx = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h)); tf = tx.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = text; p.font.size = Pt(size); p.font.bold = bold; p.font.color.rgb = color; p.alignment = align; return tx
def bullets(slide, l, t, w, h, items, size=18):
    tx = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h)); tf = tx.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.text = "• " + it; p.font.size = Pt(size); p.font.color.rgb = INK; p.space_after = Pt(6)

slides = [
 ("COVER", "Suraksha Parchi\nClear Parchi, Safe Patient", ["Team CHANAKYA | Theme: Healthcare & HealthTech", "Members: Ayush Pandey (Leader / CDO) • Kaushal Rawat (CMO) • +2 to join | Mentor: [To Fill]", "Contact: ayush4ru@gmail.com | Languages: Hindi • Bengali • Marathi | Stack: Flutter + Firebase + NeonDB + Appwrite"]),
 ("2  PROBLEM & OPPORTUNITY", "Doctor ki parchi samajh nahi aati — har ghar ki problem", ["60%+ prescriptions handwritten in English; 50% patients take wrong dose (WHO)", "NMC: 1L+ deaths/yr medication errors; AMR from incomplete antibiotic course", "10L+ ASHA workers have no tool; elders + illiterate + migrants hit hardest", "Opp: 65Cr rural + Jan Aushadhi scale; every family needs it"]),
 ("3  EXISTING SOLUTIONS & GAPS", "Apps hain, par Bharat ke liye nahi", ["Practo/MedPlus: need English + internet, no handwriting, no voice in mother-tongue", "Tesseract alone: fails on cursive; generic chatbots hallucinate dose", "Gap: offline-first + messy-handwriting + pictogram + drug-interaction + ASHA mode — nobody does all 5"]),
 ("4  OUR SOLUTION", "Photo lo → AI padhe → Bhasha me samjhaye → Yaad dilaye", ["User journey: Camera → crop → Read → Samjhao (disease + dose voice hi/bn/mr) → Timetable + reminders", "Rog Samjhao: drug-combo + lab cross-check → probable disease in Grade-5 words", "Sehat File: every parchi+lab timeline stored in NeonDB; red-flag referral, never new prescription"]),
 ("5  TECHNOLOGY & INNOVATION", "Offline reads. Cloud reasons. Voice explains.", ["Hybrid OCR: ML Kit on-device (fast) → if conf<0.70 → Gemini 2.5 Flash Vision (smart)", "Voice: Bhashini ASR/TTS hi/bn/mr + Flutter_TTS offline fallback; no Snowboy/YAMNet needed", "Lite-RAG: drug_db.json + lab_range + ICMR snippet → Gemini Flash, Groq/OpenRouter fallback", "App: Flutter + Appwrite Auth/Storage + Neon Postgres sehat_file + FCM reminders. Cost <Rs.2000"]),
 ("6  PROTOTYPE / MVP", "Working demo, not just slides", ["MVP: scan Crocin+Azithro parchi → Hindi voice + pictogram timetable + duplicate-Paracetamol alert", "Test: 20 real parchis, 87% drug-name accuracy, human-tap confirm for rest", "Expo kit: phone + tablet + 5 pre-cached parchis + offline video backup (WiFi-proof)", "Files in /app: drug_db.json (10 drugs ×3 langs), lab_range.json, rag_prompt.txt"]),
 ("7  TARGET USERS", "Har parivar + ASHA + pharmacy", ["Primary: elders, low-literate, migrants (Hindi/Bengali/Marathi)", "ASHA 10L+: door-to-door scan + referral; PHC + Jan Aushadhi kiosk", "Scale: 1 PHC pilot 500 families → district → state via Bhashini language add"]),
 ("8  IMPACT & OUTCOMES", "Galat dose kam, course pura, jaan bache", ["Adherence +40% (reminder + voice), antibiotic completion +35% → AMR down", "Duplicate-dose alerts prevent emergencies; lab cross-check catches uncontrolled sugar/BP early", "SDG-3 Good Health; measurable: scans, adherence ticks, referrals in NeonDB dashboard"]),
 ("9  BUSINESS MODEL", "Free for family, paid for system", ["Freemium: family free 10 scans/mo; Rs.99/yr unlimited + Sehat File", "B2B: pharmacy kiosk Rs.500/mo, PHC/ASHA dashboard per block", "Roadmap: Phase-2 Rs.299 beeper pill-box + BP-link hardware; funded via BIC + NHM pilot"]),
 ("10  FEASIBILITY & SCALABILITY", "3 weeks me banega, pure Bharat me chalega", ["Built: Flutter dev + free tiers (Gemini/Bhashini/Neon/Appwrite/Firebase Spark)", "Ops: Postgres scales; add language = add TTS voice + 1 JSON column", "Risks: handwriting fail→confirm UI; high-risk drugs→refer only; no-internet→cached scans+offline TTS"]),
 ("11  COMPETITIVE ADVANTAGE", "Chatbot nahi, Guardian hai", ["vs Health-chatbots: we read YOUR parchi + YOUR lab, cite DB, no hallucinated dose", "vs OCR apps: we explain disease + diet + red-flags in mother-tongue voice + pictograms", "Moat: 500 real Indian parchi dataset + ASHA workflow + offline-first; IP potential"]),
 ("12  TEAM & VISION", "CHANAKYA — Niti se Nirman tak", ["Ayush Pandey — Leader/CDO: product + Flutter+RAG build", "Kaushal Rawat — CMO: field test + ASHA interviews + Marathi/Bengali content", "Mentor: [To Fill] + 2 members to join (design + testing)", "Vision: Aaj parchi, kal Sehat File for 100Cr Indians. Thank you! ayush4ru@gmail.com"]),
]

for idx, (title, head, pts) in enumerate(slides):
    sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl, LIGHT); add_bar(sl)
    if idx==0:
        bg(sl, INK)
        textbox(sl, 0.7, 0.4, 11.9, 0.7, "BHARAT INNOVATION CHALLENGE 2.0 • HEALTHCARE & HEALTHTECH", 16, True, SAFFRON, PP_ALIGN.LEFT)
        textbox(sl, 0.7, 1.2, 7.5, 2.2, head, 44, True, WHITE)
        bullets(sl, 0.7, 3.8, 7.5, 3.0, pts, 16)
        for s in sl.shapes:
            if s.has_text_frame:
                for p in s.text_frame.paragraphs:
                    for r in p.runs: 
                        if "•" in p.text: r.font.color.rgb = WHITE
        textbox(sl, 8.8, 1.2, 3.8, 4.5, "🛡️\nSURAKSHA\nPARCHI\n\nPhoto lo\nBhasha me samjho\n\nhi • bn • mr", 28, True, SAFFRON, PP_ALIGN.CENTER)
        textbox(sl, 0.7, 6.7, 11.9, 0.5, "Team CHANAKYA • ayush4ru@gmail.com", 14, False, WHITE)
    else:
        textbox(sl, 0.7, 0.35, 11.9, 0.7, title, 22, True, TEAL)
        textbox(sl, 0.7, 1.15, 11.9, 1.1, head, 30, True, INK)
        bullets(sl, 0.7, 2.6, 11.9, 4.4, pts, 19)

out = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi\ppt\CHANAKYA_SurakshaParchi.pptx"
prs.save(out); print("saved:", out)
