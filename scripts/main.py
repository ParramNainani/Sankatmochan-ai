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
from core.interpretation import InterpretationEngine # <-- ADD THIS

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
        self.interpretation_engine = InterpretationEngine() # <-- ADD THIS
        
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

    # --- No changes to set_birth_details, get_life_predictions, get_daily_guidance, etc. ---
    
    def generate_comprehensive_report(self) -> str:
        """Generate comprehensive astrological report"""
        
        if not self.birth_data:
            return "Please set birth details first"
        
        report = []
        report.append("🕉 SANKATMOCHAN AI COMPREHENSIVE REPORT 🕉")
        report.append("=" * 70)
        
        # Personal Details
        report.append(f"\n📋 PERSONAL DETAILS:")
        # ... (this part is unchanged)
        
        # Planetary Positions
        report.append(f"\n🌟 PLANETARY POSITIONS:")
        # ... (this part is unchanged)

        # Current Dasha Analysis
        report.append(f"\n🎯 CURRENT DASHA ANALYSIS:")
        # ... (this part is unchanged)

        # *** NEW: Detailed Interpretation Section ***
        report.append(f"\n\n📜 DETAILED ANALYSIS:")
        report.append("-" * 70)

        # Personality
        personality_insights = self.interpretation_engine.analyze_personality(self.planetary_positions)
        report.append("\n**Personality Insights:**")
        for insight in personality_insights:
            report.append(f"- {insight}")

        # Career
        career_insights = self.interpretation_engine.analyze_career(self.planetary_positions)
        report.append("\n**Career Analysis:**")
        for insight in career_insights:
            report.append(f"- {insight}")

        # Relationships
        relationship_insights = self.interpretation_engine.analyze_relationships(self.planetary_positions)
        report.append("\n**Relationship Analysis:**")
        for insight in relationship_insights:
            report.append(f"- {insight}")
        
        # Detected Patterns
        if self.detected_patterns:
            report.append(f"\n🔍 DETECTED ASTROLOGICAL PATTERNS:")
            # ... (this part is unchanged)
        
        # Life Predictions
        predictions = self.get_life_predictions(12)
        report.append(f"\n🔮 LIFE PREDICTIONS (Next 12 Months):")
        # ... (this part is unchanged)
        
        # ... (rest of the function is unchanged)

        report_text = "\n".join(report)
        return report_text
    
    # --- No changes to other methods ---

if __name__ == "__main__":
    # This part can remain the same for interactive use
    pass