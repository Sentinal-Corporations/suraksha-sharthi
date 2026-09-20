import 'package:flutter_tts/flutter_tts.dart';
import '../l10n/strings.dart';

// Mother-tongue voice with offline fallback handled by the OS engine.
class VoiceService {
  final FlutterTts _tts = FlutterTts();
  Future<void> speak(String text, String lang) async {
    await _tts.setLanguage(Strings.ttsLocale[lang] ?? 'hi-IN');
    await _tts.setSpeechRate(0.45);
    await _tts.speak(text);
  }

  Future<void> stop() => _tts.stop();
}
