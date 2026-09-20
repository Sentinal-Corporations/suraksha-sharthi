// Public config only — secrets via --dart-define (never committed).
class AppConfig {
  static const appwriteEndpoint = 'https://sgp.cloud.appwrite.io/v1';
  static const appwriteProject = '6aaae7f70031f7c799d7';
  static const neonProject = 'cool-math-10984187';
  static const neonBranch = 'production';
  static const firebaseProject = 'suraksha-parchi';
  static const ocrConfThreshold = 0.70;
  // Passed with: flutter run --dart-define=NEON_URL=... --dart-define=APPWRITE_KEY=...
  static const neonUrl = String.fromEnvironment('NEON_URL', defaultValue: '');
  static const appwriteKey = String.fromEnvironment('APPWRITE_KEY', defaultValue: '');
  static const geminiKey = String.fromEnvironment('GEMINI_KEY', defaultValue: '');
  static const bhashiniKey = String.fromEnvironment('BHASHINI_KEY', defaultValue: '');
}
