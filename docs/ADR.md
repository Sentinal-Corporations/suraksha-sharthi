# ADR — Architecture Decision Records | Team CHANAKYA

## ADR-001 Hybrid OCR (ML Kit + Gemini Vision) — Accepted
Context: Tesseract alone 40-50% on cursive; cloud-only dies offline. Decision: on-device first, cloud if conf<0.70. Consequence: WiFi-proof + smart read, slight latency when escalated.

## ADR-002 Bhashini + Flutter_TTS fallback, no Snowboy/YAMNet — Accepted
Context: need hi/bn/mr STT/TTS, not wake-word. Snowboy deprecated, YAMNet is sound-events. Decision: Bhashini primary (Bharat story, free), local TTS fallback. Consequence: expo demo works offline.

## ADR-003 Lite-RAG JSON over vector DB — Accepted
Context: 200 drugs, school team, explainable to jury. Decision: keyword match drug_db.json + prompt guardrails, cite rows. Consequence: no hallucinated dose, easy to demo; migrate to pgvector later.

## ADR-004 Neon Postgres + Appwrite + Firebase (all three) — Accepted
Context: need relational timeline + simple auth/storage + on-device ML/push. Decision: Neon = truth (SQL joins), Appwrite = auth/buckets, Firebase = ML Kit/FCM. Consequence: 3 free tiers, <Rs.2000; must document why each (jury Q).

## ADR-005 Gemini Flash primary, Groq/OpenRouter fallback — Accepted
Context: free routers flaky live. Decision: Gemini default, cached demo + video backup. Consequence: stable 7-min pitch.

## ADR-006 Refer-only safety, no new prescription — Accepted
Context: medical liability. Decision: explain only, red-flag refer, disclaimer every screen. Consequence: lower risk, higher jury trust.
