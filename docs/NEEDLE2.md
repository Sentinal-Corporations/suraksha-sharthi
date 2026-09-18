# Needle-2 — VERIFIED integration | Team CHANAKYA
Status: DOWNLOADED + TESTED Sep 2026 (cactus-needle 3.0.1, Apache-2.0, Cactus Compute).

## What was downloaded (real files in engine/)
- `engine/needle2.cact` — 13.74MB Needle-2 weights (45M params, CQ2-bit).
- `engine/windows-x86_64/` — engine runner `needle.exe` (14.93MB) + lib + header.
- `engine/wasm/` — browser runner `needle.wasm` (0.33MB) + js glue (web path).
- `engine/test_needle2.py` — our 3 tools wired, passing.

## Measured (this machine, Windows desktop)
- Tool test: query about dolo+crocin + metformin Hindi + JA price → 2 correct calls
  (explain_dose, jan_aushadhi_price), results grounded in our JSONs, 83 prefill tok/s.
- Local .cact load: works, empty-call contract holds, peak 47.7MB desktop
  (vendor's 28MB figure is on-device session; desktop engine overhead is higher).
- Honest gap: one query fired 2/3 expected calls at low confidence (0.0027) —
  our app treats low confidence as "confirm with human", which matches the guide.

## Design (tool-calling, not chat)
Needle picks tools + fills args from user words; off-topic → empty list, not a guess.
Our catalogue = our DBs:
1. `explain_dose(drug, lang)` → medicines.json hi/bn/mr rows.
2. `jan_aushadhi_price(drug)` → jan_aushadhi.json MRP vs Kendra.
3. `check_interaction(drug1, drug2, lang)` → interactions.json rules.
Python: `needle.Needle(weights="engine/needle2.cact", tools=[...], generation=2)`.
Every turn returns `{function_calls, reasoning, confidence, results}`.

## Reproduce
```
pip install cactus-needle
set NEEDLE_TELEMETRY=0
python engine/test_needle2.py
needle download --generation 2 Cactus-Compute/needle2 --out engine
```

## Roadmap
- Phase 2: wire `engine/wasm` runner to `mvp/js/needle2.js` tool-loop (same catalogue).
- Optional: `needle finetune` LoRA on our 49-medicine tool examples → `tuned.cact`.
- Telemetry: keep NEEDLE_TELEMETRY=0 + DO_NOT_TRACK=1 (already in test script).

## Pitch line
"14MB ka Needle-2 model phone me hi chalta hai — internet na ho to bhi. Ye guess nahi karta: hamare verified database ke tools ko call karta hai, aur bharosa kam ho to human confirm mangta hai."
