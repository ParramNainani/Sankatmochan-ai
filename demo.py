"""
Demo script to showcase Sankatmochan AI capabilities
"""

import datetime
from main import SankatmochanAI

def run_demo():
    """Run comprehensive demo of the system"""
    
    print("🧪 SANKATMOCHAN AI DEMO")
    print("Showcasing Advanced Vedic Astrology Capabilities")
    print("=" * 60)
    
    # Initialize AI
    ai = SankatmochanAI()
    
    # Demo with sample birth data
    print("\n1. Setting Demo Birth Details...")
    ai.set_birth_details(
        name="Demo User",
        birth_date=datetime.date(2006, 12, 13),
        birth_time=datetime.time(21, 35),
        place="Delhi, India"
    )
    
    # Show planetary positions
    print("\n2. Planetary Positions:")
    print("-" * 40)
    for planet, pos in ai.planetary_positions.items():
        retrograde = " (R)" if pos.retrograde else ""
        print(f"{planet:<12}: {pos.rashi} {pos.degree:02d}°{pos.minute:02d}' - {pos.nakshatra}{retrograde}")
    
    # Show current dasha
    print("\n3. Current Dasha Status:")
    print("-" * 40)
    if ai.current_dasha:
        print(f"Mahadasha: {ai.current_dasha['current_mahadasha']}")
        print(f"Remaining: {ai.current_dasha['remaining_years']:.1f} years")
        print(f"Completion: {ai.current_dasha['completion_percentage']:.1f}%")
    
    # Show detected patterns
    print(f"\n4. Detected Patterns ({len(ai.detected_patterns)}):")
    print("-" * 40)
    for i, pattern in enumerate(ai.detected_patterns[:3], 1):
        print(f"{i}. {pattern.pattern.name}")
        print(f"   Confidence: {pattern.confidence_score:.1%}")
        print(f"   Severity: {pattern.pattern.severity_level}/10")
    
    # Generate predictions
    print("\n5. Life Predictions (Next 6 Months):")
    print("-" * 40)
    predictions = ai.get_life_predictions(6)
    
    for i, pred in enumerate(predictions[:3], 1):
        print(f"\n{i}. {pred.event_type}")
        print(f"   Date: {pred.date.strftime('%B %Y')}")
        print(f"   Confidence: {pred.confidence_score:.1%}")
        print(f"   Description: {pred.description}")
        print(f"   Key Remedy: {pred.remedies[0] if pred.remedies else 'N/A'}")
    
    # Daily guidance
    print("\n6. Today's Guidance:")
    print("-" * 40)
    guidance = ai.get_daily_guidance()
    
    for key, value in guidance.items():
        if key not in ['date']:
            print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Create chart
    print("\n7. Creating Professional Chart...")
    try:
        chart_path = ai.create_professional_chart()
        print(f"✅ Chart created: {chart_path}")
    except Exception as e:
        print(f"❌ Chart creation failed: {e}")
    
    print("\n✅ DEMO COMPLETED SUCCESSFULLY!")
    print("🎯 Key Features Demonstrated:")
    print("   • Accurate planetary position calculations")
    print("   • Precise Vimshottari Dasha timing")
    print("   • Advanced pattern detection")
    print("   • High-confidence predictions")
    print("   • Professional chart generation")
    print("   • Daily astrological guidance")
    print("   • Comprehensive remedial measures")

if __name__ == "__main__":
    run_demo()
