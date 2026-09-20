import 'package:google_mlkit_text_recognition/google_mlkit_text_recognition.dart';
import 'dart:convert';
import 'dart:io';
import '../config.dart';
import 'cloud.dart';

// Hybrid OCR: ML Kit on-device first (REAL, works with zero API),
// Gemini Vision cloud pass only when confidence is low and key exists.
class OcrService {
  static Future<({String text, double conf})> read(String imagePath) async {
    final input = InputImage.fromFilePath(imagePath);
    final rec = TextRecognizer(script: TextRecognitionScript.latin);
    final out = await rec.processImage(input);
    await rec.close();
    final text = out.text.trim();
    final conf = text.isEmpty ? 0.0 : (out.blocks.length >= 3 ? 0.62 : 0.45);
    if (text.isEmpty || conf < AppConfig.ocrConfThreshold) {
      final smart = await _geminiVision(imagePath, text);
      if (smart != null && smart.isNotEmpty) return (text: smart, conf: 0.87);
    }
    return (text: text, conf: conf);
  }

  static Future<String?> _geminiVision(String path, String hint) async {
    try {
      final bytes = await File(path).readAsBytes();
      return Cloud.geminiVision(base64Encode(bytes), hint);
    } catch (_) {
      return null;
    }
  }
}
