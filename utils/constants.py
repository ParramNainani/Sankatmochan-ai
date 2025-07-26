"""
Astrological Constants
All constant values used in calculations
"""

# Nakshatra names in order
NAKSHATRA_NAMES = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Rashi (Zodiac sign) names
RASHI_NAMES = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Sanskrit Rashi names
RASHI_NAMES_SANSKRIT = [
    "Mesha", "Vrishabha", "Mithuna", "Karka", "Simha", "Kanya",
    "Tula", "Vrishchika", "Dhanu", "Makara", "Kumbha", "Meena"
]

# Nakshatra lords for Vimshottari Dasha
NAKSHATRA_LORDS = {
    'Ashwini': 'Ketu', 'Bharani': 'Venus', 'Krittika': 'Sun',
    'Rohini': 'Moon', 'Mrigashira': 'Mars', 'Ardra': 'Rahu',
    'Punarvasu': 'Jupiter', 'Pushya': 'Saturn', 'Ashlesha': 'Mercury',
    'Magha': 'Ketu', 'Purva Phalguni': 'Venus', 'Uttara Phalguni': 'Sun',
    'Hasta': 'Moon', 'Chitra': 'Mars', 'Swati': 'Rahu',
    'Vishakha': 'Jupiter', 'Anuradha': 'Saturn', 'Jyeshtha': 'Mercury',
    'Mula': 'Ketu', 'Purva Ashadha': 'Venus', 'Uttara Ashadha': 'Sun',
    'Shravana': 'Moon', 'Dhanishta': 'Mars', 'Shatabhisha': 'Rahu',
    'Purva Bhadrapada': 'Jupiter', 'Uttara Bhadrapada': 'Saturn', 'Revati': 'Mercury'
}

# Vimshottari Dasha periods (in years)
VIMSHOTTARI_PERIODS = {
    'Ketu': 7, 'Venus': 20, 'Sun': 6, 'Moon': 10, 'Mars': 7,
    'Rahu': 18, 'Jupiter': 16, 'Saturn': 19, 'Mercury': 17
}

# Dasha sequence
DASHA_SEQUENCE = ['Ketu', 'Venus', 'Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury']

# Planet symbols for charts
PLANET_SYMBOLS = {
    'Sun': 'Su', 'Moon': 'Mo', 'Mars': 'Ma', 'Mercury': 'Me',
    'Jupiter': 'Ju', 'Venus': 'Ve', 'Saturn': 'Sa',
    'Rahu': 'Ra', 'Ketu': 'Ke', 'Ascendant': 'As'
}

# Planet colors for visualization
PLANET_COLORS = {
    'Sun': '#FF6B35', 'Moon': '#E8E8E8', 'Mars': '#FF0000', 'Mercury': '#00FF00',
    'Jupiter': '#FFD700', 'Venus': '#FFC0CB', 'Saturn': '#000080',
    'Rahu': '#8B4513', 'Ketu': '#696969', 'Ascendant': '#4169E1'
}

# House significations
HOUSE_SIGNIFICATIONS = {
    1: "Self, Personality, Appearance, Health",
    2: "Wealth, Family, Speech, Food",
    3: "Siblings, Courage, Communication, Short Journeys",
    4: "Mother, Home, Property, Education",
    5: "Children, Intelligence, Creativity, Romance",
    6: "Enemies, Diseases, Service, Debts",
    7: "Spouse, Partnership, Business, Marriage",
    8: "Longevity, Transformation, Occult, Inheritance",
    9: "Father, Guru, Religion, Fortune, Higher Learning",
    10: "Career, Reputation, Authority, Government",
    11: "Gains, Friends, Elder Siblings, Aspirations",
    12: "Losses, Expenses, Foreign Lands, Spirituality"
}

# Planetary significations
PLANET_SIGNIFICATIONS = {
    'Sun': "Soul, Father, Authority, Government, Leadership, Health",
    'Moon': "Mind, Mother, Emotions, Public, Water, Travel",
    'Mars': "Energy, Siblings, Property, Courage, Accidents, Surgery",
    'Mercury': "Intelligence, Communication, Business, Education, Skin",
    'Jupiter': "Wisdom, Teacher, Children, Wealth, Religion, Husband",
    'Venus': "Love, Marriage, Arts, Luxury, Beauty, Wife",
    'Saturn': "Discipline, Delays, Hard Work, Longevity, Servants",
    'Rahu': "Illusion, Foreign, Technology, Sudden Events, Materialism",
    'Ketu': "Spirituality, Detachment, Past Life, Research, Liberation"
}

