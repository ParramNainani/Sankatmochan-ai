import 'package:flutter/material.dart';
import 'dart:math' as math;

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> with TickerProviderStateMixin {
  late AnimationController _animationController;
  late Animation<double> _fadeAnimation;

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
            ...List.generate(50, (index) => _buildStar(index)),

            // Main content
            SafeArea(
              child: FadeTransition(
                opacity: _fadeAnimation,
                child: SingleChildScrollView(
                  padding: EdgeInsets.all(24.0),
                  child: Column(
                    children: [
                      // Header section
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Welcome to',
                                style: TextStyle(
                                  fontSize: 18,
                                  color: Color(0xFF9fa8da),
                                ),
                              ),
                              Text(
                                'Sankatmochan AI',
                                style: TextStyle(
                                  fontSize: 28,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                  letterSpacing: 2,
                                ),
                              ),
                            ],
                          ),
                          Container(
                            padding: EdgeInsets.all(12),
                            decoration: BoxDecoration(
                              shape: BoxShape.circle,
                              gradient: RadialGradient(
                                colors: [
                                  Color(0xFF3949ab).withOpacity(0.3),
                                  Colors.transparent,
                                ],
                              ),
                            ),
                            child: Icon(
                              Icons.auto_awesome,
                              size: 30,
                              color: Color(0xFF7986cb),
                            ),
                          ),
                        ],
                      ),
                      SizedBox(height: 30),

                      // Astrological features grid
                      GridView.count(
                        shrinkWrap: true,
                        physics: NeverScrollableScrollPhysics(),
                        crossAxisCount: 2,
                        crossAxisSpacing: 16,
                        mainAxisSpacing: 16,
                        childAspectRatio: 1.1,
                        children: [
                          _buildFeatureCard(
                            'Daily Horoscope',
                            Icons.wb_sunny,
                            'Get your daily cosmic guidance',
                            Color(0xFFFF9800),
                            () => Navigator.pushNamed(context, '/horoscope'),
                          ),
                          _buildFeatureCard(
                            'Birth Chart',
                            Icons.pie_chart,
                            'Analyze your natal chart',
                            Color(0xFFE91E63),
                            () => Navigator.pushNamed(context, '/birth-chart'),
                          ),
                          _buildFeatureCard(
                            'Planetary Positions',
                            Icons.public,
                            'Current planetary alignments',
                            Color(0xFF9C27B0),
                            () => Navigator.pushNamed(
                                context, '/planetary-positions'),
                          ),
                          _buildFeatureCard(
                            'Compatibility',
                            Icons.favorite,
                            'Check relationship compatibility',
                            Color(0xFFF44336),
                            () =>
                                Navigator.pushNamed(context, '/compatibility'),
                          ),
                          _buildFeatureCard(
                            'Muhurat',
                            Icons.schedule,
                            'Find auspicious timings',
                            Color(0xFF4CAF50),
                            () => Navigator.pushNamed(context, '/muhurat'),
                          ),
                          _buildFeatureCard(
                            'Gemstones',
                            Icons.diamond,
                            'Discover your lucky stones',
                            Color(0xFF00BCD4),
                            () => Navigator.pushNamed(context, '/gemstones'),
                          ),
                          _buildFeatureCard(
                            'Charts Library',
                            Icons.folder_open,
                            'View stored birth charts',
                            Color(0xFF795548),
                            () =>
                                Navigator.pushNamed(context, '/charts-library'),
                          ),
                        ],
                      ),
                      SizedBox(height: 30),

                      // Quick actions
                      Container(
                        padding: EdgeInsets.all(20),
                        decoration: BoxDecoration(
                          color: Color(0xFF1e1e2e).withOpacity(0.8),
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(
                            color: Color(0xFF3949ab).withOpacity(0.3),
                            width: 1,
                          ),
                          boxShadow: [
                            BoxShadow(
                              color: Color(0xFF3949ab).withOpacity(0.2),
                              blurRadius: 20,
                              spreadRadius: 5,
                            ),
                          ],
                        ),
                        child: Column(
                          children: [
                            Text(
                              'Quick Actions',
                              style: TextStyle(
                                fontSize: 20,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                              ),
                            ),
                            SizedBox(height: 20),
                            Row(
                              children: [
                                Expanded(
                                  child: ElevatedButton.icon(
                                    onPressed: () {
                                      // TODO: Navigate to horoscope
                                    },
                                    icon: Icon(Icons.psychology),
                                    label: Text('Today\'s Horoscope'),
                                  ),
                                ),
                                SizedBox(width: 16),
                                Expanded(
                                  child: ElevatedButton.icon(
                                    onPressed: () {
                                      // TODO: Navigate to birth chart
                                    },
                                    icon: Icon(Icons.analytics),
                                    label: Text('My Chart'),
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                      SizedBox(height: 20),

                      // Logout button
                      SizedBox(
                        width: double.infinity,
                        child: ElevatedButton.icon(
                          onPressed: () {
                            Navigator.pushReplacementNamed(context, '/login');
                          },
                          icon: Icon(Icons.logout),
                          label: Text('Logout'),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Color(0xFF424242),
                            padding: EdgeInsets.symmetric(vertical: 16),
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

  Widget _buildFeatureCard(String title, IconData icon, String description,
      Color color, VoidCallback? onTap) {
    return Container(
      decoration: BoxDecoration(
        color: Color(0xFF1e1e2e).withOpacity(0.8),
        borderRadius: BorderRadius.circular(15),
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
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(15),
        child: Padding(
          padding: EdgeInsets.all(16),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: EdgeInsets.all(12),
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: color.withOpacity(0.2),
                ),
                child: Icon(
                  icon,
                  size: 30,
                  color: color,
                ),
              ),
              SizedBox(height: 12),
              Text(
                title,
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 8),
              Text(
                description,
                style: TextStyle(
                  fontSize: 12,
                  color: Color(0xFF9fa8da),
                ),
                textAlign: TextAlign.center,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
            ],
          ),
        ),
      ),
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
