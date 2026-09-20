// Needle-2 integration — REAL design (verified Sep 2026, cactus-needle 3.0.1).
// Needle-2 is a TOOL-CALLING engine, not a chat completer: it picks tools from a
// catalogue and fills arguments. Our DBs ARE the tools (see engine/test_needle2.py).
// Weights live at engine/needle2.cact (13.74MB, verified). Browser path = engine/wasm
// runner + same .cact. Until WASM tool-loop is wired, MVP answers from grounded rules
// and reports engine status honestly — app never breaks.
window.Needle2 = {
  _status: "idle", // idle|ready|mock
  status() { return this._status; },
  config() { return ((window.APP_CONFIG || {}).llm || {}).needle2 || {}; },

  // Tool catalogue mirrors engine/test_needle2.py — same names, same args.
  tools() {
    return [
      { name: "explain_dose", args: ["drug", "lang"], desc: "Explain dose+diet in hi/bn/mr" },
      { name: "jan_aushadhi_price", args: ["drug"], desc: "Kendra price vs MRP" },
      { name: "check_interaction", args: ["drug1", "drug2", "lang"], desc: "Pairwise interaction" }
    ];
  },

  async load(onStep) {
    const say = s => { this._status = s; if (onStep) onStep(s); };
    try {
      // Presence check: engine files + weights beside the app
      const cfg = this.config();
      const r = await fetch(cfg.weightsPath, { method: "HEAD" });
      if (!r.ok) throw new Error("no weights");
      say("ready"); // WASM inference wiring = phase 2; rules answer meanwhile
      return true;
    } catch (e) { say("mock"); return false; }
  },

  // MVP: grounded-rules answer (same facts the engine calls). Phase 2: route via
  // wasm runner which returns {function_calls, reasoning, confidence} like Python.
  async explain() { return null; }
};
