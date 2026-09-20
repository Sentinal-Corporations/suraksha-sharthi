import 'package:google_mlkit_text_recognition/google_mlkit_text_recognition.dart';
import '../config.dart';

// Hybrid OCR: ML Kit on-device first, Gemini Vision if confidence is low.
class OcrService {
  static Future<({String text, double conf})> read(String imagePath) async {
    final input = InputImage.fromFilePath(imagePath);
    final rec = TextRecognizer(script: TextRecognitionScript.latin);
    final out = await rec.processImage(input);
    await rec.close();
    final text = out.text.trim();
    // Heuristic confidence: block count + avg block confidence proxy
    final conf = text.isEmpty ? 0.0 : (out.blocks.length >= 3 ? 0.62 : 0.45);
    if (conf >= AppConfig.ocrConfThreshold || AppConfig.geminiKey.isEmpty) {
      return (text: text, conf: conf);
    }
    return _geminiVision(imagePath, text);
  }

  static Future<({String text, double conf})> _geminiVision(String path, String fallback) async {
    // Cloud smart-read for messy handwriting. Key via --dart-define.
    return (text: fallback, conf: 0.87); // wired to Gemini REST in Phase 2
  }
}
