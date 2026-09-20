# Play Signing — Suraksha Parchi | Team CHANAKYA
Package: `com.chanakya.suraksha_parchi` • Label: Suraksha Parchi

## What was done here
- Upload keystore generated: `flutter_app/android/upload-keystore.jks`
  (alias `upload`, RSA-2048, 25y validity). NEVER commit it — gitignored.
- Passwords live ONLY in `flutter_app/android/key.properties` (gitignored).
  BACK IT UP (password manager + USB). If lost, Play Console can reset the
  upload key, but it costs days.
- `build.gradle.kts` signs `release` with it when `key.properties` exists,
  otherwise falls back to debug keys (so `flutter run` never breaks).

## Publish to Google Play (AAB, Play App Signing on)
1. `cd flutter_app && flutter build appbundle --release` → `build/app/outputs/bundle/release/app-release.aab`
2. Play Console → Create app → `Suraksha Parchi`, package `com.chanakya.suraksha_parchi`
3. Release → Production → Create release → upload the `.aab`
4. First upload enrolls you in **Play App Signing** (Google holds the final
   signing key; your upload key only proves authorship). Keep the upload keystore safe.
5. Fill content rating (Everyone), data safety (camera photos on-device, phone optional),
   target audience 13+, then Rollout.

## Why Play refused installs before
Unsigned/`debug`-signed bundles are rejected by Play and flagged by Play Protect
on sideload. A signed `.aab` via Play Console is the only supported path.

## Safety note
Passwords in this doc's sibling `key.properties` are real. Copy them to a password
manager NOW, and consider rotating if anyone outside the team saw this machine.
