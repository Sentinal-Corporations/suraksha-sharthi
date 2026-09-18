import json
BASE = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi"
meds = json.load(open(f"{BASE}/mvp/data/medicines.json", encoding="utf-8"))["medicines"]
rules = json.load(open(f"{BASE}/mvp/data/interactions.json", encoding="utf-8"))["rules"]

def q(s):
    return "'" + str(s).replace("'", "''") + "'"

lines = ["-- Suraksha Parchi seed for Neon (cool-math-10984187 / production)",
"-- Run: psql $NEON_DATABASE_URL -f sql/seed_medicines.sql", "",
"create table if not exists drug_master(",
"  name text primary key, brands text[] not null default '{}',",
"  mg text[] not null default '{}', disease_en text, icd11 text,",
"  hindi text, bengali text, marathi text,",
"  dz_hi text, dz_bn text, dz_mr text,",
"  red_flag boolean default false, notes text);", "",
"create table if not exists interaction_rules(",
"  id serial primary key, generics text[] not null, level text not null,",
"  hi text, bn text, mr text);", "",
"create table if not exists sehat_file(",
"  id uuid default gen_random_uuid() primary key,",
"  user_phone text, scan_type text, raw_text text,",
"  parsed_json jsonb, disease_guess text, lang text,",
"  created_at timestamptz default now());", ""]

for m in meds:
    brands = "ARRAY[" + ",".join(q(b) for b in m.get("brands", [])) + "]"
    mg = "ARRAY[" + ",".join(q(x) for x in m.get("mg", [])) + "]"
    dz = m.get("dz", {})
    lines.append(f"insert into drug_master(name,brands,mg,disease_en,icd11,hindi,bengali,marathi,dz_hi,dz_bn,dz_mr,red_flag,notes) values({q(m['name'])},{brands},{mg},{q(m.get('disease_en',''))},{q(m.get('icd11',''))},{q(m.get('hi',''))},{q(m.get('bn',''))},{q(m.get('mr',''))},{q(dz.get('hi',''))},{q(dz.get('bn',''))},{q(dz.get('mr',''))},{str(bool(m.get('red_flag'))).lower()},{q(m.get('note',''))}) on conflict(name) do update set brands=excluded.brands,mg=excluded.mg,disease_en=excluded.disease_en,icd11=excluded.icd11,hindi=excluded.hindi,bengali=excluded.bengali,marathi=excluded.marathi,dz_hi=excluded.dz_hi,dz_bn=excluded.dz_bn,dz_mr=excluded.dz_mr,red_flag=excluded.red_flag,notes=excluded.notes;")

lines.append("")
for r in rules:
    g = "ARRAY[" + ",".join(q(x) for x in r["generics"]) + "]"
    lines.append(f"insert into interaction_rules(generics,level,hi,bn,mr) values({g},{q(r['level'])},{q(r['hi'])},{q(r['bn'])},{q(r['mr'])});")

out = f"{BASE}/sql/seed_medicines.sql"
open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote", out, len(meds), "meds +", len(rules), "rules")

# Govt datasets: Jan Aushadhi prices, PM-JAY packages, helplines
ja = json.load(open(f"{BASE}/mvp/data/jan_aushadhi.json", encoding="utf-8"))
ja = ja.get("prices", ja.get("meta", {}))
ab = json.load(open(f"{BASE}/mvp/data/ayushman.json", encoding="utf-8"))
hl = json.load(open(f"{BASE}/mvp/data/helplines.json", encoding="utf-8"))
g = ["-- Govt datasets seed (indicative, verify live)", "",
"create table if not exists jan_aushadhi(generic text, pack text, branded_mrp int, ja_price int);",
"create table if not exists pmjay_packages(name text, code text, indicative_price int, note text);",
"create table if not exists helplines(name text, number text, when_hi text, when_bn text, when_mr text);", ""]
for p in ja["prices"]:
    g.append(f"insert into jan_aushadhi values({q(p['generic'])},{q(p['pack'])},{p['branded_mrp']},{p['ja_price']});")
g.append("")
for p in ab["packages"]:
    g.append(f"insert into pmjay_packages values({q(p['name'])},{q(p['code'])},{p['indicative_price']},{q(p['note'])});")
g.append("")
for h in hl["helplines"]:
    g.append(f"insert into helplines values({q(h['name'])},{q(h['number'])},{q(h['when_hi'])},{q(h['when_bn'])},{q(h['when_mr'])});")
out2 = f"{BASE}/sql/seed_govt.sql"
open(out2, "w", encoding="utf-8").write("\n".join(g) + "\n")
print("wrote", out2, len(ja["prices"]), "prices +", len(ab["packages"]), "packages +", len(hl["helplines"]), "helplines")
