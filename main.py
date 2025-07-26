"""
Main Sankatmochan AI System
Structured modular approach with all components integrated
"""

import datetime
import os
from typing import Dict, List, Optional

# Core imports
from core.calculations import AstronomicalCalculator, PlanetPosition
from core.dashas import DashaCalculator, DashaPeriod
from core.patterns import PatternDetector, PatternMatch
from core.predictions import PredictionEngine, AstroPrediction
from core.chart_visualizer import VedicChartVisualizer

# Utility imports
from utils.helpers import (
    save_json_data, load_json_data, validate_birth_date, validate_birth_time,
    get_coordinates_for_city, create_directory_structure, format_date_for_display,
    format_time_for_display, get_weekday_info
)
from utils.constants import NAKSHATRA_NAMES, RASHI_NAMES, PLANETARY_REMEDIES

class SankatmochanAI:
    """Main Sankatmochan AI System - Structured and Modular"""
    
    def __init__(self):
        # Initialize core components
        self.astro_calc = AstronomicalCalculator()
        self.dasha_calc = DashaCalculator()
        self.pattern_detector = PatternDetector()
        self.prediction_engine = PredictionEngine()
        self.chart_visualizer = VedicChartVisualizer()
        
        # Initialize data storage
        self.birth_data = {}
        self.planetary_positions = {}
        self.dasha_periods = []
        self.current_dasha = {}
        self.detected_patterns = []
        
        # Create directory structure
        create_directory_structure()
        
        # Load existing data
        self._load_user_data()
    
    def set_birth_details(self, name: str, birth_date: datetime.date, birth_time: datetime.time,
                         place: str, latitude: Optional[float] = None, longitude: Optional[float] = None):
        """Set birth details and perform all calculations"""
        
        print(f"🕉 Setting birth details for {name}")
        
        # Get coordinates if not provided
        if latitude is None or longitude is None:
            latitude, longitude = get_coordinates_for_city(place)
        
        self.birth_data = {
            'name': name,
            'birth_date': birth_date,
            'birth_time': birth_time,
            'place': place,
            'latitude': latitude,
            'longitude': longitude,
            'created_at': datetime.datetime.now().isoformat()
        }
        
        # Calculate planetary positions
        print("🎯 Calculating planetary positions...")
        self.planetary_positions = self.astro_calc.calculate_planetary_positions(
            birth_date, birth_time, latitude, longitude
        )
        
        # Get birth nakshatra for dasha calculation
        moon_pos = self.planetary_positions.get('Moon')
        if moon_pos:
            birth_nakshatra = moon_pos.nakshatra
            # Calculate elapsed portion in nakshatra
            nakshatra_start = (moon_pos.longitude // (360/27)) * (360/27)
            elapsed_portion = (moon_pos.longitude - nakshatra_start) / (360/27)
            
            self.birth_data['birth_nakshatra'] = birth_nakshatra
            self.birth_data['nakshatra_elapsed'] = elapsed_portion
        
        # Calculate Vimshottari Dasha
        print("🎯 Calculating Vimshottari Dasha...")
        if 'birth_nakshatra' in self.birth_data:
            self.dasha_periods = self.dasha_calc.calculate_vimshottari_dasha(
                self.birth_data['birth_nakshatra'],
                self.birth_data['nakshatra_elapsed'],
                birth_date
            )
            
            # Get current dasha info
            self.current_dasha = self.dasha_calc.get_current_dasha_info(birth_date)
        
        # Detect patterns in birth chart
        print("🔍 Detecting astrological patterns...")
        self.detected_patterns = self.pattern_detector.detect_patterns_in_chart(
            self.planetary_positions
        )
        
        # Save user data
        self._save_user_data()
        
        print(f"✅ Birth details set successfully!")
        print(f"Birth Nakshatra: {self.birth_data.get('birth_nakshatra', 'N/A')}")
        if self.current_dasha:
            current_lord = self.current_dasha.get('current_mahadasha', 'Unknown')
            remaining_years = self.current_dasha.get('remaining_years', 0)
            print(f"Current Mahadasha: {current_lord} ({remaining_years:.1f} years remaining)")
        
        if self.detected_patterns:
            print(f"Detected {len(self.detected_patterns)} astrological patterns")
    
    def get_life_predictions(self, months_ahead: int = 12) -> List[AstroPrediction]:
        """Generate comprehensive life predictions"""
        
        if not self.birth_data:
            raise ValueError("Please set birth details first")
        
        print(f"🔮 Generating predictions for next {months_ahead} months...")
        
        # Generate comprehensive predictions
        predictions = self.prediction_engine.generate_comprehensive_predictions(
            self.current_dasha,
            self.detected_patterns,
            months_ahead
        )
        
        return predictions
    
    def get_daily_guidance(self, date: Optional[datetime.date] = None) -> Dict[str, str]:
        """Get daily astrological guidance"""
        
        if date is None:
            date = datetime.date.today()
        
        # Get weekday information
        weekday_info = get_weekday_info(date)
        
        # Get current dasha lord
        current_lord = self.current_dasha.get('current_mahadasha', 'Jupiter')
        
        guidance = {
            'date': format_date_for_display(date),
            'weekday': date.strftime('%A'),
            'ruling_planet': weekday_info['ruling_planet'],
            'overall_energy': f"Today's energy is influenced by {current_lord} Mahadasha and {weekday_info['ruling_planet']} (weekday ruler)",
            'favorable_activities': weekday_info['favorable_activities'],
            'lucky_time': weekday_info['lucky_time'],
            'favorable_color': weekday_info['color'],
            'daily_mantra': weekday_info['mantra'],
            'spiritual_practice': f"Chant mantras for {current_lord} and practice meditation",
            'caution': "Avoid negative thoughts and maintain positive attitude"
        }
        
        return guidance
    
    def create_professional_chart(self, save_path: Optional[str] = None) -> str:
        """Create professional Vedic astrology chart"""
        
        if not self.planetary_positions:
            raise ValueError("Please set birth details first")
        
        print("🎨 Creating professional chart...")
        
        chart_path = self.chart_visualizer.create_professional_chart(
            self.planetary_positions,
            self.birth_data,
            self.current_dasha,
            save_path
        )
        
        print(f"✅ Professional chart created: {chart_path}")
        return chart_path
    
    def generate_comprehensive_report(self) -> str:
        """Generate comprehensive astrological report"""
        
        if not self.birth_data:
            return "Please set birth details first"
        
        report = []
        report.append("🕉 SANKATMOCHAN AI COMPREHENSIVE REPORT 🕉")
        report.append("=" * 70)
        
        # Personal Details
        report.append(f"\n📋 PERSONAL DETAILS:")
        report.append(f"Name: {self.birth_data['name']}")
        report.append(f"Birth Date: {format_date_for_display(self.birth_data['birth_date'])}")
        report.append(f"Birth Time: {format_time_for_display(self.birth_data['birth_time'])}")
        report.append(f"Birth Place: {self.birth_data['place']}")
        report.append(f"Coordinates: {self.birth_data['latitude']:.2f}°N, {self.birth_data['longitude']:.2f}°E")
        report.append(f"Birth Nakshatra: {self.birth_data.get('birth_nakshatra', 'N/A')}")
        
        # Planetary Positions
        report.append(f"\n🌟 PLANETARY POSITIONS:")
        report.append(f"{'Planet':<12} {'Rashi':<12} {'Degree':<12} {'Nakshatra':<15} {'House':<6}")
        report.append("-" * 70)
        
        planet_order = ['Ascendant', 'Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Rahu', 'Ketu']
        for planet in planet_order:
            if planet in self.planetary_positions:
                pos = self.planetary_positions[planet]
                degree_str = f"{pos.degree:02d}°{pos.minute:02d}'"
                retrograde_mark = " (R)" if pos.retrograde else ""
                
                report.append(f"{planet + retrograde_mark:<12} {pos.rashi:<12} {degree_str:<12} {pos.nakshatra:<15} {pos.house:<6}")
        
        # Current Dasha Analysis
        report.append(f"\n🎯 CURRENT DASHA ANALYSIS:")
        if self.current_dasha:
            report.append(f"Current Mahadasha: {self.current_dasha['current_mahadasha']}")
            report.append(f"Started: {format_date_for_display(self.current_dasha['start_date'])}")
            report.append(f"Ends: {format_date_for_display(self.current_dasha['end_date'])}")
            report.append(f"Remaining: {self.current_dasha['remaining_years']:.1f} years")
            report.append(f"Completion: {self.current_dasha['completion_percentage']:.1f}%")
        
        # Detected Patterns
        if self.detected_patterns:
            report.append(f"\n🔍 DETECTED ASTROLOGICAL PATTERNS:")
            for i, pattern in enumerate(self.detected_patterns[:5], 1):
                report.append(f"\n{i}. {pattern.pattern.name}")
                report.append(f"   Confidence: {pattern.confidence_score:.1%}")
                report.append(f"   Description: {pattern.pattern.description}")
                report.append(f"   Severity: {pattern.pattern.severity_level}/10")
                report.append(f"   Key Effects: {', '.join(pattern.pattern.typical_effects[:3])}")
                report.append(f"   Remedies:")
                for remedy in pattern.pattern.remedies[:2]:
                    report.append(f"     • {remedy}")
        
        # Life Predictions
        predictions = self.get_life_predictions(12)
        report.append(f"\n🔮 LIFE PREDICTIONS (Next 12 Months):")
        for i, pred in enumerate(predictions[:6], 1):
            report.append(f"\n{i}. {pred.event_type}")
            report.append(f"   Date: {format_date_for_display(pred.date)}")
            report.append(f"   Confidence: {pred.confidence_score:.0%}")
            report.append(f"   Description: {pred.description}")
            report.append(f"   Key Remedies:")
            for remedy in pred.remedies[:2]:
                report.append(f"     • {remedy}")
        
        # Daily Guidance
        daily_guidance = self.get_daily_guidance()
        report.append(f"\n📅 TODAY'S GUIDANCE:")
        for key, value in daily_guidance.items():
            if key != 'date':
                report.append(f"{key.replace('_', ' ').title()}: {value}")
        
        # Remedial Measures
        current_lord = self.current_dasha.get('current_mahadasha', 'Jupiter')
        if current_lord in PLANETARY_REMEDIES:
            report.append(f"\n💊 RECOMMENDED REMEDIES FOR {current_lord.upper()} MAHADASHA:")
            for remedy in PLANETARY_REMEDIES[current_lord]:
                report.append(f"• {remedy}")
        
        report.append(f"\n🕉 May divine blessings guide your path! 🕉")
        report.append(f"\nReport generated on: {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
        
        # Save report
        report_text = "\n".join(report)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"outputs/reports/comprehensive_report_{timestamp}.txt"
        
        try:
            with open(report_filename, 'w', encoding='utf-8') as f:
                f.write(report_text)
            print(f"📄 Report saved as: {report_filename}")
        except Exception as e:
            print(f"Error saving report: {e}")
        
        return report_text
    
    def _save_user_data(self):
        """Save user data to file"""
        
        user_data = {
            'birth_data': self.birth_data,
            'last_updated': datetime.datetime.now().isoformat()
        }
        
        # Convert date objects to strings for JSON serialization
        if 'birth_date' in user_data['birth_data']:
            user_data['birth_data']['birth_date'] = user_data['birth_data']['birth_date'].isoformat()
        if 'birth_time' in user_data['birth_data']:
            user_data['birth_data']['birth_time'] = user_data['birth_data']['birth_time'].isoformat()
        
        save_json_data(user_data, 'current_user.json')
    
    def _load_user_data(self):
        """Load user data from file"""
        
        user_data = load_json_data('current_user.json')
        
        if user_data and 'birth_data' in user_data:
            self.birth_data = user_data['birth_data']
            
            # Convert string dates back to date objects
            if 'birth_date' in self.birth_data:
                self.birth_data['birth_date'] = datetime.date.fromisoformat(self.birth_data['birth_date'])
            if 'birth_time' in self.birth_data:
                self.birth_data['birth_time'] = datetime.time.fromisoformat(self.birth_data['birth_time'])

def interactive_main():
    """Interactive main function"""
    
    print("🕉 WELCOME TO SANKATMOCHAN AI 🕉")
    print("Advanced Vedic Astrology Prediction System")
    print("=" * 60)
    
    # Initialize AI
    ai = SankatmochanAI()
    
    while True:
        print("\n📋 MAIN MENU:")
        print("1. Set Birth Details")
        print("2. Generate Life Predictions")
        print("3. Get Daily Guidance")
        print("4. Create Professional Chart")
        print("5. Generate Comprehensive Report")
        print("6. View Current Status")
        print("7. Exit")
        
        choice = input("\nSelect option (1-7): ").strip()
        
        if choice == '1':
            # Set birth details
            print("\n📝 Enter Birth Details:")
            
            name = input("Full Name: ").strip()
            
            # Birth date
            while True:
                date_str = input("Birth Date (DD/MM/YYYY): ").strip()
                birth_date = validate_birth_date(date_str)
                if birth_date:
                    break
                print("Invalid date format. Please use DD/MM/YYYY")
            
            # Birth time
            while True:
                time_str = input("Birth Time (HH:MM in 24-hour format): ").strip()
                birth_time = validate_birth_time(time_str)
                if birth_time:
                    break
                print("Invalid time format. Please use HH:MM")
            
            place = input("Birth Place: ").strip()
            
            # Optional coordinates
            use_coords = input("Enter custom coordinates? (y/n): ").lower().strip()
            if use_coords == 'y':
                try:
                    latitude = float(input("Latitude: "))
                    longitude = float(input("Longitude: "))
                    ai.set_birth_details(name, birth_date, birth_time, place, latitude, longitude)
                except ValueError:
                    print("Invalid coordinates. Using city-based coordinates.")
                    ai.set_birth_details(name, birth_date, birth_time, place)
            else:
                ai.set_birth_details(name, birth_date, birth_time, place)
        
        elif choice == '2':
            # Generate predictions
            if not ai.birth_data:
                print("❌ Please set birth details first")
                continue
            
            try:
                months = int(input("Months ahead to predict (1-24): "))
                months = max(1, min(24, months))
                
                predictions = ai.get_life_predictions(months)
                
                print(f"\n🔮 LIFE PREDICTIONS (Next {months} Months)")
                print("=" * 60)
                
                for i, pred in enumerate(predictions, 1):
                    print(f"\n{i}. {pred.event_type}")
                    print(f"   📅 Date: {format_date_for_display(pred.date)}")
                    print(f"   🎯 Confidence: {pred.confidence_score:.1%}")
                    print(f"   📝 Description: {pred.description}")
                    print(f"   💊 Key Remedies:")
                    for remedy in pred.remedies[:2]:
                        print(f"     • {remedy}")
                
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
        
        elif choice == '3':
            # Daily guidance
            guidance = ai.get_daily_guidance()
            
            print(f"\n📅 DAILY GUIDANCE - {guidance['date']}")
            print("=" * 50)
            
            for key, value in guidance.items():
                if key != 'date':
                    print(f"{key.replace('_', ' ').title()}: {value}")
        
        elif choice == '4':
            # Create chart
            if not ai.planetary_positions:
                print("❌ Please set birth details first")
                continue
            
            try:
                chart_path = ai.create_professional_chart()
                print(f"✅ Professional chart created: {chart_path}")
            except Exception as e:
                print(f"❌ Chart creation failed: {e}")
        
        elif choice == '5':
            # Generate report
            if not ai.birth_data:
                print("❌ Please set birth details first")
                continue
            
            print("\n📄 Generating comprehensive report...")
            report = ai.generate_comprehensive_report()
            
            # Display first part of report
            lines = report.split('\n')
            for line in lines[:30]:  # Show first 30 lines
                print(line)
            
            if len(lines) > 30:
                print(f"\n... (Report continues for {len(lines) - 30} more lines)")
                print("Full report saved to file.")
        
        elif choice == '6':
            # View current status
            if not ai.birth_data:
                print("❌ No birth details set")
                continue
            
            print(f"\n📊 CURRENT STATUS")
            print("=" * 40)
            print(f"Name: {ai.birth_data['name']}")
            print(f"Birth Date: {format_date_for_display(ai.birth_data['birth_date'])}")
            print(f"Birth Place: {ai.birth_data['place']}")
            print(f"Birth Nakshatra: {ai.birth_data.get('birth_nakshatra', 'N/A')}")
            
            if ai.current_dasha:
                print(f"Current Dasha: {ai.current_dasha['current_mahadasha']}")
                print(f"Remaining: {ai.current_dasha['remaining_years']:.1f} years")
            
            print(f"Detected Patterns: {len(ai.detected_patterns)}")
            print(f"Planetary Positions: {len(ai.planetary_positions)} calculated")
        
        elif choice == '7':
            print("\n🙏 Thank you for using Sankatmochan AI!")
            print("May divine blessings guide your path! 🕉")
            break
        
        else:
            print("❌ Invalid option. Please select 1-7.")

if __name__ == "__main__":
    interactive_main()
