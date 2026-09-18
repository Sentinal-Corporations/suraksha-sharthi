"""Needle-2 smoke test with Suraksha Parchi tools (generation=2). Telemetry off."""
import json, os
os.environ["NEEDLE_TELEMETRY"] = "0"
os.environ["DO_NOT_TRACK"] = "1"
import needle

BASE = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi\mvp\data"
MEDS = {m["name"]: m for m in json.load(open(f"{BASE}/medicines.json", encoding="utf-8"))["medicines"]}
JA = {p["generic"]: p for p in json.load(open(f"{BASE}/jan_aushadhi.json", encoding="utf-8"))["meta"]["prices"]}
RULES = json.load(open(f"{BASE}/interactions.json", encoding="utf-8"))["rules"]

@needle.tool
def explain_dose(drug: str, lang: str):
    "Explain a prescribed drug's dose and diet in the patient's language. lang is hi, bn or mr."
    m = MEDS.get(drug.lower())
    if not m:
        return {"found": False}
    return {"found": True, "disease": m["dz"].get(lang, m["disease_en"]), "how": m.get(lang, m["hi"])}

@needle.tool
def jan_aushadhi_price(drug: str):
    "Get Jan Aushadhi Kendra price vs branded MRP for a generic drug."
    p = JA.get(drug.lower())
    if not p:
        return {"found": False}
    return {"branded_mrp": p["branded_mrp"], "ja_price": p["ja_price"], "pack": p["pack"]}

@needle.tool
def check_interaction(drug1: str, drug2: str, lang: str):
    "Check interaction between two generic drugs. lang is hi, bn or mr."
    s = {drug1.lower(), drug2.lower()}
    for r in RULES:
        if set(r["generics"]) == s or (len(set(r["generics"])) == 1 and s == {r["generics"][0]}):
            return {"level": r["level"], "message": r.get(lang, r["hi"])}
    return {"level": "none", "message": "No known interaction."}

agent = needle.Needle(tools=[explain_dose, jan_aushadhi_price, check_interaction], generation=2)
q = "Patient takes dolo and crocin daily. Explain metformin dose in hindi and tell jan aushadhi price of metformin."
out = agent.run(q)
print(json.dumps(out, ensure_ascii=False, indent=1)[:3000])
