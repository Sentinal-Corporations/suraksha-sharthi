# Suraksha Parchi — Technical Architecture | Team CHANAKYA
Contact: ayush4ru@gmail.com | Stack: Flutter + Firebase + NeonDB (Postgres) + Appwrite

## Why 4 techs (jury-proof answer)
- **Flutter:** 1 codebase for Android demo + expo tablet. Fast UI for camera + pictograms.
- **Firebase:** ML Kit on-device OCR + FCM reminders + Crashlytics. Works offline.
- **Appwrite:** Auth (phone OTP for patient/ASHA) + Storage (parchi photos, lab PDFs). Self-host free, simple for school team.
- **NeonDB (Postgres):** Single source of truth for structured health data — Drug master, Sehat File timeline, reminders log. SQL = easy for judges to understand + scales to 10L users. Firebase Firestore alone gets messy for relational drug-disease joins.

Data flow:
```
Phone Camera -> Flutter crop
  -> Firebase ML Kit OCR (offline, fast) + confidence
  -> if conf < 0.70 -> Gemini 2.5 Flash Vision API (cloud smart read)
  -> Drug names -> query NeonDB drug_master (Postgres)
  -> Lite-RAG: retrieved drug rows + lab_range + ICMR snippet -> Gemini Flash text (via OpenRouter/Groq fallback)
  -> Response JSON -> NeonDB sehat_file insert + Appwrite Storage save image
  -> Bhashini TTS (hi/bn/mr) + Flutter_TTS offline fallback -> pictogram timetable UI
```

## OCR choice
- Primary offline: ML Kit Text Recognition v2 (Latin + Devanagari). Free, on-device.
- Fallback print: Tesseract (optional, for scanned prints).
- Smart: Gemini Vision for handwriting. Do NOT rely only on Tesseract — fails on cursive doctors.
- DO NOT use Snowboy/Porcupine/YAMNet — those are wake-word/sound-event, not needed. Use STT/TTS instead.

## Voice (hi, bn, mr)
- Primary: Bhashini API (free, Govt of India) — `asr hi/bn/mr` + `tts hi/bn/mr`.
- Fallback: Flutter_TTS + Google STT offline packs (expo WiFi dies).
- No training needed.

## Lite-RAG (no vector DB needed)
- Files in `/app`: drug_db.json (master, mirrors NeonDB), lab_range.json, rag_prompt.txt
- Retrieval = keyword match on drug name (lowercase, strip dose). Enough for 200 drugs, explainable to jury.
- LLM: Gemini 2.5 Flash primary (free tier ~15 RPM, Vision+text). Fallback Groq Llama-3.3 via OpenRouter free key. Never depend only on AgentRouter/OmniRouter live — keep cached demo.
- Guardrail: model must cite drug_db rows, must NOT prescribe new dose, must add disclaimer + red-flag referral.

## NeonDB schema (Postgres)
```sql
create table drug_master(
  name text primary key, mg text, disease_en text, icd11 text,
  hindi text, bengali text, marathi text, red_flag boolean, notes text
);
create table sehat_file(
  id uuid default gen_random_uuid() primary key,
  user_phone text, scan_type text, -- parchi|lab
  raw_text text, parsed_json jsonb, disease_guess text,
  lang text, created_at timestamptz default now()
);
```

## Free quotas (write in PPT)
Gemini Flash free, Bhashini free for hackathons, Neon free 3GB, Appwrite self-host free, Firebase Spark free. Total prototype cost < Rs.2000.

## Risks
Handwriting <70% -> human confirm buttons (tap correct drug). High-risk drugs (oncology/TB/pregnancy) -> no guess, refer to doctor. Offline -> cached last 5 scans + TTS works.
