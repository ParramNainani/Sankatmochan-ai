import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
import 'screens/login_screen.dart';
import 'screens/register_screen.dart';
import 'screens/home_screen.dart';
import 'screens/horoscope_screen.dart';
import 'screens/birth_chart_screen.dart';
import 'screens/planetary_positions_screen.dart';
import 'screens/compatibility_screen.dart';
import 'screens/muhurat_screen.dart';
import 'screens/gemstones_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sankatmochan AI',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        primaryColor: Color(0xFF1a237e), // Deep indigo
        scaffoldBackgroundColor: Color(0xFF0a0e21), // Dark cosmic background
        appBarTheme: AppBarTheme(
          backgroundColor: Color(0xFF1a237e),
          elevation: 0,
          centerTitle: true,
          titleTextStyle: TextStyle(
            color: Colors.white,
            fontSize: 20,
            fontWeight: FontWeight.bold,
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            backgroundColor: Color(0xFF3949ab),
            foregroundColor: Colors.white,
            padding: EdgeInsets.symmetric(horizontal: 32, vertical: 12),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(25),
            ),
          ),
        ),
        textButtonTheme: TextButtonThemeData(
          style: TextButton.styleFrom(
            foregroundColor: Color(0xFF7986cb),
          ),
        ),
        inputDecorationTheme: InputDecorationTheme(
          filled: true,
          fillColor: Color(0xFF1e1e2e),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(15),
            borderSide: BorderSide(color: Color(0xFF3949ab)),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(15),
            borderSide: BorderSide(color: Color(0xFF3949ab)),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(15),
            borderSide: BorderSide(color: Color(0xFF7986cb), width: 2),
          ),
          labelStyle: TextStyle(color: Color(0xFF7986cb)),
          hintStyle: TextStyle(color: Color(0xFF9fa8da)),
        ),
        textTheme: TextTheme(
          bodyLarge: TextStyle(color: Colors.white),
          bodyMedium: TextStyle(color: Colors.white70),
        ),
      ),
      initialRoute: '/login',
      routes: {
        '/login': (context) => LoginScreen(),
        '/register': (context) => RegisterScreen(),
        '/home': (context) => HomeScreen(),
        '/horoscope': (context) => HoroscopeScreen(),
        '/birth-chart': (context) => BirthChartScreen(),
        '/planetary-positions': (context) => PlanetaryPositionsScreen(),
        '/compatibility': (context) => CompatibilityScreen(),
        '/muhurat': (context) => MuhuratScreen(),
        '/gemstones': (context) => GemstonesScreen(),
      },
    );
  }
}
