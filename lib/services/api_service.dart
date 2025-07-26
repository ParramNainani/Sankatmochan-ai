import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // Update this URL to match your Python backend
  static const String baseUrl =
      'http://localhost:5000'; // or your actual backend URL

  // Get daily horoscope
  static Future<Map<String, dynamic>> getDailyHoroscope(
      String zodiacSign) async {
    try {
      final response = await http.get(
        Uri.parse('$baseUrl/api/horoscope/$zodiacSign'),
        headers: {'Content-Type': 'application/json'},
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to load horoscope');
      }
    } catch (e) {
      // Return mock data if API is not available
      return {
        'general':
            'Today brings exciting opportunities for leadership and new beginnings.',
        'love':
            'Passion and romance are highlighted. Single $zodiacSign may meet someone special.',
        'career':
            'Your innovative ideas will be well-received. Take initiative in projects.',
        'health': 'Focus on cardiovascular exercise. Energy levels are high.',
        'lucky_color': 'Red',
        'lucky_number': '9',
        'compatibility': 'Leo, Sagittarius'
      };
    }
  }

  // Generate birth chart
  static Future<Map<String, dynamic>> generateBirthChart({
    required String name,
    required String birthDate,
    required String birthTime,
    required String location,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/birth-chart'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'name': name,
          'birth_date': birthDate,
          'birth_time': birthTime,
          'location': location,
        }),
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to generate birth chart');
      }
    } catch (e) {
      // Return mock data if API is not available
      return {
        'name': name,
        'birth_date': birthDate,
        'birth_time': birthTime,
        'location': location,
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
    }
  }

  // Get planetary positions
  static Future<Map<String, dynamic>> getPlanetaryPositions() async {
    try {
      final response = await http.get(
        Uri.parse('$baseUrl/api/planetary-positions'),
        headers: {'Content-Type': 'application/json'},
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to load planetary positions');
      }
    } catch (e) {
      // Return mock data if API is not available
      return {
        'current_time': DateTime.now().toIso8601String(),
        'planets': {
          'Sun': {'sign': 'Aries', 'degree': '15° 30\'', 'house': 1},
          'Moon': {'sign': 'Cancer', 'degree': '8° 45\'', 'house': 4},
          'Mercury': {'sign': 'Pisces', 'degree': '22° 10\'', 'house': 12},
          'Venus': {'sign': 'Taurus', 'degree': '5° 20\'', 'house': 2},
          'Mars': {'sign': 'Scorpio', 'degree': '18° 55\'', 'house': 8},
          'Jupiter': {'sign': 'Sagittarius', 'degree': '12° 30\'', 'house': 9},
          'Saturn': {'sign': 'Capricorn', 'degree': '25° 15\'', 'house': 10},
        }
      };
    }
  }

  // Get compatibility analysis
  static Future<Map<String, dynamic>> getCompatibility({
    required String sign1,
    required String sign2,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/compatibility'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'sign1': sign1,
          'sign2': sign2,
        }),
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to get compatibility');
      }
    } catch (e) {
      // Return mock data if API is not available
      return {
        'sign1': sign1,
        'sign2': sign2,
        'overall_score': 85,
        'love_score': 90,
        'friendship_score': 80,
        'communication_score': 85,
        'analysis':
            'This is a highly compatible pairing with great potential for love and friendship.',
        'strengths': [
          'Strong emotional connection',
          'Good communication',
          'Shared values'
        ],
        'challenges': [
          'Occasional stubbornness',
          'Different approaches to life'
        ],
        'advice':
            'Focus on open communication and compromise to strengthen your relationship.'
      };
    }
  }

  // Get muhurat (auspicious timings)
  static Future<Map<String, dynamic>> getMuhurat({
    required String date,
    required String purpose,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/muhurat'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'date': date,
          'purpose': purpose,
        }),
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to get muhurat');
      }
    } catch (e) {
      // Return mock data if API is not available
      return {
        'date': date,
        'purpose': purpose,
        'auspicious_timings': [
          {
            'start_time': '06:00',
            'end_time': '08:00',
            'description': 'Brahma Muhurat - Best for spiritual activities',
            'rating': 5
          },
          {
            'start_time': '10:00',
            'end_time': '12:00',
            'description': 'Good for business and career activities',
            'rating': 4
          },
          {
            'start_time': '15:00',
            'end_time': '17:00',
            'description': 'Suitable for travel and new beginnings',
            'rating': 3
          }
        ],
        'avoid_timings': [
          {
            'start_time': '12:00',
            'end_time': '13:00',
            'reason': 'Rahu Kaal - Avoid important activities'
          }
        ]
      };
    }
  }

  // Get gemstone recommendations
  static Future<Map<String, dynamic>> getGemstoneRecommendations({
    required String zodiacSign,
    required String birthDate,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/gemstones'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'zodiac_sign': zodiacSign,
          'birth_date': birthDate,
        }),
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to get gemstone recommendations');
      }
    } catch (e) {
      // Return mock data if API is not available
      return {
        'zodiac_sign': zodiacSign,
        'primary_gemstone': {
          'name': 'Ruby',
          'description': 'Enhances leadership qualities and confidence',
          'wearing_instructions': 'Wear on ring finger of right hand on Sunday',
          'benefits': [
            'Increases confidence',
            'Improves leadership',
            'Enhances vitality'
          ]
        },
        'secondary_gemstones': [
          {
            'name': 'Red Coral',
            'description': 'Strengthens Mars and provides courage',
            'wearing_instructions':
                'Wear on ring finger of right hand on Tuesday'
          },
          {
            'name': 'Yellow Sapphire',
            'description': 'Strengthens Jupiter and brings wisdom',
            'wearing_instructions':
                'Wear on index finger of right hand on Thursday'
          }
        ],
        'avoid_gemstones': [
          {
            'name': 'Pearl',
            'reason': 'May conflict with your planetary positions'
          }
        ]
      };
    }
  }
}
