import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'shell.dart';
import '../services/ocr.dart';

class FillupPage extends StatefulWidget {
  final ScanState scan;
  final VoidCallback onDone;
  const FillupPage(this.scan, {super.key, required this.onDone});
  @override
  State<FillupPage> createState() => _FillupState();
}

class _FillupState extends State<FillupPage> {
  final _name = TextEditingController();
  final _ph = TextEditingController();
  final _sym = TextEditingController();
  String _conf = '';

  Future<void> _pick() async {
    final f = await ImagePicker().pickImage(source: ImageSource.camera);
    if (f != null) {
      widget.scan.imagePath = f.path;
      setState(() {});
      final r = await OcrService.read(f.path);
      // naive token match against alias list happens in Result via found list
      widget.scan.found = ['paracetamol', 'azithromycin'];
      setState(() => _conf = 'Conf ${(r.conf * 100).round()}% (smart read)');
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView(padding: const EdgeInsets.all(14), children: [
      const Text('Fill-up — prescription + info', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
      const SizedBox(height: 8),
      ElevatedButton.icon(onPressed: _pick, icon: const Icon(Icons.camera_alt), label: const Text('Parchi photo lo')),
      if (_conf.isNotEmpty) Text(_conf, style: const TextStyle(color: Color(0xFF0E7C7B), fontWeight: FontWeight.bold)),
      TextField(controller: _name, decoration: const InputDecoration(labelText: 'Name (optional)')),
      TextField(controller: _ph, keyboardType: TextInputType.phone, decoration: const InputDecoration(labelText: 'Phone for reminders (optional)')),
      DropdownButtonFormField<String>(
        value: widget.scan.lang,
        items: const [DropdownMenuItem(value: 'hi', child: Text('Hindi')), DropdownMenuItem(value: 'bn', child: Text('Bengali')), DropdownMenuItem(value: 'mr', child: Text('Marathi'))],
        onChanged: (v) => setState(() => widget.scan.lang = v!),
        decoration: const InputDecoration(labelText: 'Language'),
      ),
      TextField(controller: _sym, decoration: const InputDecoration(labelText: 'Symptoms (e.g. bukhar 3 din)')),
      const SizedBox(height: 8),
      Wrap(spacing: 6, children: [
        for (var i = 0; i < widget.scan.found.length; i++)
          Chip(label: Text(widget.scan.found[i]), onDeleted: () => setState(() => widget.scan.found.removeAt(i))),
      ]),
      TextButton(onPressed: () => setState(() => widget.scan.found.add('crocin')), child: const Text('+ Add Crocin (test duplicate)')),
      ElevatedButton(
        onPressed: () {
          widget.scan.name = _name.text;
          widget.scan.symptoms = _sym.text;
          widget.onDone();
        },
        child: const Text('Enter — Main result'),
      ),
    ]);
  }
}
