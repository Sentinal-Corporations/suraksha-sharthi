import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import '../data/db.dart';

class SuvidhaPage extends StatefulWidget {
  const SuvidhaPage({super.key});
  @override
  State<SuvidhaPage> createState() => _SuvidhaState();
}

class _SuvidhaState extends State<SuvidhaPage> {
  String jaq = '', abq = '';
  @override
  Widget build(BuildContext context) {
    final db = DrugDb();
    final ja = db.jaPrices.where((p) => jaq.isEmpty || p['generic'].toString().contains(jaq.toLowerCase())).take(12).toList();
    final pkgs = (db.ayushman['packages'] as List).where(
        (p) => abq.isEmpty || p['name'].toString().toLowerCase().contains(abq.toLowerCase())).take(12).toList();
    return ListView(padding: const EdgeInsets.all(14), children: [
      const Text('Jan Aushadhi — daam compare', style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold)),
      TextField(decoration: const InputDecoration(hintText: 'Dawai likho — e.g. metformin'), onChanged: (v) => setState(() => jaq = v)),
      for (final p in ja)
        ListTile(title: Text('${p['generic']} (${p['pack']})'),
            subtitle: Text('Branded Rs ${p['branded_mrp']} → Kendra Rs ${p['ja_price']}')),
      const Divider(),
      const Text('Ayushman Bharat — Rs 5 lakh cashless', style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold)),
      const Text('Helpline 14555 • beneficiary.nha.gov.in'),
      TextField(decoration: const InputDecoration(hintText: 'Ilaaj: motiyabind, delivery, knee'), onChanged: (v) => setState(() => abq = v)),
      for (final p in pkgs) ListTile(title: Text(p['name'].toString()), subtitle: Text('~Rs ${p['indicative_price']} • ${p['note']}')),
      const Divider(),
      const Text('Helplines — ek tap call', style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold)),
      for (final h in db.helplines)
        ListTile(title: Text('${h['number']} — ${h['name']}'),
            subtitle: Text(h['when_hi'].toString()),
            trailing: IconButton(icon: const Icon(Icons.call), onPressed: () => launchUrl(Uri(scheme: 'tel', path: h['number'].toString().replaceAll('-', ''))))),
    ]);
  }
}
