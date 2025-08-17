"""
Core Interpretation Engine
Analyzes birth charts to generate insights on personality, life events, and more.
"""

from typing import Dict, List
from core.calculations import PlanetPosition

class InterpretationEngine:
    """Generates detailed interpretations of a Vedic birth chart."""

    def get_planet_strength(self, planet: str, position: PlanetPosition) -> str:
        """Determines the strength of a planet based on its sign."""
        # This is a simplified placeholder. You can add detailed rules here.
        # Example rules:
        if planet == "Sun" and position.rashi == "Aries":
            return "Exalted (Very Strong)"
        if planet == "Moon" and position.rashi == "Taurus":
            return "Exalted (Very Strong)"
        # Add more rules for debilitation, mooltrikona, own house etc.
        return "Neutral"

    def analyze_personality(self, positions: Dict[str, PlanetPosition]) -> List[str]:
        """Provides a personality analysis based on the Ascendant and Moon."""
        insights = []
        ascendant = positions.get("Ascendant")
        moon = positions.get("Moon")

        if ascendant:
            insights.append(f"Your Ascendant in {ascendant.rashi} gives you a core personality that is energetic and pioneering.")
        if moon:
            insights.append(f"Your Moon in {moon.rashi} indicates your mind is analytical, practical, and detail-oriented.")
        
        return insights

    def analyze_career(self, positions: Dict[str, PlanetPosition]) -> List[str]:
        """Analyzes career prospects from the 10th house."""
        insights = []
        house_10_planets = [p for p, pos in positions.items() if pos.house == 10]
        
        if house_10_planets:
            for planet in house_10_planets:
                 insights.append(f"{planet} in your 10th house of career indicates a profession related to leadership and authority.")
        else:
            insights.append("With an empty 10th house, your career is more influenced by the lord of the 10th house and its placement.")
            
        return insights

    def analyze_relationships(self, positions: Dict[str, PlanetPosition]) -> List[str]:
        """Analyzes relationship and marriage prospects from the 7th house."""
        insights = []
        house_7_planets = [p for p, pos in positions.items() if pos.house == 7]
        
        if house_7_planets:
            for planet in house_7_planets:
                insights.append(f"The presence of {planet} in your 7th house of partnership brings intensity and transformation to your relationships.")
        else:
            insights.append("Your 7th house is unoccupied, suggesting that partnerships will be strongly influenced by the 7th lord and transiting planets.")
            
        return insights