import 'package:flutter/material.dart';
import 'shell.dart';
import '../engine/rules.dart';
import '../services/tts.dart';
import '../services/store.dart';
import '../l10n/strings.dart';

class ResultPage extends StatefulWidget {
  final ScanState scan;
  const ResultPage(this.scan, {super.key});
  @override
  State<ResultPage> createState() => _ResultState();
}

class _ResultState extends State<ResultPage> {
  final _tts = VoiceService();
  Result? _r;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (widget.scan.found.isNotEmpty) {
      _r = Rules.build(widget.scan.found, widget.scan.name, widget.scan.lang, widget.scan.symptoms);
    }
  }

  @override
  Widget build(BuildContext context) {
    final r = _r;
    if (r == null) return const Center(child: Text('Fill-up se aao — pehle scan karo.'));
    final saving = Rules.jaSaving(r.rows.map((e) => e.generic).toList());
    return ListView(padding: const EdgeInsets.all(14), children: [
      Card(
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(r.intro, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const SizedBox(height: 6),
            Text('Probable: ${r.disease}', style: const TextStyle(fontSize: 16)),
            for (final d in r.rows) Text('• ${d.generic} ${d.mg} — ${d.explain}'),
            const SizedBox(height: 6),
            Text(Strings.diet[widget.scan.lang]!, style: const TextStyle(fontStyle: FontStyle.italic)),
            Text(r.tip),
            Text('AI se bana • ${Strings.disc[widget.scan.lang]!}', style: const TextStyle(fontSize: 12, color: Colors.grey)),
            Row(children: [
              ElevatedButton.icon(onPressed: () => _tts.speak(r.voiceScript, widget.scan.lang),
                  icon: const Icon(Icons.volume_up), label: const Text('Voice me suno')),
              const SizedBox(width: 8),
              ElevatedButton.icon(onPressed: () => Store.save(
                  {'d': DateTime.now().toString(), 'nm': widget.scan.name, 'phone': widget.scan.phone, 'drugs': r.rows.map((e) => e.generic).toList(), 'lang': widget.scan.lang}),
                  icon: const Icon(Icons.save), label: const Text('Save')),
            ]),
          ]),
        ),
      ),
      const Text('Timetable', style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold)),
      for (final t in [
        ['Subah 8AM', r.rows.isNotEmpty ? '${r.rows[0].generic} — 1 goli' : '—'],
        ['Dopahar 2PM', r.rows.length > 1 ? '${r.rows[1].generic} — 1 goli' : 'Aaram + paani'],
        ['Raat 9PM', r.rows.isNotEmpty ? '${r.rows[0].generic} — 1 goli' : '—'],
      ])
        Card(child: ListTile(title: Text(t[0]), subtitle: Text(t[1]), trailing: const Icon(Icons.alarm))),
      for (final a in r.alerts)
        Card(color: a.level == 'danger' ? Colors.red[100] : null,
            child: ListTile(leading: Icon(a.level == 'danger' ? Icons.warning : Icons.check_circle), title: Text(a.text))),
      if (saving != null)
        Card(child: ListTile(leading: const Icon(Icons.currency_rupee),
            title: Text('Jan Aushadhi me ~${saving['pct']}% bachao: Rs ${saving['branded']} → Rs ${saving['ja']}'),
            subtitle: const Text('Kendra: 1800-180-8080'))),
      const Text('Sehat File', style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold)),
      for (final e in Store.all()) Card(child: ListTile(title: Text((e['drugs'] as List).join(', ')), subtitle: Text(e['d'].toString()))),
    ]);
  }
}
