// Drug master loaded from data/drug_db.json at runtime (fetch) with inline fallback.
// behavior: DRUG_DB is source of truth for explain; keep in sync with NeonDB drug_master + data/drug_db.json
window.DRUG_DB_FALLBACK = [
 {n:"paracetamol",mg:"650mg",hi:"Bukhar/dard. Khane ke baad 1, max 3.",bn:"Jor/byatha. Khabar pore 1 ta.",mr:"Taap/dukh. Jevnanantar 1.",dz:{hi:"Bukhar",bn:"Jor",mr:"Taap"}},
 {n:"azithromycin",mg:"500mg",hi:"Infection. Roz 1, 3-5 din pura.",bn:"Infection. Roz 1 ta.",mr:"Sansarg. Roz 1.",dz:{hi:"Bacterial infection",bn:"Bacterial infection",mr:"Jivanu sansarg"}},
 {n:"crocin",mg:"500mg",hi:"Paracetamol brand. Dolo sang double nahi.",bn:"Paracetamol brand. Dolo sathe na.",mr:"Paracetamol brand. Dolo sobat naka.",dz:{hi:"Bukhar",bn:"Jor",mr:"Taap"}},
 {n:"dolo",mg:"650mg",hi:"Paracetamol brand. Crocin sang overdose.",bn:"Paracetamol brand. Overdose hobe.",mr:"Paracetamol brand. Overdose hoil.",dz:{hi:"Bukhar",bn:"Jor",mr:"Taap"}},
 {n:"metformin",mg:"500mg",hi:"Sugar. Khane ke saath + walk.",bn:"Sugar er jonno.",mr:"Sakharsathi.",dz:{hi:"Sugar (Type-2)",bn:"Sugar",mr:"Sakhar"}},
 {n:"amoxicillin",mg:"500mg",hi:"Gale infection. 5 din pura.",bn:"Golar infection.",mr:"Ghasa sansarg.",dz:{hi:"Gale ka infection",bn:"Golar infection",mr:"Ghasa sansarg"}}
];
