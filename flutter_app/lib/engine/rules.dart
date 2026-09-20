import '../data/db.dart';
import '../l10n/strings.dart';

class Alert {
  final String level; // danger | warn | ok
  final String text;
  Alert(this.level, this.text);
}

class DoseRow {
  final String generic, mg, explain, disease;
  DoseRow(this.generic, this.mg, this.explain, this.disease);
}

class Result {
  final String disease, intro, tip, voiceScript;
  final List<DoseRow> rows;
  final List<Alert> alerts;
  final List<String> redFlags;
  Result(this.disease, this.intro, this.tip, this.voiceScript, this.rows, this.alerts, this.redFlags);
}

// Grounded rules engine: facts only from DrugDb, varied phrasing per visit.
class Rules {
  static int _visits = 0;

  static Map<String, dynamic>? _dupRule(DrugDb db, String g) {
    for (final r in db.rules) {
      final gs = List.from(r['generics']);
      if (gs.length == 2 && gs[0] == g && gs[1] == g) return r;
    }
    return null;
  }

  static Map<String, dynamic>? _pairRule(DrugDb db, String a, String b) {
    for (final r in db.rules) {
      final s = Set.from(r['generics'] as List);
      if (s.contains(a) && s.contains(b)) return r;
    }
    return null;
  }

  static Result build(List<String> inputs, String name, String lang, String symptoms) {
    final db = DrugDb();
    final generics = inputs.map(db.resolve).whereType<String>().toList();
    final rows = generics.map((g) {
      final d = db.get(g)!;
      final dz = (d['dz'] as Map)[lang] ?? d['disease_en'];
      return DoseRow(g, (d['mg'] as List).join('/'), d[lang] ?? d['hi'], dz.toString());
    }).toList();
    final dzAll = rows.map((r) => r.disease).toSet().join(' + ');
    final v = _visits++;
    final intro = (Strings.intros[lang]!)[v % 3];
    final tip = (Strings.tips[lang]!)[(v + 1) % 3];
    final voice = Strings.voice(name.isEmpty ? 'Patient' : name, dzAll, lang);
    final alerts = <Alert>[];
    final counts = <String, int>{};
    for (final g in generics) {
      counts[g] = (counts[g] ?? 0) + 1;
    }
    for (final e in counts.entries) {
      if (e.value > 1) {
        final rule = _dupRule(db, e.key);
        alerts.add(Alert('danger', rule != null ? rule[lang].toString() : 'Same dawai 2 baar — overdose khatra.'));
      }
    }
    final uniq = counts.keys.toList();
    for (var i = 0; i < uniq.length; i++) {
      for (var j = i + 1; j < uniq.length; j++) {
        final rule = _pairRule(db, uniq[i], uniq[j]);
        if (rule != null) alerts.add(Alert(rule['level'].toString(), rule[lang].toString()));
      }
    }
    if (alerts.isEmpty) alerts.add(Alert('ok', 'No interaction. Course pura karo.'));
    final reds = rows.where((r) => (db.get(r.generic)!['red_flag'] == true)).map((r) => r.generic).toList();
    return Result(dzAll.isEmpty ? '—' : dzAll, intro, tip, voice, rows, alerts, reds);
  }

  static Map<String, int>? jaSaving(List<String> generics) {
    final db = DrugDb();
    var b = 0, j = 0, n = 0;
    for (final g in generics.toSet()) {
      for (final p in db.jaPrices.where((p) => DrugDb.norm(p['generic'].toString()) == DrugDb.norm(g))) {
        b += (p['branded_mrp'] as num).toInt();
        j += (p['ja_price'] as num).toInt();
        n++;
      }
    }
    if (n == 0) return null;
    return {'branded': b, 'ja': j, 'pct': ((1 - j / b) * 100).round()};
  }
}
