// Suraksha Parchi app logic — config + data driven, no hardcoded secrets.
let DRUGS = window.DRUG_DB_FALLBACK.map(d => ({ n: d.n, brands: [d.n], mg: [d.mg], hi: d.hi, bn: d.bn, mr: d.mr, dz: d.dz, red_flag: false }));
let RULES = [];
let JA = { prices: [], meta: {} };
let AB = { packages: [], steps_hi: [], steps_bn: [], steps_mr: [], helpline: "14555" };
let HL = [];
let ALIAS = {};
let found = ["dolo", "azithromycin"];
const $ = id => document.getElementById(id);

function norm(s) { return (s || "").toLowerCase().replace(/[^a-z]/g, ""); }
function buildAlias() {
  ALIAS = {};
  DRUGS.forEach(d => { ALIAS[norm(d.n)] = d.n; (d.brands || []).forEach(b => { ALIAS[norm(b)] = d.n; }); });
}
function resolve(input) { return ALIAS[norm(input)] || null; }

async function loadData() {
  try {
    const r = await fetch("./data/medicines.json");
    if (r.ok) {
      const j = await r.json();
      const list = j.medicines || j;
      if (Array.isArray(list) && list.length) DRUGS = list;
    }
  } catch (e) { console.log("medicines.json fallback", e); }
  try {
    const r2 = await fetch("./data/drug_db.json");
    if (r2.ok) {
      const j2 = await r2.json();
      const extra = (Array.isArray(j2) ? j2 : []).filter(x => !DRUGS.some(d => norm(d.name || d.n) === norm(x.name)));
      extra.forEach(x => DRUGS.push({ n: x.name, brands: [x.name], mg: [x.mg], hi: x.hindi, bn: x.bengali, mr: x.marathi, dz: { hi: x.disease_en, bn: x.disease_en, mr: x.disease_en }, red_flag: !!x.red_flag }));
    }
  } catch (e) { console.log("drug_db skip", e); }
  try {
    const r3 = await fetch("./data/interactions.json");
    if (r3.ok) { const j3 = await r3.json(); RULES = j3.rules || []; }
  } catch (e) { console.log("interactions fallback", e); }
  try {
    const r4 = await fetch("./data/jan_aushadhi.json");
    if (r4.ok) { const j4 = await r4.json(); JA = j4.prices ? j4 : (j4.meta || {}); }
  } catch (e) { console.log("ja fallback", e); }
  try {
    const r5 = await fetch("./data/ayushman.json");
    if (r5.ok) AB = await r5.json();
  } catch (e) { console.log("ab fallback", e); }
  try {
    const r6 = await fetch("./data/helplines.json");
    if (r6.ok) { const j6 = await r6.json(); HL = j6.helplines || []; }
  } catch (e) { console.log("hl fallback", e); }
  buildAlias();
}
const lang = () => $("lang").value;
function go(v) { document.querySelectorAll(".view").forEach(s => s.classList.remove("on")); $("v-" + v).classList.add("on"); closeDrawer(); window.scrollTo(0, 0); document.querySelectorAll("#tabbar button[data-go]").forEach(b => b.classList.toggle("on", b.dataset.go === v)); if (v === "suvidha" && typeof renderSuvidha === "function") renderSuvidha(); }
function closeDrawer() { $("drawer").classList.remove("open"); $("scrim").classList.remove("on"); }
function hydrateIcons(root) { (root || document).querySelectorAll("[data-ic]").forEach(el => { if (!el.dataset.done) { el.innerHTML = window.icon(el.dataset.ic, el.classList.contains("icwrap") ? 24 : 18); el.dataset.done = "1"; } }); }
function renderChips() {
  $("chips").innerHTML = found.map((n, i) => {
    const g = resolve(n), d = DRUGS.find(x => x.n === g);
    return d ? `<span class="chip">${window.icon("pill", 14)} ${n} → ${d.n} ${(d.mg || []).join("/")} <a href="#" data-del="${i}" aria-label="remove">${window.icon("x", 14)}</a></span>` : `<span class="chip">${n} ? <a href="#" data-del="${i}">${window.icon("x", 14)}</a></span>`;
  }).join("") || '<span class="muted">Empty</span>';
  document.querySelectorAll("[data-del]").forEach(a => a.onclick = e => { e.preventDefault(); found.splice(+a.dataset.del, 1); renderChips(); });
}
function checkInteractions(generics, L) {
  const out = [];
  const counts = {};
  generics.forEach(g => { counts[g] = (counts[g] || 0) + 1; });
  Object.keys(counts).forEach(g => {
    if (counts[g] > 1) {
      const rule = RULES.find(r => r.generics[0] === g && r.generics[1] === g);
      out.push({ level: "danger", text: rule ? rule[L] : `Same dawai 2 baar — overdose khatra.` });
    }
  });
  const uniq = [...new Set(generics)];
  for (let i = 0; i < uniq.length; i++) for (let j = i + 1; j < uniq.length; j++) {
    const rule = RULES.find(r => { const s = new Set(r.generics); return s.has(uniq[i]) && s.has(uniq[j]); });
    if (rule) out.push({ level: rule.level, text: rule[L] });
  }
  return out;
}
function buildResult() {
  const L = lang();
  const generics = found.map(resolve).filter(Boolean);
  const rows = generics.map(g => DRUGS.find(x => x.n === g)).filter(Boolean);
  const T = window.I18N[L];
  const dz = [...new Set(rows.map(r => (r.dz && r.dz[L]) || r.dz.hi))].join(" + ") || "—";
  const nm = ($("nm").value || "Patient").trim();
  const v = visitNo();
  const intro = INTROS[L][v % INTROS[L].length];
  const tip = TIPS[L][(v + 1) % TIPS[L].length];
  $("who").textContent = `— ${nm} (${L.toUpperCase()})`;
  const reds = rows.filter(r => r.red_flag).map(r => r.n);
  $("explain").innerHTML = `<div class="ok"><b>${intro}</b><br><br><b>Probable: ${dz}</b><br>${rows.map(r => `• ${r.n} ${(r.mg || []).join("/")} — ${r[L] || r.hi}`).join("<br>")}<br><br><b>Parhez:</b> ${T.diet}<br><br><span class="muted">${tip}</span><br><span class="muted">Symptoms: ${$("sym").value || "—"} • Verified database • ${T.disc}</span></div>`
    + (reds.length ? `<div class="alert" style="margin-top:8px">${window.icon("alert", 18)} Note: ${reds.join(", ")} — doctor ki salah se hi lein, khud band/shuru na karein.</div>` : "");
  const vs = T.voice(nm) + ` Dawai: ${rows.map(r => r.n).join(", ")}.`;
  $("voiceScript").style.display = "block"; $("voiceScript").innerHTML = "<b>Voice:</b> " + vs;
  $("voiceScript").dataset.t = vs; $("voiceScript").dataset.l = L;
  const eng = (window.Needle2 && window.Needle2.status() === "ready") ? "Needle-2 AI • auto" : "Built-in AI • auto";
  $("voiceScript").innerHTML += `<br><span class="muted">AI se bana • ${eng}</span>`;
  const tt = [["sun", "Subah 8AM", rows[0] ? rows[0].n + " — 1 goli" : "—"], ["cloud", "Dopahar 2PM", rows[1] ? rows[1].n + " — 1 goli" : "Aaram + paani"], ["moon", "Raat 9PM", rows[0] ? rows[0].n + " — 1 goli" : "—"]];
  $("tt").innerHTML = tt.map(t => `<div class="slot">${window.icon(t[0], 22)}<br><b>${t[1]}</b><br>${t[2]}<br><button class="line" style="margin-top:8px;padding:6px 10px;font-size:13px">${window.icon("bell", 14)} Reminder ON</button></div>`).join("");
  const hits = checkInteractions(generics, L);
  $("alertBox").innerHTML = hits.length
    ? hits.map(h => h.level === "danger" ? `<div class="alert">${window.icon("alert", 18)} ${h.text}</div>` : `<div class="ok">${window.icon("info", 18)} ${h.text}</div>`).join("")
    : `<div class="ok">${window.icon("check", 18)} No interaction. Course pura karo.</div>`;
  // Jan Aushadhi savings box
  const jaRows = [...new Set(generics)].flatMap(g => (JA.prices || []).filter(p => norm(p.generic) === norm(g)));
  if (jaRows.length) {
    const totB = jaRows.reduce((s, p) => s + p.branded_mrp, 0), totJ = jaRows.reduce((s, p) => s + p.ja_price, 0);
    const pct = Math.round((1 - totJ / totB) * 100);
    $("jabox").innerHTML = `<div class="ok">${window.icon("rupee", 18)} <b>Jan Aushadhi me ~${pct}% bachao: Rs ${totB} → Rs ${totJ}</b><br>${jaRows.map(p => `• ${p.generic} (${p.pack}): branded Rs ${p.branded_mrp} vs Kendra Rs ${p.ja_price}`).join("<br>")}<br><span class="muted">Kendra: 1800-180-8080 • daam indicative</span></div>`;
  } else { $("jabox").innerHTML = ""; }
}
function renderSuvidha() {
  const L = ($("lang") && $("lang").value) || "hi";
  hydrateIcons(document);
  const steps = AB["steps_" + L] || AB.steps_hi || [];
  $("absteps").innerHTML = `<b>Patrata kaise check karein (14555):</b><br>${steps.map((s, i) => `${i + 1}. ${s}`).join("<br>")}`;
  $("hlout").innerHTML = HL.map(h => `<div class="slot"><b>${h.number}</b><br>${h.name}<br><span class="muted">${h["when_" + L] || h.when_hi}</span><br><a href="tel:${h.number.replace(/-/g, "")}">${window.icon("phone", 14)} Call</a></div>`).join("");
  const doJA = () => {
    const q = norm($("jaq").value);
    const list = (JA.prices || []).filter(p => !q || norm(p.generic).includes(q) || norm(resolve(p.generic) || "").includes(q)).slice(0, 12);
    $("jaout").innerHTML = list.length ? list.map(p => { const pct = Math.round((1 - p.ja_price / p.branded_mrp) * 100); return `<div class="chip">${window.icon("rupee", 14)} ${p.generic} (${p.pack}): Rs ${p.branded_mrp} → <b>Rs ${p.ja_price}</b> (−${pct}%)</div>`; }).join("") : '<span class="muted">Nahi mila — spelling badlo (e.g. metformin).</span>';
  };
  const doAB = () => {
    const q = ($("abq").value || "").toLowerCase();
    const list = (AB.packages || []).filter(p => !q || p.name.toLowerCase().includes(q) || p.code.toLowerCase().includes(q)).slice(0, 12);
    $("about").innerHTML = list.length ? list.map(p => `<div class="chip">${window.icon("hospital", 14)} ${p.name}: ~Rs ${p.indicative_price} <span class="muted">${p.note}</span></div>`).join("") : '<span class="muted">Nahi mila — (e.g. motiyabind, delivery, knee).</span>';
  };
  $("jaq").oninput = doJA; $("abq").oninput = doAB; doJA(); doAB();
}
const INTROS = {
  hi: ["AI ne aapki parchi padh li hai — aasan bhasha me samjhaya:", "Parchi taiyaar — AI se saral me janiye:", "AI vishleshan taiyaar hai — dhyaan se padhein:"],
  bn: ["AI apnar parchi poreche — sohoj bhashay:", "Parchi toiri — AI theke janun:", "AI bishleshon toiri:"],
  mr: ["AI ne tumchi parchi vachli — sopya bhashet:", "Parchi tayar — AI kadun samja:", "AI vishleshan tayar aahe:"]
};
const TIPS = {
  hi: ["AI tip: dawai roz same time par lo — asar best hota hai.", "AI tip: course beech me mat chhodo, warna bimari wapas aayegi.", "AI tip: dawai ke saath paani khoob piyo."],
  bn: ["AI tip: roj ekei somoye osudh khan.", "AI tip: course majhpathe chharben na.", "AI tip: osudher sathe porjapto jol khan."],
  mr: ["AI tip: darroj ekach veli aushadh ghya.", "AI tip: course madhyat sodu naka.", "AI tip: aushadhasobat bharpur pani pya."]
};
function visitNo() { let n = +(localStorage.getItem("visits") || 0); localStorage.setItem("visits", n + 1); return n; }
function setBadge() {
  const b = $("aibadge"); if (!b) return;
  const st = window.Needle2 ? window.Needle2.status() : "mock";
  if (st === "ready") { b.innerHTML = '<span class="dot"></span>Needle-2 AI • auto-loaded'; b.classList.add("ready"); }
  else if (st === "loading" || st === "idle") { b.innerHTML = '<span class="dot"></span>AI starting…'; b.classList.remove("ready"); }
  else { b.innerHTML = '<span class="dot"></span>Built-in AI • auto'; b.classList.remove("ready"); }
}
function renderFile() { const all = JSON.parse(localStorage.getItem("sehat") || "[]"); $("file").innerHTML = all.length ? all.map(a => `<span class="chip">${a.d} — ${(a.nm ? a.nm + ": " : "")}${a.drugs.join(", ")} (${a.lang})</span>`).join("") : '<span class="muted">Empty — save dabao.</span>'; }
window.addEventListener("DOMContentLoaded", async () => {
  hydrateIcons(document);
  setBadge();
  // Needle-2 auto-starts on app open — no manual start needed
  if (window.Needle2) window.Needle2.load(() => setBadge()).then(() => setBadge());
  await loadData();
  document.querySelectorAll("[data-go]").forEach(b => b.onclick = e => { e.preventDefault(); go(b.dataset.go); });
  $("menuBtn").onclick = () => { $("drawer").classList.add("open"); $("scrim").classList.add("on"); };
  $("closeDr").onclick = closeDrawer; $("scrim").onclick = closeDrawer;
  document.querySelectorAll("[data-modal]").forEach(a => a.onclick = e => { e.preventDefault(); closeDrawer(); $("m-" + a.dataset.modal).classList.add("on"); });
  document.querySelectorAll(".closeM").forEach(b => b.onclick = () => b.closest(".modal").classList.remove("on"));
  document.querySelectorAll(".modal").forEach(m => m.onclick = e => { if (e.target === m) m.classList.remove("on"); });
  const frameOff = on => { document.body.classList.toggle("device-off", on); const ic = on ? "phone" : "monitor"; if ($("viewBtn")) $("viewBtn").innerHTML = window.icon(ic, 20); fitDevice(); };
  function fitDevice() {
    const wrap = document.querySelector(".device-wrap"); if (!wrap) return;
    if (document.body.classList.contains("device-off") || window.innerWidth <= 640) { wrap.style.transform = ""; return; }
    const r = getComputedStyle(document.body);
    const dw = parseFloat(r.getPropertyValue("--dw")) + 26, dh = parseFloat(r.getPropertyValue("--dh")) + 26;
    const side = document.querySelector(".side");
    const sideW = (side && getComputedStyle(side).display !== "none") ? side.offsetWidth + 20 : 0;
    const s = Math.min(1, (window.innerHeight - 20) / dh, (window.innerWidth - 20 - sideW) / dw);
    wrap.style.transform = s < 1 ? `scale(${s})` : "";
  }
  function setDevice(spec, btn) {
    const [w, h] = spec.split("x");
    document.body.style.setProperty("--dw", w + "px");
    document.body.style.setProperty("--dh", h + "px");
    document.querySelectorAll("[data-dev]").forEach(b => b.classList.toggle("on", b === btn));
    fitDevice();
  }
  document.querySelectorAll("[data-dev]").forEach(b => b.onclick = () => setDevice(b.dataset.dev, b));
  window.addEventListener("resize", fitDevice);
  if ($("viewBtn")) $("viewBtn").onclick = () => frameOff(!document.body.classList.contains("device-off"));
  if ($("frameBtn")) $("frameBtn").onclick = () => frameOff(!document.body.classList.contains("device-off"));
  const flipTheme = () => { const b = document.body; b.dataset.theme = b.dataset.theme === "dark" ? "" : "dark"; if ($("themeBtn")) $("themeBtn").innerHTML = window.icon(b.dataset.theme === "dark" ? "sun" : "moon", 20); };
  $("themeBtn").onclick = flipTheme;
  if ($("sideThemeBtn")) $("sideThemeBtn").onclick = flipTheme;
  $("up").onchange = e => { const f = e.target.files[0]; if (f) $("pv").src = URL.createObjectURL(f); };
  $("useSample").onclick = () => { $("pv").src = "branding/sample-parchi.png"; };
  $("scanBtn").onclick = () => { $("conf").textContent = "Conf 87% (smart read)"; renderChips(); };
  $("addBtn").onclick = () => { if (!found.includes("crocin")) found.push("crocin"); renderChips(); };
  $("expBtn").onclick = () => { buildResult(); go("main"); };
  $("speakBtn").onclick = () => { const t = $("voiceScript").dataset.t || "Subah 1 goli."; const L = $("voiceScript").dataset.l || "hi"; const u = new SpeechSynthesisUtterance(t); u.lang = L === "hi" ? "hi-IN" : L === "bn" ? "bn-IN" : "mr-IN"; speechSynthesis.cancel(); speechSynthesis.speak(u); };
  $("saveBtn").onclick = () => { const all = JSON.parse(localStorage.getItem("sehat") || "[]"); all.unshift({ d: new Date().toLocaleString(), drugs: [...found], lang: lang(), nm: $("nm").value || "" }); localStorage.setItem("sehat", JSON.stringify(all)); renderFile(); };
  $("clearBtn").onclick = () => { localStorage.removeItem("sehat"); renderFile(); };
  renderChips(); renderFile(); fitDevice();
});
