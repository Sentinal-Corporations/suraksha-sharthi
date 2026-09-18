import os, wave, textwrap
BASE = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi"
B = f"{BASE}/branding"; M = f"{BASE}/mvp"
SCENES = [
("logo.png", "HOOK — har ghar ki problem",
 "Raise your hand if you have ever struggled to read a doctor's handwriting. In India, more than sixty percent of prescriptions are still handwritten in English. My grandmother once took two medicines instead of one, because nobody could read the slip. We are Team Chanakya, and this is Suraksha Parchi. Clear parchi, safe patient."),
("sample-parchi.png", "PROBLEM — 50% galat dose",
 "The numbers are serious. Half of all patients take the wrong dose. One lakh deaths every year come from medication errors. Antibiotics stopped halfway create drug resistance. Ten lakh Asha workers, who carry healthcare to villages, have no tool for this. Elders, migrants, and low-literate families suffer the most."),
("architecture.png", "GAP — apps hain, Bharat ke liye nahi",
 "Apps exist, but not for Bharat. City apps need English and internet. Basic scanners fail on cursive handwriting. Generic chatbots guess doses and hallucinate. Nothing reads messy handwriting, speaks the dose in the mother tongue, warns of duplicate drugs, and works offline for an Asha worker. That gap is our product."),
("journey.png", "SOLUTION — Photo lo, Bhasha me samjho",
 "Our flow has four steps. Scan the parchi photo. Read it with hybrid A I, fast offline first, smart cloud when needed. Samjhao: the app explains the disease and dose with voice and pictures in Hindi, Bengali, or Marathi. Yaad: a morning noon night timetable with reminders, plus red alerts for dangerous combinations."),
("sample-parchi.png", "DEMO 1 — Scan to Read, 87%",
 "Watch the demo. We photograph a real messy parchi, Crocin plus Azithro. The offline reader gives sixty two percent confidence, so the smart reader takes over and reaches eighty seven percent. Anything unsure gets a tap to confirm button, so a human always stays in charge of handwriting the machine cannot read."),
("phone-timetable.png", "DEMO 2 — Rog Samjhao, 3 bhasha",
 "Now Rog Samjhao. The A I sees Metformin with a high sugar report and explains in grade five words: this is sugar, take it with food, walk daily, recheck in fifteen days. It speaks in Hindi, switches to Bengali and Marathi, and shows sun cloud moon pictograms, so even illiterate users follow the timetable."),
("phone-timetable.png", "DEMO 3 — Duplicate RED alert",
 "Here is the crowd moment. Add Dolo beside Crocin. Both are paracetamol brands. The app fires a red duplicate alert, overdose will damage the liver, ask the doctor. High risk drugs like insulin or T B medicines never get guesses, only a referral. Safety first, always."),
("architecture.png", "SUVIDHA — sarkari sahayata",
 "Beyond the parchi, the Suvidha section saves money and opens doors. Jan Aushadhi price check shows branded versus Kendra rates, metformin forty five rupees becomes fourteen. Ayushman Bharat guides the five lakh cashless cover, eligibility steps, and nineteen treatment packages. Helplines, one zero eight and more, call with one tap."),
("architecture.png", "TECH — 14MB AI, offline-first",
 "Under the hood: hybrid O C R, Bhashini voices plus offline fallback, and a verified database of forty nine medicines with twelve interaction rules. Our A I, Needle two, is fourteen megabytes, runs on the phone itself with no internet, and only calls our verified tools, never inventing doses. Low confidence means ask a human."),
("logo.png", "IMPACT — Team CHANAKYA",
 "Impact we can measure: adherence up forty percent, antibiotic courses completed, duplicate emergencies prevented, all tracked for a five hundred family health centre pilot. Team Chanakya: Ayush Pandey leads the build, Kaushal Rawat leads field testing. Today parchi, tomorrow the Sehat File for one hundred crore Indians. Thank you."),
]
for i, (img, cap, nar) in enumerate(SCENES):
    open(f"{M}/audio/scene{i}.txt", "w", encoding="utf-8").write(f"IMG={img}\nCAP={cap}\nNAR={nar}\n")
print("wrote", len(SCENES), "scene scripts")
