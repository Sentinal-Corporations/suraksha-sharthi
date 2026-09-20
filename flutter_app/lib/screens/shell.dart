import 'package:flutter/material.dart';
import 'home.dart';
import 'fillup.dart';
import 'result.dart';
import 'suvidha.dart';
import '../services/needle2.dart';

class Shell extends StatefulWidget {
  const Shell({super.key});
  @override
  State<Shell> createState() => _ShellState();
}

class ScanState extends ChangeNotifier {
  String name = '', phone = '', lang = 'hi', symptoms = '', imagePath = '';
  List<String> found = [];
  void reset() {
    found = [];
    notifyListeners();
  }
}

class _ShellState extends State<Shell> {
  int idx = 0;
  final scan = ScanState();
  @override
  void initState() {
    super.initState();
    Needle2.autoStart(() => setState(() {}));
  }

  @override
  Widget build(BuildContext context) {
    final pages = [HomePage(scan), FillupPage(scan, onDone: () => setState(() => idx = 2)), ResultPage(scan), const SuvidhaPage()];
    return Scaffold(
      appBar: AppBar(
        title: const Text('Suraksha Parchi'),
        actions: [
          Chip(label: Text(Needle2.label(), style: const TextStyle(fontSize: 11))),
          const SizedBox(width: 8),
        ],
      ),
      drawer: Drawer(
        child: ListView(padding: EdgeInsets.zero, children: [
          const DrawerHeader(
            decoration: BoxDecoration(color: Color(0xFF3A3A3C)),
            child: Text('Suraksha Parchi\nPhoto lo, Bhasha me samjho',
                style: TextStyle(color: Colors.white, fontSize: 18)),
          ),
          for (final t in const [
            ['Home', 0], ['New Scan', 1], ['My Result', 2], ['Jan Aushadhi Daam', 3], ['Ayushman Bharat', 3]
          ])
            ListTile(
                title: Text(t[0] as String),
                onTap: () {
                  Navigator.pop(context);
                  setState(() => idx = t[1] as int);
                }),
          const Divider(),
          for (final t in const ['Privacy Policy', 'User Agreement', 'Support / Help', 'About CHANAKYA', 'How it works'])
            ListTile(title: Text(t), onTap: () => _info(context, t)),
        ]),
      ),
      body: pages[idx],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: idx,
        onTap: (i) => setState(() => idx = i),
        type: BottomNavigationBarType.fixed,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.document_scanner), label: 'Scan'),
          BottomNavigationBarItem(icon: Icon(Icons.bar_chart), label: 'Result'),
          BottomNavigationBarItem(icon: Icon(Icons.currency_rupee), label: 'Suvidha'),
        ],
      ),
    );
  }

  void _info(BuildContext c, String t) {
    Navigator.pop(c);
    const bodies = {
      'Privacy Policy': 'No Aadhaar needed. Photos stay private. View/delete anytime. Kids with parent consent.',
      'User Agreement': 'Explains YOUR prescription, never prescribes new. Red flag means visit PHC.',
      'Support / Help': 'Mail ayush4ru@gmail.com. Saaf photo lo. RED alert aaye to doctor/ASHA se poochho.',
      'About CHANAKYA': 'Ayush Pandey (Leader) + Kaushal Rawat (CMO) +2. Aaj parchi, kal Sehat File.',
      'How it works': 'Scan, smart read, verified database match, mother-tongue voice, reminders, alerts. Works offline.',
    };
    showDialog(context: c, builder: (_) => AlertDialog(title: Text(t), content: Text(bodies[t]!), actions: [
      TextButton(onPressed: () => Navigator.pop(c), child: const Text('Close'))
    ]));
  }
}
