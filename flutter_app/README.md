# Suraksha Parchi — Flutter App | Team CHANAKYA

Real Android/iOS app. Mirrors the web MVP (`mvp/`) screen-for-screen, same verified
datasets bundled as assets (49 medicines, 12 interaction rules, Jan Aushadhi,
Ayushman, helplines).

## Prereqs
- Flutter SDK 3.22+ (`flutter doctor`)
- Firebase project `suraksha-parchi`: `dart pub global activate flutterfire_cli && flutterfire configure`
- Secrets NEVER in code — pass at run time:
```
flutter run --dart-define=NEON_URL=postgresql://... \
  --dart-define=APPWRITE_KEY=... --dart-define=GEMINI_KEY=... --dart-define=BHASHINI_KEY=...
```

## Run
```
cd flutter_app
flutter pub get
flutter run
```

## Build (also runs in CI)
```
flutter build apk --debug
```

## Structure
- `lib/screens/` — home, fillup (camera + ML Kit OCR), result (disease, timetable,
  alerts, Jan Aushadhi savings, voice, Sehat File), suvidha, shell (nav + drawer)
- `lib/engine/rules.dart` — grounded rules: brand→generic, interactions, varied phrasing
- `lib/services/` — ocr (hybrid), tts (hi/bn/mr), needle2 (autostart status),
  store (Hive local + Neon/Appwrite plug-in)
- `lib/l10n/strings.dart` — all UI strings hi/bn/mr, no hardcoding
- `assets/data/` — copied from `mvp/data` (single source of truth)

## Backend wiring (Neon + Appwrite + Firebase)
- Firebase: `google-services.json` / `GoogleService-Info.plist` (gitignored) + FCM for reminders
- Neon: `sql/seed_medicines.sql` + `sql/seed_govt.sql`, connect with `NEON_URL`
- Appwrite: Auth (phone OTP) + Storage (parchi photos), `APPWRITE_KEY` server-side
- Needle-2: `engine/needle2.cact` verified via `engine/test_needle2.py`; mobile binding is Phase 2
