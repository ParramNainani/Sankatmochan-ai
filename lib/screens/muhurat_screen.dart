import 'package:flutter/material.dart';

class MuhuratScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Muhurat'),
        backgroundColor: Color(0xFF1a237e),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              Color(0xFF0a0e21),
              Color(0xFF1a237e),
              Color(0xFF0a0e21),
            ],
          ),
        ),
        child: Center(
          child: Text(
            'Auspicious Timings Coming Soon!',
            style: TextStyle(color: Colors.white, fontSize: 20),
          ),
        ),
      ),
    );
  }
}
