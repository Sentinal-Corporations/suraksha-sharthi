import 'dart:convert';
import 'package:http/http.dart' as http;
import '../config.dart';

// Cloud APIs. Every method returns null/false when its key is missing,
// and callers fall back to on-device behavior. Keys via --dart-define only.
class Cloud {
  // Gemini 2.5 Flash grounded explain. Guardrails live in the prompt.
  static Future<String?> geminiExplain(String prompt) async {
    if (AppConfig.geminiKey.isEmpty) return null;
    final uri = Uri.parse(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${AppConfig.geminiKey}');
    final r = await http.post(uri,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'contents': [
            {'parts': [{'text': prompt}]}
          ],
          'generationConfig': {'temperature': 0.2, 'maxOutputTokens': 256}
        }));
    if (r.statusCode != 200) return null;
    try {
      final c = (jsonDecode(r.body)['candidates'] as List)[0];
      return (((c['content']['parts'] as List)[0])['text'] as String);
    } catch (_) {
      return null;
    }
  }

  // Gemini Vision smart-read for messy handwriting. Returns text or null.
  static Future<String?> geminiVision(String base64Jpg, String hint) async {
    if (AppConfig.geminiKey.isEmpty) return null;
    final uri = Uri.parse(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${AppConfig.geminiKey}');
    final r = await http.post(uri,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'contents': [
            {
              'parts': [
                {'text': 'Read this Indian doctor prescription. List drug names with doses, one per line. Context guess: $hint'},
                {'inline_data': {'mime_type': 'image/jpeg', 'data': base64Jpg}}
              ]
            }
          ],
          'generationConfig': {'temperature': 0.1, 'maxOutputTokens': 256}
        }));
    if (r.statusCode != 200) return null;
    try {
      final c = (jsonDecode(r.body)['candidates'] as List)[0];
      return (((c['content']['parts'] as List)[0])['text'] as String);
    } catch (_) {
      return null;
    }
  }

  // Bhashini ULCA TTS. Needs pipeline IDs via --dart-define (see README).
  // Returns raw wav bytes, or null to fall back to device TTS.
  static Future<List<int>?> bhashiniTts(String text, String lang) async {
    if (AppConfig.bhashiniKey.isEmpty) return null;
    return null; // Phase 2: pipeline search + compute call (endpoint IDs in README)
  }
}
