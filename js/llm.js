// Pluggable AI engine — local rules (offline default), Gemini, or any OpenAI-compatible
// endpoint (self-hosted medical model via Ollama/vLLM, or cloud). No keys in frontend:
// custom backends are called through YOUR server proxy (see docs/TRD.md). MVP uses rules.
window.LLM = {
  active() {
    const c = (window.APP_CONFIG && window.APP_CONFIG.llm) || {};
    return c.backend || "rules";
  },
  // Build the grounded prompt (same guardrails as app/rag_prompt.txt)
  prompt(drugs, labs, lang) {
    return `Explain these prescribed drugs in simple Grade-5 ${lang}. ` +
      `Drugs: ${JSON.stringify(drugs)}. Labs: ${JSON.stringify(labs || {})}. ` +
      `Rules: cite only given drugs, never prescribe new dose, add red-flag referral, end with disclaimer. ` +
      `Return JSON: {disease_guess, drugs_explained[], timetable[], diet, red_flags[], next_visit, voice_script}`;
  },
  // Needle-2 on-device tiny model (45M, ≤14MB, ~28MB RAM).
  // Returns rephrased text or null → caller keeps grounded rules. See docs/NEEDLE2.md.
  async viaNeedle2(drugLines, lang, onStep) {
    if (!window.Needle2) return null;
    if (window.Needle2.status() === "idle") await window.Needle2.load(onStep);
    return window.Needle2.explain(drugLines, lang);
  },
  async viaGemini(prompt) {
    const c = window.APP_CONFIG.llm;
    const res = await fetch(c.proxyUrl + "/gemini", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ prompt }) });
    return res.json();
  },
  // Optional: any OpenAI-compatible chat endpoint — point model: "needle-2",
  // "meditron", "llama-3", etc. through your proxy. MVP keeps rules offline.
  async viaCustom(prompt) {
    const c = window.APP_CONFIG.llm;
    const res = await fetch(c.proxyUrl + "/chat", { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ model: c.model, messages: [{ role: "user", content: prompt }] }) });
    return res.json();
  }
};
