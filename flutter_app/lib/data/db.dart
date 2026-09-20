import 'dart:convert';
import 'package:flutter/services.dart';

// In-memory DB loaded from bundled assets. Mirrors Neon tables + web JSONs.
class DrugDb {
  static final DrugDb _i = DrugDb._();
  factory DrugDb() => _i;
  DrugDb._();
  List<Map<String, dynamic>> meds = [];
  List<Map<String, dynamic>> rules = [];
  List<Map<String, dynamic>> jaPrices = [];
  Map<String, dynamic> ayushman = {};
  List<Map<String, dynamic>> helplines = [];
  final Map<String, String> alias = {};

  static String norm(String s) => s.toLowerCase().replaceAll(RegExp(r'[^a-z]'), '');

  Future<void> load() async {
    final m = jsonDecode(await rootBundle.loadString('assets/data/medicines.json'));
    meds = List<Map<String, dynamic>>.from(m['medicines']);
    final r = jsonDecode(await rootBundle.loadString('assets/data/interactions.json'));
    rules = List<Map<String, dynamic>>.from(r['rules']);
    final j = jsonDecode(await rootBundle.loadString('assets/data/jan_aushadhi.json'));
    final jm = (j['prices'] ?? j['meta']) as Map;
    jaPrices = List<Map<String, dynamic>>.from(jm['prices']);
    ayushman = Map<String, dynamic>.from(jsonDecode(await rootBundle.loadString('assets/data/ayushman.json')));
    final h = jsonDecode(await rootBundle.loadString('assets/data/helplines.json'));
    helplines = List<Map<String, dynamic>>.from(h['helplines']);
    for (final d in meds) {
      alias[norm(d['name'])] = d['name'];
      for (final b in (d['brands'] as List)) {
        alias[norm(b.toString())] = d['name'];
      }
    }
  }

  String? resolve(String input) => alias[norm(input)];
  Map<String, dynamic>? get(String generic) {
    for (final d in meds) {
      if (d['name'] == generic) return d;
    }
    return null;
  }
}
