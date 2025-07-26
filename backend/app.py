from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
from datetime import datetime
import json

# Add the parent directory to the path to import your existing modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your existing modules
try:
    from core.calculations import *
    from core.dashas import *
    from core.patterns import *
    from core.predictions import *
    from core.chart_visualizer import *
except ImportError as e:
    print(f"Warning: Could not import some modules: {e}")

app = Flask(__name__)
CORS(app)  # Enable CORS for Flutter web app

@app.route('/')
def home():
    return jsonify({
        'message': 'Sankatmochan AI Backend API',
        'version': '1.0.0',
        'endpoints': [
            '/api/horoscope/<zodiac_sign>',
            '/api/birth-chart',
            '/api/planetary-positions',
            '/api/compatibility',
            '/api/muhurat',
            '/api/gemstones'
        ]
    })

@app.route('/api/horoscope/<zodiac_sign>')
def get_horoscope(zodiac_sign):
    """Get daily horoscope for a zodiac sign"""
    try:
        # You can integrate your existing prediction logic here
        # For now, returning mock data
        horoscopes = {
            'Aries': {
                'general': 'Today brings exciting opportunities for leadership and new beginnings.',
                'love': 'Passion and romance are highlighted. Single Aries may meet someone special.',
                'career': 'Your innovative ideas will be well-received. Take initiative in projects.',
                'health': 'Focus on cardiovascular exercise. Energy levels are high.',
                'lucky_color': 'Red',
                'lucky_number': '9',
                'compatibility': 'Leo, Sagittarius'
            },
            'Taurus': {
                'general': 'Stability and determination are your strengths today.',
                'love': 'Deep emotional connections are possible. Show your caring nature.',
                'career': 'Financial matters look promising. Your practical approach pays off.',
                'health': 'Grounding exercises like yoga will benefit you.',
                'lucky_color': 'Green',
                'lucky_number': '6',
                'compatibility': 'Virgo, Capricorn'
            },
            'Gemini': {
                'general': 'Communication flows easily today. Express your thoughts clearly.',
                'love': 'Intellectual connection is important. Share your ideas with your partner.',
                'career': 'Networking opportunities abound. Connect with new people.',
                'health': 'Mental exercises and puzzles will keep you sharp.',
                'lucky_color': 'Yellow',
                'lucky_number': '5',
                'compatibility': 'Libra, Aquarius'
            },
            'Cancer': {
                'general': 'Emotional sensitivity is heightened. Trust your intuition.',
                'love': 'Family and home life are important. Spend time with loved ones.',
                'career': 'Your nurturing nature helps in team environments.',
                'health': 'Focus on emotional well-being and self-care.',
                'lucky_color': 'Silver',
                'lucky_number': '2',
                'compatibility': 'Scorpio, Pisces'
            },
            'Leo': {
                'general': 'Your natural charisma shines today. Lead with confidence.',
                'love': 'Romance is in the air. Show your generous and loving nature.',
                'career': 'Recognition for your work is likely. Take center stage.',
                'health': 'Creative activities will boost your energy.',
                'lucky_color': 'Gold',
                'lucky_number': '1',
                'compatibility': 'Aries, Sagittarius'
            },
            'Virgo': {
                'general': 'Attention to detail serves you well today.',
                'love': 'Practical gestures of love are appreciated.',
                'career': 'Your analytical skills are valuable. Focus on organization.',
                'health': 'Healthy routines and diet are beneficial.',
                'lucky_color': 'Brown',
                'lucky_number': '5',
                'compatibility': 'Taurus, Capricorn'
            },
            'Libra': {
                'general': 'Balance and harmony are your themes today.',
                'love': 'Partnership and cooperation are highlighted.',
                'career': 'Diplomatic skills help resolve conflicts.',
                'health': 'Gentle exercise and meditation bring peace.',
                'lucky_color': 'Pink',
                'lucky_number': '6',
                'compatibility': 'Gemini, Aquarius'
            },
            'Scorpio': {
                'general': 'Your intensity and passion are powerful today.',
                'love': 'Deep emotional connections are possible.',
                'career': 'Your investigative skills uncover important information.',
                'health': 'Transformative practices like yoga are beneficial.',
                'lucky_color': 'Deep Red',
                'lucky_number': '8',
                'compatibility': 'Cancer, Pisces'
            },
            'Sagittarius': {
                'general': 'Adventure and exploration call to you today.',
                'love': 'Optimism and enthusiasm attract positive relationships.',
                'career': 'New opportunities for growth and learning appear.',
                'health': 'Outdoor activities and travel energize you.',
                'lucky_color': 'Purple',
                'lucky_number': '3',
                'compatibility': 'Aries, Leo'
            },
            'Capricorn': {
                'general': 'Your ambition and discipline lead to success.',
                'love': 'Long-term commitment and stability are valued.',
                'career': 'Your hard work and determination pay off.',
                'health': 'Structured fitness routines work best.',
                'lucky_color': 'Black',
                'lucky_number': '4',
                'compatibility': 'Taurus, Virgo'
            },
            'Aquarius': {
                'general': 'Innovation and originality are your strengths.',
                'love': 'Intellectual connection and friendship are important.',
                'career': 'Your unique perspective brings fresh solutions.',
                'health': 'Alternative therapies and technology help.',
                'lucky_color': 'Electric Blue',
                'lucky_number': '7',
                'compatibility': 'Gemini, Libra'
            },
            'Pisces': {
                'general': 'Intuition and creativity flow freely today.',
                'love': 'Spiritual and emotional connections are deep.',
                'career': 'Your artistic and compassionate nature shines.',
                'health': 'Water activities and meditation are healing.',
                'lucky_color': 'Sea Green',
                'lucky_number': '2',
                'compatibility': 'Cancer, Scorpio'
            }
        }
        
        if zodiac_sign in horoscopes:
            return jsonify(horoscopes[zodiac_sign])
        else:
            return jsonify({'error': 'Invalid zodiac sign'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/birth-chart', methods=['POST'])
def generate_birth_chart():
    """Generate birth chart analysis"""
    try:
        data = request.get_json()
        name = data.get('name')
        birth_date = data.get('birth_date')
        birth_time = data.get('birth_time')
        location = data.get('location')
        
        # Here you can integrate your existing birth chart calculation logic
        # For now, returning mock data
        
        birth_chart = {
            'name': name,
            'birth_date': birth_date,
            'birth_time': birth_time,
            'location': location,
            'sun_sign': 'Aries',
            'moon_sign': 'Cancer',
            'ascendant': 'Libra',
            'planets': {
                'Sun': {'sign': 'Aries', 'house': 1, 'degree': '15° 30\'', 'status': 'Strong'},
                'Moon': {'sign': 'Cancer', 'house': 4, 'degree': '8° 45\'', 'status': 'Exalted'},
                'Mercury': {'sign': 'Pisces', 'house': 12, 'degree': '22° 10\'', 'status': 'Debilitated'},
                'Venus': {'sign': 'Taurus', 'house': 2, 'degree': '5° 20\'', 'status': 'Strong'},
                'Mars': {'sign': 'Scorpio', 'house': 8, 'degree': '18° 55\'', 'status': 'Strong'},
                'Jupiter': {'sign': 'Sagittarius', 'house': 9, 'degree': '12° 30\'', 'status': 'Exalted'},
                'Saturn': {'sign': 'Capricorn', 'house': 10, 'degree': '25° 15\'', 'status': 'Strong'},
                'Rahu': {'sign': 'Gemini', 'house': 3, 'degree': '7° 40\'', 'status': 'Neutral'},
                'Ketu': {'sign': 'Sagittarius', 'house': 9, 'degree': '7° 40\'', 'status': 'Neutral'},
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
        }
        
        return jsonify(birth_chart)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/planetary-positions')
def get_planetary_positions():
    """Get current planetary positions"""
    try:
        # You can integrate your existing planetary calculation logic here
        current_time = datetime.now().isoformat()
        
        positions = {
            'current_time': current_time,
            'planets': {
                'Sun': {'sign': 'Aries', 'degree': '15° 30\'', 'house': 1},
                'Moon': {'sign': 'Cancer', 'degree': '8° 45\'', 'house': 4},
                'Mercury': {'sign': 'Pisces', 'degree': '22° 10\'', 'house': 12},
                'Venus': {'sign': 'Taurus', 'degree': '5° 20\'', 'house': 2},
                'Mars': {'sign': 'Scorpio', 'degree': '18° 55\'', 'house': 8},
                'Jupiter': {'sign': 'Sagittarius', 'degree': '12° 30\'', 'house': 9},
                'Saturn': {'sign': 'Capricorn', 'degree': '25° 15\'', 'house': 10},
            }
        }
        
        return jsonify(positions)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/compatibility', methods=['POST'])
def get_compatibility():
    """Get compatibility analysis between two zodiac signs"""
    try:
        data = request.get_json()
        sign1 = data.get('sign1')
        sign2 = data.get('sign2')
        
        # You can integrate your existing compatibility logic here
        compatibility = {
            'sign1': sign1,
            'sign2': sign2,
            'overall_score': 85,
            'love_score': 90,
            'friendship_score': 80,
            'communication_score': 85,
            'analysis': f'This is a highly compatible pairing between {sign1} and {sign2} with great potential for love and friendship.',
            'strengths': ['Strong emotional connection', 'Good communication', 'Shared values'],
            'challenges': ['Occasional stubbornness', 'Different approaches to life'],
            'advice': 'Focus on open communication and compromise to strengthen your relationship.'
        }
        
        return jsonify(compatibility)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/muhurat', methods=['POST'])
def get_muhurat():
    """Get auspicious timings (muhurat) for various activities"""
    try:
        data = request.get_json()
        date = data.get('date')
        purpose = data.get('purpose')
        
        # You can integrate your existing muhurat calculation logic here
        muhurat = {
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
        }
        
        return jsonify(muhurat)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/gemstones', methods=['POST'])
def get_gemstone_recommendations():
    """Get gemstone recommendations based on zodiac sign and birth details"""
    try:
        data = request.get_json()
        zodiac_sign = data.get('zodiac_sign')
        birth_date = data.get('birth_date')
        
        # You can integrate your existing gemstone recommendation logic here
        gemstones = {
            'zodiac_sign': zodiac_sign,
            'primary_gemstone': {
                'name': 'Ruby',
                'description': 'Enhances leadership qualities and confidence',
                'wearing_instructions': 'Wear on ring finger of right hand on Sunday',
                'benefits': ['Increases confidence', 'Improves leadership', 'Enhances vitality']
            },
            'secondary_gemstones': [
                {
                    'name': 'Red Coral',
                    'description': 'Strengthens Mars and provides courage',
                    'wearing_instructions': 'Wear on ring finger of right hand on Tuesday'
                },
                {
                    'name': 'Yellow Sapphire',
                    'description': 'Strengthens Jupiter and brings wisdom',
                    'wearing_instructions': 'Wear on index finger of right hand on Thursday'
                }
            ],
            'avoid_gemstones': [
                {
                    'name': 'Pearl',
                    'reason': 'May conflict with your planetary positions'
                }
            ]
        }
        
        return jsonify(gemstones)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Sankatmochan AI Backend...")
    print("API endpoints available:")
    print("- GET  /api/horoscope/<zodiac_sign>")
    print("- POST /api/birth-chart")
    print("- GET  /api/planetary-positions")
    print("- POST /api/compatibility")
    print("- POST /api/muhurat")
    print("- POST /api/gemstones")
    print("\nServer running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000) 