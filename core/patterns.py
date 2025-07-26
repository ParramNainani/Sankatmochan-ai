"""
Core Pattern Detection
Identifies astrological patterns and their effects
"""

import datetime
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from core.calculations import PlanetPosition

@dataclass
class AstroPattern:
    """Astrological pattern data structure"""
    pattern_id: str
    name: str
    description: str
    planets_involved: List[str]
    orb_tolerance: float
    severity_level: int
    typical_effects: List[str]
    remedies: List[str]
    confirmed_count: int
    accuracy_score: float

@dataclass
class PatternMatch:
    """Pattern match instance"""
    pattern: AstroPattern
    match_date: datetime.date
    exact_degrees: Dict[str, float]
    orb_accuracy: float
    confidence_score: float
    predicted_effects: List[str]

class PatternDetector:
    """Advanced pattern detection system"""
    
    def __init__(self):
        self.patterns = self._initialize_patterns()
    
    def _initialize_patterns(self) -> Dict[str, AstroPattern]:
        """Initialize pattern database"""
        
        patterns = {}
        
        # Rahu-Sun conjunction
        patterns['rahu_sun_conjunction'] = AstroPattern(
            pattern_id='rahu_sun_conjunction',
            name='Rahu-Sun Conjunction',
            description='Conjunction causing ego conflicts and authority issues',
            planets_involved=['Rahu', 'Sun'],
            orb_tolerance=6.0,
            severity_level=9,
            typical_effects=[
                'Authority conflicts', 'Ego issues', 'Government problems',
                'Father-related issues', 'Career obstacles', 'Health problems'
            ],
            remedies=[
                'Chant Aditya Hridayam daily',
                'Offer water to Sun every morning',
                'Donate copper items on Sundays',
                'Avoid conflicts with authority figures'
            ],
            confirmed_count=0,
            accuracy_score=0.0
        )
        
        # Mars-Saturn conjunction
        patterns['mars_saturn_conjunction'] = AstroPattern(
            pattern_id='mars_saturn_conjunction',
            name='Mars-Saturn Conjunction',
            description='Conjunction causing delays, accidents, and frustrations',
            planets_involved=['Mars', 'Saturn'],
            orb_tolerance=6.0,
            severity_level=8,
            typical_effects=[
                'Accidents', 'Delays in projects', 'Frustration', 'Legal issues',
                'Property disputes', 'Bone/muscle problems'
            ],
            remedies=[
                'Recite Hanuman Chalisa daily',
                'Donate iron items on Tuesdays',
                'Avoid risky activities',
                'Practice patience and discipline'
            ],
            confirmed_count=0,
            accuracy_score=0.0
        )
        
        # Ketu-Moon conjunction
        patterns['ketu_moon_conjunction'] = AstroPattern(
            pattern_id='ketu_moon_conjunction',
            name='Ketu-Moon Conjunction',
            description='Conjunction causing mental stress and emotional instability',
            planets_involved=['Ketu', 'Moon'],
            orb_tolerance=4.0,
            severity_level=7,
            typical_effects=[
                'Mental stress', 'Emotional instability', 'Depression',
                'Family problems', 'Mother-related issues', 'Sleep disorders'
            ],
            remedies=[
                'Chant Mahamrityunjaya Mantra',
                'Worship Goddess Durga',
                'Practice meditation',
                'Maintain emotional balance'
            ],
            confirmed_count=0,
            accuracy_score=0.0
        )
        
        # Rahu-Mars conjunction (Angarak Yoga)
        patterns['rahu_mars_conjunction'] = AstroPattern(
            pattern_id='rahu_mars_conjunction',
            name='Rahu-Mars Conjunction (Angarak Yoga)',
            description='Dangerous conjunction causing accidents and violence',
            planets_involved=['Rahu', 'Mars'],
            orb_tolerance=6.0,
            severity_level=9,
            typical_effects=[
                'Accidents', 'Violence', 'Explosions', 'Surgery',
                'Blood-related issues', 'Aggressive behavior'
            ],
            remedies=[
                'Recite Hanuman Chalisa 108 times daily',
                'Donate red items on Tuesdays',
                'Avoid aggressive behavior',
                'Practice anger management'
            ],
            confirmed_count=0,
            accuracy_score=0.0
        )
        
        return patterns
    
    def detect_patterns_in_chart(self, planetary_positions: Dict[str, PlanetPosition]) -> List[PatternMatch]:
        """Detect patterns in birth chart"""
        
        pattern_matches = []
        
        for pattern_id, pattern in self.patterns.items():
            matches = self._check_conjunction_pattern(pattern, planetary_positions)
            pattern_matches.extend(matches)
        
        return pattern_matches
    
    def detect_transit_patterns(self, transit_positions: Dict[str, PlanetPosition],
                              birth_positions: Dict[str, PlanetPosition],
                              start_date: datetime.date, end_date: datetime.date) -> List[PatternMatch]:
        """Detect patterns in transit period"""
        
        pattern_matches = []
        current_date = start_date
        
        while current_date <= end_date:
            # Check transit conjunctions
            for pattern_id, pattern in self.patterns.items():
                matches = self._check_conjunction_pattern(pattern, transit_positions, current_date)
                pattern_matches.extend(matches)
            
            current_date += datetime.timedelta(days=1)
        
        return pattern_matches
    
    def _check_conjunction_pattern(self, pattern: AstroPattern, 
                                 positions: Dict[str, PlanetPosition],
                                 date: datetime.date = None) -> List[PatternMatch]:
        """Check conjunction pattern matches"""
        
        matches = []
        
        if len(pattern.planets_involved) == 2:
            planet1, planet2 = pattern.planets_involved
            
            if planet1 in positions and planet2 in positions:
                pos1, pos2 = positions[planet1], positions[planet2]
                
                # Calculate orb
                orb = abs(pos1.longitude - pos2.longitude)
                if orb > 180:
                    orb = 360 - orb
                
                if orb <= pattern.orb_tolerance:
                    confidence = self._calculate_confidence_score(pattern, orb)
                    
                    if confidence > 0.6:
                        match = PatternMatch(
                            pattern=pattern,
                            match_date=date or datetime.date.today(),
                            exact_degrees={planet1: pos1.longitude, planet2: pos2.longitude},
                            orb_accuracy=orb,
                            confidence_score=confidence,
                            predicted_effects=pattern.typical_effects.copy()
                        )
                        matches.append(match)
        
        return matches
    
    def _calculate_confidence_score(self, pattern: AstroPattern, orb: float) -> float:
        """Calculate confidence score for pattern match"""
        
        # Base confidence from orb accuracy
        orb_confidence = (pattern.orb_tolerance - orb) / pattern.orb_tolerance
        
        # Historical accuracy bonus
        accuracy_bonus = pattern.accuracy_score * 0.1
        
        # User confirmation bonus
        confirmation_bonus = min(pattern.confirmed_count * 0.05, 0.2)
        
        total_confidence = orb_confidence + accuracy_bonus + confirmation_bonus
        
        return min(total_confidence, 1.0)
    
    def update_pattern_accuracy(self, pattern_id: str, confirmed: bool, effect_count: float):
        """Update pattern accuracy based on user feedback"""
        
        if pattern_id in self.patterns:
            pattern = self.patterns[pattern_id]
            
            if confirmed:
                pattern.confirmed_count += 1
                total_predictions = pattern.confirmed_count
                if total_predictions > 0:
                    pattern.accuracy_score = (pattern.accuracy_score * (total_predictions - 1) + effect_count) / total_predictions
            else:
                # Decrease accuracy for false positives
                total_predictions = pattern.confirmed_count + 1
                pattern.accuracy_score = (pattern.accuracy_score * (total_predictions - 1)) / total_predictions
            
            # Ensure accuracy score stays within bounds
            pattern.accuracy_score = max(0.0, min(1.0, pattern.accuracy_score))
    
    def get_pattern_statistics(self) -> Dict[str, Any]:
        """Get pattern accuracy statistics"""
        
        stats = {
            'total_patterns': len(self.patterns),
            'confirmed_patterns': 0,
            'average_accuracy': 0.0,
            'pattern_details': {}
        }
        
        accuracies = []
        for pattern_id, pattern in self.patterns.items():
            if pattern.confirmed_count > 0:
                stats['confirmed_patterns'] += 1
                accuracies.append(pattern.accuracy_score)
            
            stats['pattern_details'][pattern_id] = {
                'name': pattern.name,
                'confirmed_count': pattern.confirmed_count,
                'accuracy_score': pattern.accuracy_score,
                'severity': pattern.severity_level
            }
        
        if accuracies:
            stats['average_accuracy'] = sum(accuracies) / len(accuracies)
        
        return stats

print("✅ Core Pattern Detection loaded")
