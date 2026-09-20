import 'package:flutter/material.dart';
import 'screens/shell.dart';
import 'data/db.dart';
import 'services/store.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await DrugDb().load(); // 49 medicines, rules, govt datasets
  await Store.init(); // local Sehat File (Hive); Neon/Appwrite sync plugs in here
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Suraksha Parchi',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF0E7C7B)),
        scaffoldBackgroundColor: const Color(0xFFF5EFE3),
        appBarTheme: const AppBarTheme(backgroundColor: Color(0xFF3A3A3C), foregroundColor: Colors.white),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(minimumSize: const Size.fromHeight(50), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14))),
        ),
        cardTheme: CardTheme(shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18))),
      ),
      home: const Shell(),
    );
  }
}
