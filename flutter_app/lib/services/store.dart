import 'dart:convert';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:postgres/postgres.dart';
import 'package:appwrite/appwrite.dart';
import 'package:appwrite/models.dart' as models;
import '../config.dart';

// Sehat File: Hive local always; Neon Postgres + Appwrite sync when configured.
class Store {
  static late Box _box;
  static Client? _aw;
  static Storage? _storage;

  static Future<void> init() async {
    await Hive.initFlutter();
    _box = await Hive.openBox('sehat');
    if (AppConfig.appwriteKey.isNotEmpty) {
      _aw = Client()
          .setEndpoint(AppConfig.appwriteEndpoint)
          .setProject(AppConfig.appwriteProject)
          .setKey(AppConfig.appwriteKey)
          .setSelfSigned(status: true);
      _storage = Storage(_aw!);
    }
  }

  static List<Map> all() => _box.values.map((e) => Map.from(e)).toList().reversed.toList();
  static Future<void> save(Map m) async {
    await _box.add(m);
    await syncNeon(m); // no-op without NEON_URL
  }

  static Future<void> clear() => _box.clear();

  static Future<void> syncNeon(Map m) async {
    if (AppConfig.neonUrl.isEmpty) return;
    final conn = await Connection.open(Endpoint.parse(AppConfig.neonUrl));
    await conn.execute(
      Sql.named('INSERT INTO sehat_file(user_phone,scan_type,parsed_json,lang) VALUES(@p,@s,@j::jsonb,@l)'),
      parameters: {
        'p': (m['phone'] ?? '').toString(),
        's': 'parchi',
        'j': jsonEncode({'drugs': m['drugs']}),
        'l': (m['lang'] ?? 'hi').toString(),
      },
    );
    await conn.close();
  }

  static Future<String?> uploadPhoto(String path, String name) async {
    if (_storage == null) return null;
    try {
      final f = await _storage!.createFile(
          bucketId: 'parchis', fileId: ID.unique(), file: InputFile.fromPath(path: path, filename: name));
      return (f as models.File).$id;
    } catch (_) {
      return null;
    }
  }
}
