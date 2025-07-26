"""
Utility Helper Functions
Common functions used across the system
"""

import datetime
import json
import os
from typing import Dict, List, Any, Optional

def normalize_longitude(longitude: float) -> float:
    """Normalize longitude to 0-360 range"""
    longitude = longitude % 360
    if longitude < 0:
        longitude += 360
    return longitude

def degrees_to_dms(degrees: float) -> tuple:
    """Convert decimal degrees to degrees, minutes, seconds"""
    deg = int(degrees)
    min_float = (degrees - deg) * 60
    minutes = int(min_float)
    seconds = (min_float - minutes) * 60
    return deg, minutes, seconds

def dms_to_degrees(degrees: int, minutes: int, seconds: float) -> float:
    """Convert degrees, minutes, seconds to decimal degrees"""
    return degrees + minutes/60.0 + seconds/3600.0

def calculate_orb(longitude1: float, longitude2: float) -> float:
    """Calculate orb between two longitudes"""
    orb = abs(longitude1 - longitude2)
    if orb > 180:
        orb = 360 - orb
    return orb

def add_years_to_date(start_date: datetime.date, years: float) -> datetime.date:
    """Add fractional years to date with precision"""
    days = years * 365.25
    end_date = start_date + datetime.timedelta(days=int(days))
    
    # Handle fractional days
    fractional_days = days - int(days)
    if fractional_days >= 0.5:
        end_date += datetime.timedelta(days=1)
    
    return end_date

def calculate_years_between_dates(start_date: datetime.date, end_date: datetime.date) -> float:
    """Calculate precise years between two dates"""
    days_diff = (end_date - start_date).days
    return days_diff / 365.25

def save_json_data(data: Dict, filename: str, directory: str = "data") -> bool:
    """Save data to JSON file"""
    try:
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        return True
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")
        return False

def load_json_data(filename: str, directory: str = "data") -> Optional[Dict]:
    """Load data from JSON file"""
    try:
        filepath = os.path.join(directory, filename)
        
        if not os.path.exists(filepath):
            return None
        
        with open(filepath, 'r') as f:
            return json.load(f)
    
    except Exception as e:
        print(f"Error loading data from {filename}: {e}")
        return None

def format_date_for_display(date: datetime.date) -> str:
    """Format date for user-friendly display"""
    return date.strftime("%B %d, %Y")

def format_time_for_display(time: datetime.time) -> str:
    """Format time for user-friendly display"""
    return time.strftime("%I:%M %p")

def validate_birth_date(date_str: str) -> Optional[datetime.date]:
    """Validate and parse birth date string"""
    try:
        # Try different date formats
        formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d", "%m/%d/%Y"]
        
        for fmt in formats:
            try:
                return datetime.datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        
        return None
    except Exception:
        return None

def validate_birth_time(time_str: str) -> Optional[datetime.time]:
    """Validate and parse birth time string"""
    try:
        # Try different time formats
        formats = ["%H:%M", "%I:%M %p", "%H:%M:%S", "%I:%M:%S %p"]
        
        for fmt in formats:
            try:
                return datetime.datetime.strptime(time_str, fmt).time()
            except ValueError:
                continue
        
        return None
    except Exception:
        return None

