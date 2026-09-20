import 'package:hive_flutter/hive_flutter.dart';

// Local Sehat File timeline (Hive). Neon/Appwrite sync plugs in here via config keys.
class Store {
  static late Box _box;
  static Future<void> init() async {
    await Hive.initFlutter();
    _box = await Hive.openBox('sehat');
  }

  static List<Map> all() => _box.values.map((e) => Map.from(e)).toList().reversed.toList();
  static Future<void> save(Map m) => _box.add(m);
  static Future<void> clear() => _box.clear();
}
