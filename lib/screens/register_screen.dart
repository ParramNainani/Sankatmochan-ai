import 'package:flutter/material.dart';
import 'dart:math' as math;

class RegisterScreen extends StatefulWidget {
  @override
  _RegisterScreenState createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen>
    with TickerProviderStateMixin {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  String error = '';
  bool loading = false;
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

  void register() async {
    setState(() {
      loading = true;
      error = '';
    });

    // Simulate registration delay
    await Future.delayed(Duration(seconds: 1));

    setState(() {
      loading = false;
    });

    // For now, just navigate to home
    Navigator.pushReplacementNamed(context, '/home');
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
                child: Center(
                  child: SingleChildScrollView(
                    padding: EdgeInsets.all(24.0),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        // Logo/Title section
                        Container(
                          padding: EdgeInsets.all(20),
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            gradient: RadialGradient(
                              colors: [
                                Color(0xFFFFB74D).withOpacity(0.3),
                                Colors.transparent,
                              ],
                            ),
                          ),
                          child: Icon(
                            Icons.auto_awesome,
                            size: 60,
                            color: Color(0xFFFFB74D),
                          ),
                        ),
                        SizedBox(height: 20),
                        Text(
                          'Join the Cosmos',
                          style: TextStyle(
                            fontSize: 32,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                            letterSpacing: 2,
                          ),
                        ),
                        SizedBox(height: 8),
                        Text(
                          'Begin Your Astrological Journey',
                          style: TextStyle(
                            fontSize: 16,
                            color: Color(0xFFFFB74D),
                            letterSpacing: 1,
                          ),
                        ),
                        SizedBox(height: 40),

                        // Register form - Smaller centered box
                        Container(
                          width: 350, // Fixed width
                          constraints: BoxConstraints(maxWidth: 400),
                          padding: EdgeInsets.all(32),
                          decoration: BoxDecoration(
                            color: Color(0xFF1e1e2e).withOpacity(0.9),
                            borderRadius: BorderRadius.circular(25),
                            border: Border.all(
                              color: Color(0xFFFFB74D).withOpacity(0.4),
                              width: 2,
                            ),
                            boxShadow: [
                              BoxShadow(
                                color: Color(0xFFFFB74D).withOpacity(0.3),
                                blurRadius: 25,
                                spreadRadius: 8,
                              ),
                            ],
                          ),
                          child: Column(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Text(
                                'Create Account',
                                style: TextStyle(
                                  fontSize: 24,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                ),
                              ),
                              SizedBox(height: 8),
                              Text(
                                'Start your cosmic journey today',
                                style: TextStyle(
                                  fontSize: 14,
                                  color: Color(0xFFFFB74D),
                                ),
                              ),
                              SizedBox(height: 24),
                              TextField(
                                controller: emailController,
                                decoration: InputDecoration(
                                  labelText: 'Email',
                                  prefixIcon: Icon(Icons.email,
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
                              TextField(
                                controller: passwordController,
                                decoration: InputDecoration(
                                  labelText: 'Password',
                                  prefixIcon: Icon(Icons.lock,
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
                                obscureText: true,
                                style: TextStyle(color: Colors.white),
                              ),
                              SizedBox(height: 20),
                              if (error.isNotEmpty)
                                Container(
                                  padding: EdgeInsets.all(12),
                                  decoration: BoxDecoration(
                                    color: Colors.red.withOpacity(0.2),
                                    borderRadius: BorderRadius.circular(10),
                                  ),
                                  child: Text(
                                    error,
                                    style: TextStyle(color: Colors.red[300]),
                                  ),
                                ),
                              SizedBox(height: 24),
                              SizedBox(
                                width: double.infinity,
                                child: loading
                                    ? Center(
                                        child: CircularProgressIndicator(
                                            color: Color(0xFFFFB74D)))
                                    : ElevatedButton(
                                        onPressed: register,
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
                                          'Register',
                                          style: TextStyle(
                                              fontSize: 16,
                                              fontWeight: FontWeight.bold),
                                        ),
                                      ),
                              ),
                            ],
                          ),
                        ),
                        SizedBox(height: 24),
                        TextButton(
                          onPressed: () {
                            Navigator.pushReplacementNamed(context, '/login');
                          },
                          child: Text(
                            'Already have an account? Login',
                            style: TextStyle(
                                fontSize: 16, color: Color(0xFFFFB74D)),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ],
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
