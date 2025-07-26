import 'package:flutter/material.dart';
import 'dart:math' as math;

class HoroscopeScreen extends StatefulWidget {
  @override
  _HoroscopeScreenState createState() => _HoroscopeScreenState();
}

class _HoroscopeScreenState extends State<HoroscopeScreen>
    with TickerProviderStateMixin {
  late AnimationController _animationController;
  late Animation<double> _fadeAnimation;
  String selectedZodiac = 'Aries';
  bool loading = false;
  Map<String, Map<String, dynamic>> horoscopeData = {};

  final List<String> zodiacSigns = [
    'Aries',
    'Taurus',
    'Gemini',
    'Cancer',
    'Leo',
    'Virgo',
    'Libra',
    'Scorpio',
    'Sagittarius',
    'Capricorn',
    'Aquarius',
    'Pisces'
  ];

  @override
  void initState() {
    super.initState();
    _animationController = AnimationController(
      duration: Duration(seconds: 2),
      vsync: this,
    );
    _fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _animationController, curve: Curves.easeIn),
    );
    _animationController.forward();
    _loadHoroscopeData();
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }

  void _loadHoroscopeData() {
    setState(() {
      loading = true;
    });

    // Simulate API call to your Python backend
    Future.delayed(Duration(seconds: 2), () {
      setState(() {
        loading = false;
        horoscopeData = {
          'Aries': {
            'general':
                'Today brings exciting opportunities for leadership and new beginnings.',
            'love':
                'Passion and romance are highlighted. Single Aries may meet someone special.',
            'career':
                'Your innovative ideas will be well-received. Take initiative in projects.',
            'health':
                'Focus on cardiovascular exercise. Energy levels are high.',
            'lucky_color': 'Red',
            'lucky_number': '9',
            'compatibility': 'Leo, Sagittarius'
          },
          'Taurus': {
            'general': 'Stability and determination are your strengths today.',
            'love':
                'Deep emotional connections are possible. Show your caring nature.',
            'career':
                'Financial matters look promising. Your practical approach pays off.',
            'health': 'Grounding exercises like yoga will benefit you.',
            'lucky_color': 'Green',
            'lucky_number': '6',
            'compatibility': 'Virgo, Capricorn'
          },
          // Add more zodiac signs...
        };
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
        child: Stack(
          children: [
            // Animated stars background
            ...List.generate(30, (index) => _buildStar(index)),

            // Main content
            SafeArea(
              child: FadeTransition(
                opacity: _fadeAnimation,
                child: SingleChildScrollView(
                  padding: EdgeInsets.all(24.0),
                  child: Column(
                    children: [
                      // Header
                      Row(
                        children: [
                          IconButton(
                            onPressed: () => Navigator.pop(context),
                            icon: Icon(Icons.arrow_back,
                                color: Color(0xFFFFB74D)),
                          ),
                          Expanded(
                            child: Text(
                              'Daily Horoscope',
                              style: TextStyle(
                                fontSize: 24,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                              ),
                              textAlign: TextAlign.center,
                            ),
                          ),
                          SizedBox(width: 48), // Balance the back button
                        ],
                      ),
                      SizedBox(height: 20),

                      // Zodiac selector
                      Container(
                        padding: EdgeInsets.all(20),
                        decoration: BoxDecoration(
                          color: Color(0xFF1e1e2e).withOpacity(0.8),
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(
                            color: Color(0xFFFFB74D).withOpacity(0.3),
                            width: 1,
                          ),
                        ),
                        child: Column(
                          children: [
                            Text(
                              'Select Your Zodiac Sign',
                              style: TextStyle(
                                fontSize: 18,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                              ),
                            ),
                            SizedBox(height: 16),
                            DropdownButtonFormField<String>(
                              value: selectedZodiac,
                              decoration: InputDecoration(
                                border: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(15),
                                  borderSide:
                                      BorderSide(color: Color(0xFFFFB74D)),
                                ),
                                enabledBorder: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(15),
                                  borderSide:
                                      BorderSide(color: Color(0xFFFFB74D)),
                                ),
                                filled: true,
                                fillColor: Color(0xFF2a2a3a),
                                labelStyle: TextStyle(color: Color(0xFFFFB74D)),
                              ),
                              dropdownColor: Color(0xFF2a2a3a),
                              style: TextStyle(color: Colors.white),
                              items: zodiacSigns.map((String sign) {
                                return DropdownMenuItem<String>(
                                  value: sign,
                                  child: Text(sign),
                                );
                              }).toList(),
                              onChanged: (String? newValue) {
                                setState(() {
                                  selectedZodiac = newValue!;
                                });
                              },
                            ),
                          ],
                        ),
                      ),
                      SizedBox(height: 20),

                      // Horoscope content
                      if (loading)
                        Container(
                          padding: EdgeInsets.all(40),
                          child: Center(
                            child: Column(
                              children: [
                                CircularProgressIndicator(
                                    color: Color(0xFFFFB74D)),
                                SizedBox(height: 16),
                                Text(
                                  'Reading the stars...',
                                  style: TextStyle(color: Color(0xFFFFB74D)),
                                ),
                              ],
                            ),
                          ),
                        )
                      else if (horoscopeData.containsKey(selectedZodiac))
                        _buildHoroscopeContent(selectedZodiac)
                      else
                        Container(
                          padding: EdgeInsets.all(40),
                          child: Center(
                            child: Text(
                              'Select a zodiac sign to see your horoscope',
                              style: TextStyle(color: Color(0xFFFFB74D)),
                            ),
                          ),
                        ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildHoroscopeContent(String zodiac) {
    final data = horoscopeData[zodiac]!;

    return Column(
      children: [
        // General horoscope
        _buildHoroscopeCard(
          'General',
          data['general']!,
          Icons.auto_awesome,
          Color(0xFFFFB74D),
        ),
        SizedBox(height: 16),

        // Love horoscope
        _buildHoroscopeCard(
          'Love & Relationships',
          data['love']!,
          Icons.favorite,
          Color(0xFFE91E63),
        ),
        SizedBox(height: 16),

        // Career horoscope
        _buildHoroscopeCard(
          'Career & Finance',
          data['career']!,
          Icons.work,
          Color(0xFF4CAF50),
        ),
        SizedBox(height: 16),

        // Health horoscope
        _buildHoroscopeCard(
          'Health & Wellness',
          data['health']!,
          Icons.favorite_border,
          Color(0xFF2196F3),
        ),
        SizedBox(height: 16),

        // Lucky elements
        Container(
          padding: EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: Color(0xFF1e1e2e).withOpacity(0.8),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
              color: Color(0xFFFFB74D).withOpacity(0.3),
              width: 1,
            ),
          ),
          child: Column(
            children: [
              Text(
                'Lucky Elements',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              SizedBox(height: 16),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  _buildLuckyElement(
                      'Color', data['lucky_color']!, Icons.palette),
                  _buildLuckyElement(
                      'Number', data['lucky_number']!, Icons.tag),
                  _buildLuckyElement(
                      'Compatibility', data['compatibility']!, Icons.people),
                ],
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildHoroscopeCard(
      String title, String content, IconData icon, Color color) {
    return Container(
      padding: EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Color(0xFF1e1e2e).withOpacity(0.8),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(
          color: color.withOpacity(0.3),
          width: 1,
        ),
        boxShadow: [
          BoxShadow(
            color: color.withOpacity(0.2),
            blurRadius: 10,
            spreadRadius: 2,
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: EdgeInsets.all(8),
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: color.withOpacity(0.2),
                ),
                child: Icon(icon, color: color, size: 20),
              ),
              SizedBox(width: 12),
              Text(
                title,
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
            ],
          ),
          SizedBox(height: 12),
          Text(
            content,
            style: TextStyle(
              fontSize: 14,
              color: Colors.white70,
              height: 1.4,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildLuckyElement(String label, String value, IconData icon) {
    return Column(
      children: [
        Icon(icon, color: Color(0xFFFFB74D), size: 24),
        SizedBox(height: 8),
        Text(
          label,
          style: TextStyle(
            fontSize: 12,
            color: Color(0xFFFFB74D),
          ),
        ),
        SizedBox(height: 4),
        Text(
          value,
          style: TextStyle(
            fontSize: 14,
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
      ],
    );
  }

  Widget _buildStar(int index) {
    final random = math.Random(index);
    return AnimatedBuilder(
      animation: _animationController,
      builder: (context, child) {
        return Positioned(
          left: random.nextDouble() * MediaQuery.of(context).size.width,
          top: random.nextDouble() * MediaQuery.of(context).size.height,
          child: Opacity(
            opacity: (0.5 +
                    0.5 *
                        math.sin(
                            _animationController.value * 2 * math.pi + index))
                .clamp(0.0, 1.0),
            child: Container(
              width: random.nextDouble() * 3 + 1,
              height: random.nextDouble() * 3 + 1,
              decoration: BoxDecoration(
                color: Colors.white,
                shape: BoxShape.circle,
              ),
            ),
          ),
        );
      },
    );
  }
}
