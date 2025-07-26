import 'package:flutter/material.dart';
import 'dart:math' as math;

class BirthChartScreen extends StatefulWidget {
  @override
  _BirthChartScreenState createState() => _BirthChartScreenState();
}

class _BirthChartScreenState extends State<BirthChartScreen>
    with TickerProviderStateMixin {
  late AnimationController _animationController;
  late Animation<double> _fadeAnimation;

  final TextEditingController nameController = TextEditingController();
  DateTime selectedDate = DateTime.now();
  TimeOfDay selectedTime = TimeOfDay.now();
  String selectedLocation = 'Mumbai, India';
  bool loading = false;
  Map<String, dynamic>? birthChartData;

  final List<String> locations = [
    'Mumbai, India',
    'Delhi, India',
    'Bangalore, India',
    'Chennai, India',
    'Kolkata, India',
    'New York, USA',
    'London, UK',
    'Tokyo, Japan',
    'Sydney, Australia',
    'Toronto, Canada'
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
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }

  Future<void> _selectDate() async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: selectedDate,
      firstDate: DateTime(1900),
      lastDate: DateTime.now(),
      builder: (context, child) {
        return Theme(
          data: Theme.of(context).copyWith(
            colorScheme: ColorScheme.dark(
              primary: Color(0xFFFFB74D),
              onPrimary: Colors.black,
              surface: Color(0xFF2a2a3a),
              onSurface: Colors.white,
            ),
          ),
          child: child!,
        );
      },
    );
    if (picked != null && picked != selectedDate) {
      setState(() {
        selectedDate = picked;
      });
    }
  }

  Future<void> _selectTime() async {
    final TimeOfDay? picked = await showTimePicker(
      context: context,
      initialTime: selectedTime,
      builder: (context, child) {
        return Theme(
          data: Theme.of(context).copyWith(
            colorScheme: ColorScheme.dark(
              primary: Color(0xFFFFB74D),
              onPrimary: Colors.black,
              surface: Color(0xFF2a2a3a),
              onSurface: Colors.white,
            ),
          ),
          child: child!,
        );
      },
    );
    if (picked != null && picked != selectedTime) {
      setState(() {
        selectedTime = picked;
      });
    }
  }

  void _generateBirthChart() {
    if (nameController.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Please enter your name'),
          backgroundColor: Colors.red,
        ),
      );
      return;
    }

    setState(() {
      loading = true;
    });

    // Simulate API call to your Python backend
    Future.delayed(Duration(seconds: 3), () {
      setState(() {
        loading = false;
        birthChartData = {
          'name': nameController.text,
          'birth_date': selectedDate.toString(),
          'birth_time': selectedTime.format(context),
          'location': selectedLocation,
          'sun_sign': 'Aries',
          'moon_sign': 'Cancer',
          'ascendant': 'Libra',
          'planets': {
            'Sun': {
              'sign': 'Aries',
              'house': 1,
              'degree': '15° 30\'',
              'status': 'Strong'
            },
            'Moon': {
              'sign': 'Cancer',
              'house': 4,
              'degree': '8° 45\'',
              'status': 'Exalted'
            },
            'Mercury': {
              'sign': 'Pisces',
              'house': 12,
              'degree': '22° 10\'',
              'status': 'Debilitated'
            },
            'Venus': {
              'sign': 'Taurus',
              'house': 2,
              'degree': '5° 20\'',
              'status': 'Strong'
            },
            'Mars': {
              'sign': 'Scorpio',
              'house': 8,
              'degree': '18° 55\'',
              'status': 'Strong'
            },
            'Jupiter': {
              'sign': 'Sagittarius',
              'house': 9,
              'degree': '12° 30\'',
              'status': 'Exalted'
            },
            'Saturn': {
              'sign': 'Capricorn',
              'house': 10,
              'degree': '25° 15\'',
              'status': 'Strong'
            },
            'Rahu': {
              'sign': 'Gemini',
              'house': 3,
              'degree': '7° 40\'',
              'status': 'Neutral'
            },
            'Ketu': {
              'sign': 'Sagittarius',
              'house': 9,
              'degree': '7° 40\'',
              'status': 'Neutral'
            },
          },
          'houses': {
            '1st House': 'Libra - Self, personality, appearance',
            '2nd House': 'Scorpio - Wealth, family, speech',
            '3rd House': 'Sagittarius - Siblings, courage, short journeys',
            '4th House': 'Capricorn - Mother, home, property',
            '5th House': 'Aquarius - Children, intelligence, creativity',
            '6th House': 'Pisces - Enemies, health, service',
            '7th House': 'Aries - Marriage, partnerships, business',
            '8th House': 'Taurus - Longevity, obstacles, occult',
            '9th House': 'Gemini - Religion, higher education, luck',
            '10th House': 'Cancer - Career, profession, reputation',
            '11th House': 'Leo - Income, gains, elder siblings',
            '12th House': 'Virgo - Expenses, losses, foreign travel',
          }
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
                              'Birth Chart Analysis',
                              style: TextStyle(
                                fontSize: 24,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                              ),
                              textAlign: TextAlign.center,
                            ),
                          ),
                          SizedBox(width: 48),
                        ],
                      ),
                      SizedBox(height: 20),

                      if (birthChartData == null) ...[
                        // Birth details form
                        Container(
                          padding: EdgeInsets.all(24),
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
                                'Enter Your Birth Details',
                                style: TextStyle(
                                  fontSize: 20,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                ),
                              ),
                              SizedBox(height: 24),

                              // Name field
                              TextField(
                                controller: nameController,
                                decoration: InputDecoration(
                                  labelText: 'Full Name',
                                  prefixIcon: Icon(Icons.person,
                                      color: Color(0xFFFFB74D)),
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
                                  focusedBorder: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(15),
                                    borderSide: BorderSide(
                                        color: Color(0xFFFFCC02), width: 2),
                                  ),
                                  filled: true,
                                  fillColor: Color(0xFF2a2a3a),
                                  labelStyle:
                                      TextStyle(color: Color(0xFFFFB74D)),
                                ),
                                style: TextStyle(color: Colors.white),
                              ),
                              SizedBox(height: 16),

                              // Date picker
                              InkWell(
                                onTap: _selectDate,
                                child: Container(
                                  padding: EdgeInsets.all(16),
                                  decoration: BoxDecoration(
                                    border:
                                        Border.all(color: Color(0xFFFFB74D)),
                                    borderRadius: BorderRadius.circular(15),
                                    color: Color(0xFF2a2a3a),
                                  ),
                                  child: Row(
                                    children: [
                                      Icon(Icons.calendar_today,
                                          color: Color(0xFFFFB74D)),
                                      SizedBox(width: 12),
                                      Text(
                                        'Birth Date: ${selectedDate.day}/${selectedDate.month}/${selectedDate.year}',
                                        style: TextStyle(color: Colors.white),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                              SizedBox(height: 16),

                              // Time picker
                              InkWell(
                                onTap: _selectTime,
                                child: Container(
                                  padding: EdgeInsets.all(16),
                                  decoration: BoxDecoration(
                                    border:
                                        Border.all(color: Color(0xFFFFB74D)),
                                    borderRadius: BorderRadius.circular(15),
                                    color: Color(0xFF2a2a3a),
                                  ),
                                  child: Row(
                                    children: [
                                      Icon(Icons.access_time,
                                          color: Color(0xFFFFB74D)),
                                      SizedBox(width: 12),
                                      Text(
                                        'Birth Time: ${selectedTime.format(context)}',
                                        style: TextStyle(color: Colors.white),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                              SizedBox(height: 16),

                              // Location dropdown
                              DropdownButtonFormField<String>(
                                value: selectedLocation,
                                decoration: InputDecoration(
                                  labelText: 'Birth Location',
                                  prefixIcon: Icon(Icons.location_on,
                                      color: Color(0xFFFFB74D)),
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
                                  labelStyle:
                                      TextStyle(color: Color(0xFFFFB74D)),
                                ),
                                dropdownColor: Color(0xFF2a2a3a),
                                style: TextStyle(color: Colors.white),
                                items: locations.map((String location) {
                                  return DropdownMenuItem<String>(
                                    value: location,
                                    child: Text(location),
                                  );
                                }).toList(),
                                onChanged: (String? newValue) {
                                  setState(() {
                                    selectedLocation = newValue!;
                                  });
                                },
                              ),
                              SizedBox(height: 24),

                              // Generate button
                              SizedBox(
                                width: double.infinity,
                                child: loading
                                    ? Center(
                                        child: CircularProgressIndicator(
                                            color: Color(0xFFFFB74D)))
                                    : ElevatedButton(
                                        onPressed: _generateBirthChart,
                                        style: ElevatedButton.styleFrom(
                                          backgroundColor: Color(0xFFFFB74D),
                                          foregroundColor: Colors.black87,
                                          padding: EdgeInsets.symmetric(
                                              vertical: 16),
                                          shape: RoundedRectangleBorder(
                                            borderRadius:
                                                BorderRadius.circular(15),
                                          ),
                                        ),
                                        child: Text(
                                          'Generate Birth Chart',
                                          style: TextStyle(
                                              fontSize: 16,
                                              fontWeight: FontWeight.bold),
                                        ),
                                      ),
                              ),
                            ],
                          ),
                        ),
                      ] else ...[
                        // Birth chart results
                        _buildBirthChartResults(),
                      ],
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

  Widget _buildBirthChartResults() {
    return Column(
      children: [
        // Basic info
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
                'Birth Chart Analysis',
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              SizedBox(height: 16),
              Text(
                'Name: ${birthChartData!['name']}',
                style: TextStyle(color: Color(0xFFFFB74D)),
              ),
              Text(
                'Birth: ${birthChartData!['birth_date']} at ${birthChartData!['birth_time']}',
                style: TextStyle(color: Color(0xFFFFB74D)),
              ),
              Text(
                'Location: ${birthChartData!['location']}',
                style: TextStyle(color: Color(0xFFFFB74D)),
              ),
            ],
          ),
        ),
        SizedBox(height: 20),

        // Planetary positions
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
                'Planetary Positions',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              SizedBox(height: 16),
              ...birthChartData!['planets']
                  .entries
                  .map((planet) => _buildPlanetRow(planet.key, planet.value))
                  .toList(),
            ],
          ),
        ),
        SizedBox(height: 20),

        // Houses
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
                'House Analysis',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              SizedBox(height: 16),
              ...birthChartData!['houses']
                  .entries
                  .map((house) => _buildHouseRow(house.key, house.value))
                  .toList(),
            ],
          ),
        ),
        SizedBox(height: 20),

        // Regenerate button
        ElevatedButton(
          onPressed: () {
            setState(() {
              birthChartData = null;
            });
          },
          style: ElevatedButton.styleFrom(
            backgroundColor: Color(0xFF424242),
            foregroundColor: Colors.white,
          ),
          child: Text('Generate New Chart'),
        ),
      ],
    );
  }

  Widget _buildPlanetRow(String planet, Map<String, dynamic> data) {
    return Padding(
      padding: EdgeInsets.symmetric(vertical: 8),
      child: Row(
        children: [
          Container(
            width: 60,
            child: Text(
              planet,
              style: TextStyle(
                fontWeight: FontWeight.bold,
                color: Color(0xFFFFB74D),
              ),
            ),
          ),
          Expanded(
            child: Text(
              '${data['sign']} ${data['degree']} (House ${data['house']})',
              style: TextStyle(color: Colors.white),
            ),
          ),
          Container(
            padding: EdgeInsets.symmetric(horizontal: 8, vertical: 4),
            decoration: BoxDecoration(
              color: _getStatusColor(data['status']).withOpacity(0.2),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Text(
              data['status'],
              style: TextStyle(
                color: _getStatusColor(data['status']),
                fontSize: 12,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildHouseRow(String house, String description) {
    return Padding(
      padding: EdgeInsets.symmetric(vertical: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            house,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              color: Color(0xFFFFB74D),
            ),
          ),
          SizedBox(height: 4),
          Text(
            description,
            style: TextStyle(color: Colors.white70, fontSize: 14),
          ),
        ],
      ),
    );
  }

  Color _getStatusColor(String status) {
    switch (status.toLowerCase()) {
      case 'exalted':
        return Colors.green;
      case 'strong':
        return Color(0xFFFFB74D);
      case 'debilitated':
        return Colors.red;
      default:
        return Colors.grey;
    }
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
