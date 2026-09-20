import 'package:flutter/material.dart';
import 'shell.dart';

class HomePage extends StatelessWidget {
  final ScanState scan;
  const HomePage(this.scan, {super.key});
  @override
  Widget build(BuildContext context) {
    return ListView(padding: const EdgeInsets.all(14), children: [
      Card(
        color: const Color(0xFF3A3A3C),
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            const Text('Clear Parchi,\nSafe Patient.', style: TextStyle(color: Colors.white, fontSize: 28, fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            const Text('Handwritten parchi ka photo lo — AI mother-tongue me samjhaye.',
                style: TextStyle(color: Color(0xFFD8D2C2))),
            const SizedBox(height: 12),
            ElevatedButton(onPressed: () {}, child: const Text('Enter — Scan Parchi')),
          ]),
        ),
      ),
      const SizedBox(height: 10),
      const Row(children: [
        Expanded(child: _Feat(Icons.camera_alt, 'Scan', 'Parchi + lab photo')),
        Expanded(child: _Feat(Icons.volume_up, 'Samjhao', 'Voice hi/bn/mr')),
        Expanded(child: _Feat(Icons.notifications, 'Yaad', 'Reminders + alerts')),
      ]),
      const Card(
        child: Padding(
          padding: EdgeInsets.all(16),
          child: Text('60% handwritten parchis. 50% wrong dose. 10L+ ASHAs have no tool — till now.'),
        ),
      ),
    ]);
  }
}

class _Feat extends StatelessWidget {
  final IconData icon;
  final String title, sub;
  const _Feat(this.icon, this.title, this.sub);
  @override
  Widget build(BuildContext context) {
    return Card(child: Padding(padding: const EdgeInsets.all(12),
        child: Column(children: [Icon(icon), Text(title, style: const TextStyle(fontWeight: FontWeight.bold)), Text(sub, textAlign: TextAlign.center, style: const TextStyle(fontSize: 12))]));
  }
}
