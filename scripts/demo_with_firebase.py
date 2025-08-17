"""
Demo script with Firebase integration
Showcases chart generation and Firebase storage
"""

import datetime
from scripts.main import SankatmochanAI

def run_firebase_demo():
    """Run demo with Firebase integration"""
    
    print("🔥 SANKATMOCHAN AI WITH FIREBASE INTEGRATION")
    print("Showcasing Chart Generation and Cloud Storage")
    print("=" * 70)
    
    # Initialize AI
    ai = SankatmochanAI()
    
    # Demo with sample birth data
    print("\n1. Setting Demo Birth Details...")
    ai.set_birth_details(
        name="Rahul Sharma",
        birth_date=datetime.date(1995, 8, 15),
        birth_time=datetime.time(14, 30),
        place="Mumbai, India"
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
    if ai.current_dasha and 'current_mahadasha' in ai.current_dasha:
        print(f"Mahadasha: {ai.current_dasha['current_mahadasha']}")
        print(f"Remaining: {ai.current_dasha['remaining_years']:.1f} years")
        print(f"Completion: {ai.current_dasha['completion_percentage']:.1f}%")
    
    # Create chart with Firebase upload
    print("\n4. Creating Professional Chart with Firebase Upload...")
    try:
        chart_path = ai.create_professional_chart(upload_to_firebase=True)
        print(f"✅ Chart created and uploaded: {chart_path}")
        
        # Show Firebase information if available
        if 'firebase_download_url' in ai.birth_data:
            print(f"\n📊 FIREBASE STORAGE INFORMATION:")
            print(f"   Person: {ai.birth_data['name']}")
            print(f"   Birth Date: {ai.birth_data['birth_date']}")
            print(f"   Birth Time: {ai.birth_data['birth_time']}")
            print(f"   Birth Place: {ai.birth_data['place']}")
            print(f"   Chart URL: {ai.birth_data['firebase_download_url']}")
            print(f"   Document ID: {ai.birth_data['firebase_document_id']}")
            print(f"   Storage Path: {ai.birth_data['firebase_storage_path']}")
        
    except Exception as e:
        print(f"❌ Chart creation failed: {e}")
    
    # Test Firebase retrieval if available
    if ai.firebase_service:
        print("\n5. Testing Firebase Retrieval...")
        try:
            charts = ai.firebase_service.get_all_birth_charts()
            print(f"✅ Found {len(charts)} charts in Firebase")
            
            if charts:
                latest_chart = charts[0]
                print(f"   Latest: {latest_chart.get('person_name', 'Unknown')}")
                print(f"   Created: {latest_chart.get('created_at', 'Unknown')}")
            
        except Exception as e:
            print(f"⚠️ Firebase retrieval failed: {e}")
    
    print("\n✅ FIREBASE DEMO COMPLETED SUCCESSFULLY!")
    print("🎯 Key Features Demonstrated:")
    print("   • Professional chart generation")
    print("   • Firebase Storage integration")
    print("   • Firestore metadata storage")
    print("   • Cloud-based chart retrieval")
    print("   • Complete birth chart management")

def run_multiple_charts_demo():
    """Run demo with multiple charts to test Firebase storage"""
    
    print("\n" + "=" * 70)
    print("📚 MULTIPLE CHARTS DEMO - Testing Firebase Storage")
    print("=" * 70)
    
    # Sample data for multiple charts
    sample_data = [
        {
            'name': 'Priya Patel',
            'birth_date': datetime.date(1990, 3, 22),
            'birth_time': datetime.time(9, 15),
            'place': 'Delhi, India'
        },
        {
            'name': 'Amit Kumar',
            'birth_date': datetime.date(1988, 11, 8),
            'birth_time': datetime.time(18, 45),
            'place': 'Bangalore, India'
        },
        {
            'name': 'Neha Singh',
            'birth_date': datetime.date(1992, 7, 14),
            'birth_time': datetime.time(12, 30),
            'place': 'Chennai, India'
        }
    ]
    
    ai = SankatmochanAI()
    
    for i, data in enumerate(sample_data, 1):
        print(f"\n{i}. Creating chart for {data['name']}...")
        
        try:
            ai.set_birth_details(**data)
            chart_path = ai.create_professional_chart(upload_to_firebase=True)
            print(f"   ✅ Chart created and uploaded successfully")
            
        except Exception as e:
            print(f"   ❌ Failed: {e}")
    
    # Show all charts in Firebase
    if ai.firebase_service:
        print(f"\n📊 ALL CHARTS IN FIREBASE:")
        try:
            charts = ai.firebase_service.get_all_birth_charts()
            for i, chart in enumerate(charts, 1):
                print(f"{i}. {chart.get('person_name', 'Unknown')} - {chart.get('birth_date', 'Unknown')}")
        except Exception as e:
            print(f"⚠️ Failed to retrieve charts: {e}")

if __name__ == "__main__":
    run_firebase_demo()
    run_multiple_charts_demo() 