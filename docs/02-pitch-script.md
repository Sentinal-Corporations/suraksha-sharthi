# 7-Minute Live Pitch — Team CHANAKYA | Suraksha Parchi
Members: Ayush Pandey (Leader/CDO), Kaushal Rawat (CMO) | Email: ayush4ru@gmail.com

## 0:00-1:00 Hook (Ayush)
"Haath uthao — kisne doctor ki parchi padhne me struggle kiya? Meri dadi ne Crocin ki jagah 2 dawaiyan kha li thi. Bharat me 50% log galat dose lete hain. Hum hain Team CHANAKYA, ye hai Suraksha Parchi."

## 1:00-3:00 Live Demo (Ayush, phone to projector)
1. Messy parchi photo lo → ML Kit fast read → Gemini Vision smart read.
2. Play Hindi voice: "Subah 1 goli khane ke baad, 5 din tak."
3. Show Bengali + Marathi toggle + pictogram timetable (illiterate-friendly).
4. Show alert: "2 Paracetamol brands together — Doctor se poochhein!"

Backup line if WiFi fails: "Internet slow hai — dekhiye cached offline demo, yehi hamari strength hai."

## 3:00-5:00 Rog Samjhao (Kaushal)
"Ye sirf dose nahi batata, bimari samjhata hai. Metformin + report HbA1c 8.2 = sugar uncontrolled. AI Grade-5 Hindi me: parhez, walk, 15 din me re-check. Lab + parchi cross-check — koi chatbot ye nahi karta."

## 5:00-6:00 Tech in 30 sec (Ayush)
"Hybrid OCR offline-first, Bhashini voice hi/bn/mr, Lite-RAG drug_db se cite, Flutter + Appwrite + NeonDB Sehat File. Cost <2000."

## 6:00-7:00 Impact + Vision (Kaushal)
"500 family pilot, ASHA ke saath. Aaj parchi, kal Sehat File + Rs.299 pill-box hardware. Clear Parchi, Safe Patient. Dhanyavaad!"

## Q&A bank
- Accuracy? 87% on 20 parchis, rest human-tap confirm; high-risk → refer only.
- Doctor replacement? No — literacy + reminder + referral, disclaimer every screen.
- Offline? Yes — last 5 scans + TTS cached; smart read needs net once.
- Why Firebase+Neon+Appwrite? Firebase ML/FCM, Appwrite auth/storage simple, Neon SQL for relational health timeline.
- Privacy? Phone-OTP, Appwrite private buckets, delete button, no name needed.
- Scale? Add language = add voice + JSON column; PHC → district via Bhashini.
