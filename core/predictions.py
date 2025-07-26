"""
Core Prediction Engine
Generates astrological predictions based on dashas and patterns
"""

import datetime
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from core.calculations import PlanetPosition
from core.dashas import DashaPeriod
from core.patterns import PatternMatch

@dataclass
class AstroPrediction:
    """Astrological prediction data structure"""
    prediction_id: str
    date: datetime.date
    event_type: str
    description: str
    confidence_score: float
    accuracy_factors: Dict[str, float]
    supporting_patterns: List[str]
    dasha_factors: Dict[str, Any]
    remedies: List[str]
    user_confirmed: Optional[bool] = None
    actual_outcome: Optional[str] = None

class PredictionEngine:
    """Advanced prediction generation system"""
    
    def __init__(self):
        self.dasha_effects = self._initialize_dasha_effects()
        self.prediction_history = {}
        self.accuracy_metrics = {
            'total_predictions': 0,
            'confirmed_predictions': 0,
            'accuracy_rate': 0.0
        }
    
    def _initialize_dasha_effects(self) -> Dict[str, Dict]:
        """Initialize dasha effect database"""
        
        return {
            'Sun': {
                'event_type': 'Career Authority Enhancement',
                'description': 'Leadership opportunities and recognition in professional sphere',
                'confidence': 0.75,
                'effects': ['Career advancement', 'Leadership roles', 'Government recognition', 'Father-related matters']
            },
            'Moon': {
                'event_type': 'Emotional and Family Focus',
                'description': 'Increased attention to family matters and emotional well-being',
                'confidence': 0.72,
                'effects': ['Family harmony', 'Emotional growth', 'Home-related matters', 'Mother-related issues']
            },
            'Mars': {
                'event_type': 'Action and Achievement Period',
                'description': 'Time for bold actions and overcoming obstacles through determination',
                'confidence': 0.78,
                'effects': ['Goal achievement', 'Physical activities', 'Property matters', 'Competitive success']
            },
            'Mercury': {
                'event_type': 'Communication and Learning Phase',
                'description': 'Enhanced communication skills and learning opportunities',
                'confidence': 0.74,
                'effects': ['Business success', 'Communication skills', 'Learning opportunities', 'Travel']
            },
            'Jupiter': {
                'event_type': 'Wisdom and Expansion Period',
                'description': 'Spiritual growth, education, and expansion of knowledge',
                'confidence': 0.80,
                'effects': ['Spiritual growth', 'Educational success', 'Financial expansion', 'Religious activities']
            },
            'Venus': {
                'event_type': 'Relationship and Creative Focus',
                'description': 'Emphasis on relationships, creativity, and artistic pursuits',
                'confidence': 0.76,
                'effects': ['Relationship harmony', 'Creative success', 'Artistic pursuits', 'Luxury and comfort']
            },
            'Saturn': {
                'event_type': 'Discipline and Structure Building',
                'description': 'Period requiring discipline and long-term planning',
                'confidence': 0.77,
                'effects': ['Long-term success', 'Disciplined approach', 'Responsibility', 'Slow but steady progress']
            },
            'Rahu': {
                'event_type': 'Innovation and Worldly Success',
                'description': 'Unconventional opportunities and material advancement',
                'confidence': 0.73,
                'effects': ['Innovative opportunities', 'Foreign connections', 'Technology success', 'Unconventional gains']
            },
            'Ketu': {
                'event_type': 'Spiritual Detachment Phase',
                'description': 'Focus on spirituality and detachment from material concerns',
                'confidence': 0.71,
                'effects': ['Spiritual growth', 'Detachment', 'Research activities', 'Inner wisdom']
            }
        }
    
    def generate_dasha_based_predictions(self, current_dasha: Dict, 
                                       months_ahead: int = 12) -> List[AstroPrediction]:
        """Generate predictions based on current dasha"""
        
        predictions = []
        
        if not current_dasha or 'current_mahadasha' not in current_dasha:
            return predictions
        
        maha_lord = current_dasha['current_mahadasha']
        
        if maha_lord in self.dasha_effects:
            effect = self.dasha_effects[maha_lord]
            
            # Generate predictions for different time periods
            time_periods = [
                (30, 'Short-term'),
                (90, 'Medium-term'),
                (180, 'Long-term')
            ]
            
            for days_ahead, period_type in time_periods:
                if days_ahead <= months_ahead * 30:
                    prediction_date = datetime.date.today() + datetime.timedelta(days=days_ahead)
                    
                    prediction = AstroPrediction(
                        prediction_id=f"dasha_{maha_lord}_{prediction_date}_{period_type}",
                        date=prediction_date,
                        event_type=f"{period_type} {effect['event_type']}",
                        description=f"{effect['description']} - {period_type} manifestation",
                        confidence_score=effect['confidence'],
                        accuracy_factors={'dasha_based': 1.0, 'period_type': period_type},
                        supporting_patterns=[f"{maha_lord}_mahadasha"],
                        dasha_factors=current_dasha,
                        remedies=self._get_dasha_remedies(maha_lord)
                    )
                    
                    predictions.append(prediction)
        
        return predictions
    
    def generate_pattern_based_predictions(self, pattern_matches: List[PatternMatch]) -> List[AstroPrediction]:
        """Generate predictions based on detected patterns"""
        
        predictions = []
        
        for pattern_match in pattern_matches:
            if pattern_match.confidence_score > 0.7:
                
                prediction = AstroPrediction(
                    prediction_id=f"pattern_{pattern_match.pattern.pattern_id}_{pattern_match.match_date}",
                    date=pattern_match.match_date,
                    event_type=pattern_match.pattern.name,
                    description=pattern_match.pattern.description,
                    confidence_score=pattern_match.confidence_score,
                    accuracy_factors={
                        'pattern_accuracy': pattern_match.pattern.accuracy_score,
                        'orb_accuracy': (pattern_match.pattern.orb_tolerance - pattern_match.orb_accuracy) / pattern_match.pattern.orb_tolerance
                    },
                    supporting_patterns=[pattern_match.pattern.pattern_id],
                    dasha_factors={},
                    remedies=pattern_match.pattern.remedies.copy()
                )
                
                predictions.append(prediction)
        
        return predictions
    
    def generate_comprehensive_predictions(self, current_dasha: Dict, 
                                         pattern_matches: List[PatternMatch],
                                         months_ahead: int = 12) -> List[AstroPrediction]:
        """Generate comprehensive predictions combining all factors"""
        
        predictions = []
        
        # Dasha-based predictions
        dasha_predictions = self.generate_dasha_based_predictions(current_dasha, months_ahead)
        predictions.extend(dasha_predictions)
        
        # Pattern-based predictions
        pattern_predictions = self.generate_pattern_based_predictions(pattern_matches)
        predictions.extend(pattern_predictions)
        
        # Monthly general predictions
        monthly_predictions = self._generate_monthly_predictions(current_dasha, months_ahead)
        predictions.extend(monthly_predictions)
        
        # Sort by confidence and date
        predictions.sort(key=lambda x: (-x.confidence_score, x.date))
        
        return predictions[:10]  # Return top 10 predictions
    
    def _generate_monthly_predictions(self, current_dasha: Dict, months_ahead: int) -> List[AstroPrediction]:
        """Generate monthly predictions"""
        
        predictions = []
        
        if not current_dasha or 'current_mahadasha' not in current_dasha:
            return predictions
        
        maha_lord = current_dasha['current_mahadasha']
        
        for month in range(1, min(months_ahead + 1, 7)):
            prediction_date = datetime.date.today() + datetime.timedelta(days=30 * month)
            
            # Monthly themes based on dasha lord
            monthly_theme = self._get_monthly_theme(maha_lord, month)
            
            prediction = AstroPrediction(
                prediction_id=f"monthly_{maha_lord}_{prediction_date}",
                date=prediction_date,
                event_type=monthly_theme['event_type'],
                description=monthly_theme['description'],
                confidence_score=monthly_theme['confidence'],
                accuracy_factors={'monthly_prediction': 1.0},
                supporting_patterns=[f"{maha_lord}_monthly"],
                dasha_factors=current_dasha,
                remedies=self._get_monthly_remedies(maha_lord)
            )
            
            predictions.append(prediction)
        
        return predictions
    
    def _get_monthly_theme(self, dasha_lord: str, month: int) -> Dict:
        """Get monthly theme based on dasha lord and month"""
        
        base_effect = self.dasha_effects.get(dasha_lord, self.dasha_effects['Jupiter'])
        
        # Modify based on month
        monthly_modifiers = {
            1: {'confidence_modifier': 0.05, 'theme': 'New beginnings'},
            2: {'confidence_modifier': 0.0, 'theme': 'Development'},
            3: {'confidence_modifier': 0.03, 'theme': 'Growth'},
            4: {'confidence_modifier': 0.02, 'theme': 'Stability'},
            5: {'confidence_modifier': 0.04, 'theme': 'Expansion'},
            6: {'confidence_modifier': 0.01, 'theme': 'Consolidation'}
        }
        
        modifier = monthly_modifiers.get(month, {'confidence_modifier': 0.0, 'theme': 'Progress'})
        
        return {
            'event_type': f"{modifier['theme']} in {base_effect['event_type']}",
            'description': f"{base_effect['description']} with focus on {modifier['theme'].lower()}",
            'confidence': min(base_effect['confidence'] + modifier['confidence_modifier'], 1.0)
        }
    
    def _get_dasha_remedies(self, lord: str) -> List[str]:
        """Get remedies for dasha lord"""
        
        remedies_map = {
            'Sun': [
                "Chant Aditya Hridayam daily at sunrise",
                "Offer water to Sun every morning",
                "Donate wheat and jaggery on Sundays"
            ],
            'Moon': [
                "Chant 'Om Chandraya Namaha' 108 times daily",
                "Offer milk to Shiva on Mondays",
                "Practice meditation near water bodies"
            ],
            'Mars': [
                "Recite Hanuman Chalisa daily",
                "Donate red lentils on Tuesdays",
                "Practice physical exercise regularly"
            ],
            'Mercury': [
                "Chant 'Om Budhaya Namaha' daily",
                "Donate green items on Wednesdays",
                "Engage in learning and teaching"
            ],
            'Jupiter': [
                "Chant 'Om Gurave Namaha' daily",
                "Donate yellow items on Thursdays",
                "Practice charity and help teachers"
            ],
            'Venus': [
                "Chant 'Om Shukraya Namaha' daily",
                "Donate white items on Fridays",
                "Engage in artistic activities"
            ],
            'Saturn': [
                "Chant 'Om Shanicharaya Namaha' daily",
                "Donate black items on Saturdays",
                "Practice discipline and serve the needy"
            ],
            'Rahu': [
                "Chant 'Om Rahave Namaha' daily",
                "Donate multicolored items",
                "Practice meditation and charity"
            ],
            'Ketu': [
                "Chant 'Om Ketave Namaha' daily",
                "Donate spiritual items",
                "Practice spiritual disciplines"
            ]
        }
        
        return remedies_map.get(lord, ["Regular spiritual practice", "Meditation", "Charity"])
    
    def _get_monthly_remedies(self, lord: str) -> List[str]:
        """Get monthly remedies"""
        base_remedies = self._get_dasha_remedies(lord)
        return base_remedies[:2] + ["Daily prayer and positive thinking"]
    
    def track_prediction_accuracy(self, prediction_id: str, actual_outcome: str, 
                                accuracy_rating: float):
        """Track prediction accuracy for continuous improvement"""
        
        self.accuracy_metrics['total_predictions'] += 1
        
        if accuracy_rating > 0.5:
            self.accuracy_metrics['confirmed_predictions'] += 1
        
        self.accuracy_metrics['accuracy_rate'] = (
            self.accuracy_metrics['confirmed_predictions'] / 
            self.accuracy_metrics['total_predictions']
        ) * 100
    
    def get_accuracy_report(self) -> Dict[str, Any]:
        """Get prediction accuracy report"""
        
        return {
            'overall_accuracy': self.accuracy_metrics['accuracy_rate'],
            'total_predictions': self.accuracy_metrics['total_predictions'],
            'confirmed_predictions': self.accuracy_metrics['confirmed_predictions'],
            'improvement_suggestions': self._get_improvement_suggestions()
        }
    
    def _get_improvement_suggestions(self) -> List[str]:
        """Get suggestions for improving accuracy"""
        
        suggestions = []
        
        if self.accuracy_metrics['accuracy_rate'] < 80:
            suggestions.append("Focus on patterns with highest accuracy rates")
            suggestions.append("Collect more user feedback for validation")
            suggestions.append("Refine confidence scoring algorithms")
        
        if self.accuracy_metrics['total_predictions'] < 10:
            suggestions.append("Generate more predictions to improve statistical accuracy")
        
        return suggestions

print("✅ Core Prediction Engine loaded")
