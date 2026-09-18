# Design Doc — Suraksha Parchi | Team CHANAKYA
Brand: branding/brand-kit.md | Assets: logo.png, phone-timetable.png, journey.png

## Design principles
Grade-5 words, 1 thumb reach, voice-first, pictogram-first for illiterate, RED only for danger, offline badge always visible.

## Screens
1. Home: big SCAN button (saffron), lang chips hi/bn/mr, Sehat File list. Teal header with logo.
2. Scan: camera frame + crop + "Saaf photo lo" hint + sample-parchi.png example.
3. Confirm: OCR text + conf % + tap-to-correct drug chips (critical for handwriting fails).
4. Samjhao: disease card ("Sugar ke liye lagta hai"), per-drug rows with ☀/☁/🌙 icons, diet box, red-flag box.
5. Timetable: phone-timetable.png style — 3 cards + speaker replay + FCM toggle.
6. Sehat File: timeline by date, lab badges, delete.

## Components
DrugCard, TimetableCard, AlertBanner (red), LangChip, VoiceBar, Pictograms (sun/cloud/moon + roti-cross for parhez). Fonts Poppins + Noto Sans Devanagari/Bengali. Min touch 48dp, contrast AA.

## Figma tasks for designer
Recreate 6 screens with teal #0E7C7B + saffron #FF7A1A, export PNG for PPT slide 6, poster A3 per poster/poster-content.md.
