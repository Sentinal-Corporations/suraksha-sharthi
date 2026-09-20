// Needle-2 on-device status. Full WASM/tool-loop wiring is Phase 2;
// engine/needle2.cact verified via Python (see engine/test_needle2.py).
// Tools catalogue mirrors it: explain_dose, jan_aushadhi_price, check_interaction.
enum NeedleStatus { starting, ready, builtin }

class Needle2 {
  static NeedleStatus status = NeedleStatus.starting;

  // Auto-called on app open. Real load binds the .cact via platform channel later.
  static Future<void> autoStart(void Function() onChange) async {
    await Future.delayed(const Duration(seconds: 1));
    status = NeedleStatus.builtin; // -> ready once WASM runner is bound
    onChange();
  }

  static String label() => switch (status) {
        NeedleStatus.ready => 'Needle-2 AI • auto-loaded',
        NeedleStatus.starting => 'AI starting…',
        NeedleStatus.builtin => 'Built-in AI • auto',
      };
}
