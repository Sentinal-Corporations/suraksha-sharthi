// PUBLIC frontend config only — NO secrets here. Secrets live in server .env (gitignored).
window.APP_CONFIG = {
  appwrite: { endpoint: "https://sgp.cloud.appwrite.io/v1", projectId: "6aaae7f70031f7c799d7" },
  neon: { projectId: "cool-math-10984187", branch: "production" },
  firebase: { projectName: "Suraksha-parchi", projectId: "suraksha-parchi", projectNumber: "399451441985" },
  ocr: { primary: "mlkit-ondevice", fallback: "gemini-vision", confThreshold: 0.70 },
  voice: { provider: "bhashini", fallback: "browser-tts", langs: ["hi", "bn", "mr"] },
  // AI engine: "rules" (offline default) | "needle2" (14MB on-device tool-caller,
  //   verified: engine/needle2.cact + engine/wasm runner) | "gemini" | "custom".
  // "custom" = any OpenAI-compatible model via YOUR server proxy.
  // proxyUrl holds NO keys in frontend — keys live in server .env only.
  llm: { backend: "rules", model: "needle-2",
    needle2: { enabled: true, weightsPath: "../engine/needle2.cact",
      wasmEngine: "../engine/wasm/wasm/needle.wasm",
      tools: ["explain_dose", "jan_aushadhi_price", "check_interaction"] },
    proxyUrl: "" }
};
