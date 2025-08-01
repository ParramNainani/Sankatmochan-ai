import 'package:flutter/material.dart';
import 'dart:math' as math;
import '../services/auth_service.dart';
import 'package:firebase_auth/firebase_auth.dart';

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen>
    with TickerProviderStateMixin {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  String error = '';
  bool loading = false;
  late AnimationController _animationController;
  late Animation<double> _fadeAnimation;
  final AuthService _authService = AuthService();

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

  void login() async {
    setState(() {
      loading = true;
      error = '';
    });

    try {
      String? errorMessage = await _authService.signIn(
        emailController.text.trim(),
        passwordController.text,
      );

      setState(() {
        loading = false;
      });

      if (errorMessage != null) {
        setState(() {
          error = errorMessage;
        });
      } else {
        Navigator.pushReplacementNamed(context, '/home');
      }
    } catch (e) {
      setState(() {
        loading = false;
        error = 'An error occurred during login.';
      });
    }
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
                          'Sankatmochan AI',
                          style: TextStyle(
                            fontSize: 32,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                            letterSpacing: 2,
                          ),
                        ),
                        SizedBox(height: 8),
                        Text(
                          'Vedic Astrology & AI',
                          style: TextStyle(
                            fontSize: 16,
                            color: Color(0xFFFFB74D),
                            letterSpacing: 1,
                          ),
                        ),
                        SizedBox(height: 40),

                        // Login form - Smaller centered box
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
                                'Welcome Back',
                                style: TextStyle(
                                  fontSize: 24,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                ),
                              ),
                              SizedBox(height: 8),
                              Text(
                                'Enter your cosmic credentials',
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
                                        onPressed: login,
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
                                          'Login',
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
                            Navigator.pushReplacementNamed(
                                context, '/register');
                          },
                          child: Text(
                            'Don\'t have an account? Register',
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