def get_coordinates_for_city(city_name: str) -> tuple:
    """Get approximate coordinates for major cities"""
    city_coordinates = {
        'delhi': (28.6139, 77.2090),
        'mumbai': (19.0760, 72.8777),
        'bangalore': (12.9716, 77.5946),
        'chennai': (13.0827, 80.2707),
        'kolkata': (22.5726, 88.3639),
        'hyderabad': (17.3850, 78.4867),
        'pune': (18.5204, 73.8567),
        'ahmedabad': (23.0225, 72.5714),
        'jaipur': (26.9124, 75.7873),
        'lucknow': (26.8467, 80.9462),
        'kanpur': (26.4499, 80.3319),
        'nagpur': (21.1458, 79.0882),
        'indore': (22.7196, 75.8577),
        'thane': (19.2183, 72.9781),
        'bhopal': (23.2599, 77.4126),
        'visakhapatnam': (17.6868, 83.2185),
        'pimpri': (18.6298, 73.7997),
        'patna': (25.5941, 85.1376),
        'vadodara': (22.3072, 73.1812),
        'ghaziabad': (28.6692, 77.4538),
        'ludhiana': (30.9010, 75.8573),
        'agra': (27.1767, 78.0081),
        'nashik': (19.9975, 73.7898),
        'faridabad': (28.4089, 77.3178),
        'meerut': (28.9845, 77.7064),
        'rajkot': (22.3039, 70.8022),
        'kalyan': (19.2437, 73.1355),
        'vasai': (19.4911, 72.8054),
        'varanasi': (25.3176, 82.9739),
        'srinagar': (34.0837, 74.7973),
        'aurangabad': (19.8762, 75.3433),
        'dhanbad': (23.7957, 86.4304),
        'amritsar': (31.6340, 74.8723),
        'navi mumbai': (19.0330, 73.0297),
        'allahabad': (25.4358, 81.8463),
        'ranchi': (23.3441, 85.3096),
        'howrah': (22.5958, 88.2636),
        'coimbatore': (11.0168, 76.9558),
        'jabalpur': (23.1815, 79.9864),
        'gwalior': (26.2183, 78.1828),
        'vijayawada': (16.5062, 80.6480),
        'jodhpur': (26.2389, 73.0243),
        'madurai': (9.9252, 78.1198),
        'raipur': (21.2514, 81.6296),
        'kota': (25.2138, 75.8648),
        'chandigarh': (30.7333, 76.7794),
        'guwahati': (26.1445, 91.7362)
    }
    
    city_lower = city_name.lower().strip()
    return city_coordinates.get(city_lower, (28.6139, 77.2090))  # Default to Delhi

def create_directory_structure():
    """Create necessary directory structure"""
    directories = [
        'data',
        'outputs',
        'outputs/charts',
        'outputs/reports'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def get_weekday_info(date: datetime.date) -> Dict[str, str]:
    """Get weekday information for daily guidance"""
    weekday = date.strftime('%A')
    
    weekday_info = {
        'Monday': {
            'ruling_planet': 'Moon',
            'favorable_activities': 'Family time, emotional healing, water-related activities',
            'lucky_time': '7:00 PM - 8:30 PM',
            'mantra': 'Om Chandraya Namaha',
            'color': 'White'
        },
        'Tuesday': {
            'ruling_planet': 'Mars',
            'favorable_activities': 'Physical exercise, competitive activities, property matters',
            'lucky_time': '12:00 PM - 1:30 PM',
            'mantra': 'Om Mangalaya Namaha',
            'color': 'Red'
        },
        'Wednesday': {
            'ruling_planet': 'Mercury',
            'favorable_activities': 'Communication, business, travel, learning',
            'lucky_time': '10:00 AM - 11:30 AM',
            'mantra': 'Om Budhaya Namaha',
            'color': 'Green'
        },
        'Thursday': {
            'ruling_planet': 'Jupiter',
            'favorable_activities': 'Education, religious activities, financial planning',
            'lucky_time': '1:00 PM - 2:30 PM',
            'mantra': 'Om Gurave Namaha',
            'color': 'Yellow'
        },
        'Friday': {
            'ruling_planet': 'Venus',
            'favorable_activities': 'Relationships, artistic pursuits, beauty treatments',
            'lucky_time': '3:00 PM - 4:30 PM',
            'mantra': 'Om Shukraya Namaha',
            'color': 'White/Pink'
        },
        'Saturday': {
            'ruling_planet': 'Saturn',
            'favorable_activities': 'Long-term planning, discipline, ancestral work',
            'lucky_time': '5:00 AM - 6:30 AM',
            'mantra': 'Om Shanicharaya Namaha',
            'color': 'Black/Blue'
        },
        'Sunday': {
            'ruling_planet': 'Sun',
            'favorable_activities': 'Leadership activities, government work, spiritual practices',
            'lucky_time': '6:00 AM - 7:30 AM',
            'mantra': 'Om Suryaya Namaha',
            'color': 'Orange/Red'
        }
    }
    
    return weekday_info.get(weekday, weekday_info['Sunday'])

print("✅ Utility Helper Functions loaded")
