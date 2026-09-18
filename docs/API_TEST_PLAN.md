# API + Test Plan — Suraksha Parchi | Team CHANAKYA

## API (MVP)
POST /scan {image} → {drugs:[{name,mg,conf}], raw_text} — 15s timeout, cached.
POST /explain {drugs, labs, lang} → {disease_guess, timetable[3], voice_script, red_flags[], disclaimer} — must cite drug_db.
POST /tts {text, lang} → mp3 — Bhashini, fallback local.
GET/DELETE /sehat-file?phone= → timeline; DELETE wipes DB+storage.
Errors: {code, message_hi} e.g. LOW_CONF → "Saaf photo lo", UNSAFE → refer.

## Test plan (20 parchis)
T1 printed Crocin → 100% hit. T2 cursive Azithro → Vision escalates, ≥80%. T3 Dolo+Crocin → RED duplicate fires. T4 Metformin+HbA1c8.2 → sugar story + diet + recheck. T5 Bengali/Marathi toggle → voice plays. T6 airplane mode → cached timetable + TTS works. T7 high-risk (e.g. chemo name) → refer-only, no guess. T8 delete → DB+bucket gone. Exit: 16/20 pass + all safety tests pass.
Devices: Rs.6000 Android + expo tablet. Log in Neon dashboard.
