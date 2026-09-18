# PRD — Suraksha Parchi | Team CHANAKYA v1.0
Contact: ayush4ru@gmail.com | Date: Sep 2026 | Theme: Healthcare & HealthTech

## 1. Problem
Indian patients get handwritten English parchis they can't read. 50% wrong dose, 1L+ deaths/yr, AMR from incomplete course. ASHA (10L+) has no tool. Languages: Hindi, Bengali, Marathi must.

## 2. Goals / Non-goals
Goals: scan parchi+lab → explain disease + dose in mother-tongue voice + timetable + duplicate alert + reminders. Offline-first.
Non-goals: NOT a doctor, NO new prescription, NO diagnosis beyond probable-condition explanation, NO hardware in v1.

## 3. Users
P1 Patient family (elder/low-literate/migrant), P2 ASHA worker, P3 Jan Aushadhi pharmacist. Out-of-scope: doctors portal in v1.

## 4. User stories + acceptance
- US1 Scan: photo → drugs parsed in <15s, conf shown. Accept: 80%+ drug hit on 20 test parchis.
- US2 Samjhao: Hindi/Bengali/Marathi voice + pictogram timetable. Accept: plays offline if cached.
- US3 Rog Samjhao: drug-combo + lab → probable disease Grade-5 words + diet + red-flags. Accept: cites drug_db, shows disclaimer.
- US4 Alert: duplicate paracetamol / overdose → RED block + refer. Accept: triggers on Dolo+Crocin test.
- US5 Sehat File: history timeline in NeonDB. Accept: list by date, delete works.

## 5. Scope v1 (Sep-Nov 2026)
Flutter app: camera, OCR hybrid, RAG explain, TTS hi/bn/mr, timetable, FCM reminders, Appwrite auth/storage, Neon sehat_file. 10-drug DB + lab ranges.
v2 (later): 200 drugs, BP-link, Rs.299 pill-box, PHC dashboard.

## 6. Success metrics
Scans, adherence %, course completion %, alerts fired, referral taps, ASHA pilot 500 families, accuracy %, offline-play %.

## 7. Constraints
Free tiers only, <Rs.2000, school team build in 3 weeks, BIC 12-slide + 7-min pitch + expo demo, WiFi-proof.

## 8. Risks
Handwriting fail → confirm UI; hallucination → RAG cite + guardrail; privacy → OTP + delete; medical liability → disclaimer + refer-only.