# Nakshatra characteristics
NAKSHATRA_CHARACTERISTICS = {
    'Ashwini': {'deity': 'Ashwini Kumaras', 'nature': 'Swift', 'symbol': 'Horse Head'},
    'Bharani': {'deity': 'Yama', 'nature': 'Fierce', 'symbol': 'Yoni'},
    'Krittika': {'deity': 'Agni', 'nature': 'Sharp', 'symbol': 'Razor'},
    'Rohini': {'deity': 'Brahma', 'nature': 'Fixed', 'symbol': 'Cart'},
    'Mrigashira': {'deity': 'Soma', 'nature': 'Soft', 'symbol': 'Deer Head'},
    'Ardra': {'deity': 'Rudra', 'nature': 'Sharp', 'symbol': 'Teardrop'},
    'Punarvasu': {'deity': 'Aditi', 'nature': 'Movable', 'symbol': 'Bow'},
    'Pushya': {'deity': 'Brihaspati', 'nature': 'Light', 'symbol': 'Flower'},
    'Ashlesha': {'deity': 'Nagas', 'nature': 'Sharp', 'symbol': 'Serpent'},
    'Magha': {'deity': 'Pitrs', 'nature': 'Fierce', 'symbol': 'Throne'},
    'Purva Phalguni': {'deity': 'Bhaga', 'nature': 'Fierce', 'symbol': 'Hammock'},
    'Uttara Phalguni': {'deity': 'Aryaman', 'nature': 'Fixed', 'symbol': 'Bed'},
    'Hasta': {'deity': 'Savitar', 'nature': 'Light', 'symbol': 'Hand'},
    'Chitra': {'deity': 'Vishvakarma', 'nature': 'Soft', 'symbol': 'Pearl'},
    'Swati': {'deity': 'Vayu', 'nature': 'Movable', 'symbol': 'Sword'},
    'Vishakha': {'deity': 'Indra-Agni', 'nature': 'Sharp', 'symbol': 'Archway'},
    'Anuradha': {'deity': 'Mitra', 'nature': 'Soft', 'symbol': 'Lotus'},
    'Jyeshtha': {'deity': 'Indra', 'nature': 'Sharp', 'symbol': 'Earring'},
    'Mula': {'deity': 'Nirriti', 'nature': 'Sharp', 'symbol': 'Root'},
    'Purva Ashadha': {'deity': 'Apas', 'nature': 'Fierce', 'symbol': 'Fan'},
    'Uttara Ashadha': {'deity': 'Vishvedevas', 'nature': 'Fixed', 'symbol': 'Elephant Tusk'},
    'Shravana': {'deity': 'Vishnu', 'nature': 'Movable', 'symbol': 'Ear'},
    'Dhanishta': {'deity': 'Vasus', 'nature': 'Movable', 'symbol': 'Drum'},
    'Shatabhisha': {'deity': 'Varuna', 'nature': 'Movable', 'symbol': 'Circle'},
    'Purva Bhadrapada': {'deity': 'Aja Ekapada', 'nature': 'Fierce', 'symbol': 'Sword'},
    'Uttara Bhadrapada': {'deity': 'Ahir Budhnya', 'nature': 'Fixed', 'symbol': 'Snake'},
    'Revati': {'deity': 'Pushan', 'nature': 'Soft', 'symbol': 'Fish'}
}

# Remedial measures by planet
PLANETARY_REMEDIES = {
    'Sun': [
        "Chant Aditya Hridayam daily at sunrise",
        "Offer water to Sun every morning",
        "Donate wheat, jaggery, and copper items on Sundays",
        "Wear Ruby (after astrological consultation)",
        "Fast on Sundays",
        "Respect father and authority figures"
    ],
    'Moon': [
        "Chant 'Om Chandraya Namaha' 108 times daily",
        "Offer milk to Shiva on Mondays",
        "Wear Pearl or Moonstone",
        "Practice meditation near water bodies",
        "Donate white items on Mondays",
        "Respect mother and elderly women"
    ],
    'Mars': [
        "Recite Hanuman Chalisa daily",
        "Donate red lentils and red items on Tuesdays",
        "Wear Red Coral (after consultation)",
        "Practice physical exercise regularly",
        "Control anger and aggression",
        "Respect siblings and younger people"
    ],
    'Mercury': [
        "Chant 'Om Budhaya Namaha' daily",
        "Donate green items and books on Wednesdays",
        "Wear Emerald (after consultation)",
        "Engage in learning and teaching",
        "Practice truthful communication",
        "Help students and scholars"
    ],
    'Jupiter': [
        "Chant 'Om Gurave Namaha' daily",
        "Donate yellow items and turmeric on Thursdays",
        "Wear Yellow Sapphire (after consultation)",
        "Practice charity and help teachers",
        "Study religious texts",
        "Respect gurus and learned people"
    ],
    'Venus': [
        "Chant 'Om Shukraya Namaha' daily",
        "Donate white items and sweets on Fridays",
        "Wear Diamond or White Sapphire",
        "Engage in artistic activities",
        "Practice moderation in pleasures",
        "Respect women and artists"
    ],
    'Saturn': [
        "Chant 'Om Shanicharaya Namaha' daily",
        "Donate black items and oil on Saturdays",
        "Wear Blue Sapphire (after consultation)",
        "Practice discipline and serve the needy",
        "Be patient and persistent",
        "Help laborers and elderly people"
    ],
    'Rahu': [
        "Chant 'Om Rahave Namaha' daily",
        "Donate multicolored items",
        "Wear Hessonite (after consultation)",
        "Practice meditation and charity",
        "Avoid speculation and gambling",
        "Help foreigners and outcasts"
    ],
    'Ketu': [
        "Chant 'Om Ketave Namaha' daily",
        "Donate spiritual items",
        "Wear Cat's Eye (after consultation)",
        "Practice spiritual disciplines",
        "Study occult sciences",
        "Help spiritual seekers"
    ]
}

# Astronomical constants
JULIAN_DAY_J2000 = 2451545.0
SECONDS_PER_DAY = 86400.0
DAYS_PER_YEAR = 365.25
DEGREES_PER_CIRCLE = 360.0
MINUTES_PER_DEGREE = 60.0
SECONDS_PER_MINUTE = 60.0

# Nakshatra span in degrees
NAKSHATRA_SPAN = DEGREES_PER_CIRCLE / 27.0  # 13.333... degrees

# Rashi span in degrees
RASHI_SPAN = DEGREES_PER_CIRCLE / 12.0  # 30 degrees

# Pada span in degrees
PADA_SPAN = NAKSHATRA_SPAN / 4.0  # 3.333... degrees

print("✅ Astrological Constants loaded")
