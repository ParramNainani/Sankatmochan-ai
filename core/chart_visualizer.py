"""
Professional Chart Visualizer
Creates traditional Vedic astrology charts
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import datetime
from typing import Dict, List
from core.calculations import PlanetPosition

class VedicChartVisualizer:
    """Professional Vedic astrology chart creator"""
    
    def __init__(self):
        self.planet_symbols = {
            'Sun': 'Su', 'Moon': 'Mo', 'Mars': 'Ma', 'Mercury': 'Me',
            'Jupiter': 'Ju', 'Venus': 'Ve', 'Saturn': 'Sa',
            'Rahu': 'Ra', 'Ketu': 'Ke', 'Ascendant': 'As'
        }
        
        self.house_colors = {
            1: '#FFE6E6', 2: '#E6F3FF', 3: '#E6FFE6', 4: '#FFFFE6',
            5: '#F3E6FF', 6: '#FFE6F3', 7: '#E6FFFF', 8: '#FFF0E6',
            9: '#F0FFE6', 10: '#E6F0FF', 11: '#FFE6F0', 12: '#F0E6FF'
        }
    
    def create_professional_chart(self, planetary_positions: Dict[str, PlanetPosition],
                                birth_data: Dict, current_dasha: Dict,
                                save_path: str = None) -> str:
        """Create professional Vedic chart"""
        
        fig = plt.figure(figsize=(16, 12))
        
        # Create layout
        gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1], hspace=0.3, wspace=0.2)
        
        # Main chart
        ax_chart = fig.add_subplot(gs[0, :])
        self._draw_lagna_chart(ax_chart, planetary_positions)
        
        # Planetary data table
        ax_table = fig.add_subplot(gs[1, 0])
        self._draw_planetary_table(ax_table, planetary_positions)
        
        # Dasha information
        ax_dasha = fig.add_subplot(gs[1, 1])
        self._draw_dasha_info(ax_dasha, current_dasha)
        
        # Birth details
        ax_birth = fig.add_subplot(gs[2, :])
        self._draw_birth_details(ax_birth, birth_data)
        
        plt.suptitle('🕉 Professional Vedic Astrology Chart 🕉', 
                    fontsize=18, fontweight='bold', y=0.95)
        
        # Save chart
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            return save_path
        else:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"outputs/charts/professional_chart_{timestamp}.png"
            
            import os
            os.makedirs('outputs/charts', exist_ok=True)
            
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            plt.close()
            return filename
    
    def _draw_lagna_chart(self, ax, positions: Dict[str, PlanetPosition]):
        """Draw traditional diamond-shaped Lagna chart"""
        
        ax.clear()
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Lagna Chart (D-1)', fontsize=14, fontweight='bold', pad=20)
        
        # Draw diamond shape
        diamond = patches.Polygon([(0.5, 0.1), (0.9, 0.5), (0.5, 0.9), (0.1, 0.5)], 
                                 fill=False, edgecolor='orange', linewidth=3)
        ax.add_patch(diamond)
        
        # Draw internal lines to create houses
        ax.plot([0.3, 0.7], [0.3, 0.7], 'orange', linewidth=2)
        ax.plot([0.3, 0.7], [0.7, 0.3], 'orange', linewidth=2)
        
        # House centers for diamond chart
        house_centers = {
            1: (0.5, 0.5),     # Center
            2: (0.7, 0.65),    # Top right
            3: (0.65, 0.7),    # Top right corner
            4: (0.5, 0.75),    # Top
            5: (0.35, 0.7),    # Top left corner
            6: (0.3, 0.65),    # Top left
            7: (0.25, 0.5),    # Left
            8: (0.3, 0.35),    # Bottom left
            9: (0.35, 0.3),    # Bottom left corner
            10: (0.5, 0.25),   # Bottom
            11: (0.65, 0.3),   # Bottom right corner
            12: (0.7, 0.35)    # Bottom right
        }
        
        # Group planets by house
        house_planets = {}
        for planet, pos in positions.items():
            house = pos.house
            if house not in house_planets:
                house_planets[house] = []
            house_planets[house].append({
                'symbol': self.planet_symbols.get(planet, planet[:2]),
                'retrograde': pos.retrograde
            })
        
        # Draw houses and place planets
        for house, center in house_centers.items():
            # Draw house number
            if house == 1:
                # Ascendant house - special highlighting
                circle = patches.Circle(center, 0.08, fill=True, 
                                      facecolor='lightblue', alpha=0.3, edgecolor='blue')
                ax.add_patch(circle)
                ax.text(center[0], center[1] + 0.04, str(house), 
                       ha='center', va='center', fontsize=12, fontweight='bold', color='blue')
            else:
                ax.text(center[0], center[1] + 0.03, str(house), 
                       ha='center', va='center', fontsize=10, fontweight='bold')
            
            # Place planets
            if house in house_planets:
                planet_texts = []
                for planet_info in house_planets[house]:
                    symbol = planet_info['symbol']
                    if planet_info['retrograde']:
                        symbol += '(R)'
                    planet_texts.append(symbol)
                
                planets_text = '\n'.join(planet_texts)
                color = 'red' if len(house_planets[house]) > 1 else 'darkblue'
                ax.text(center[0], center[1] - 0.02, planets_text,
                       ha='center', va='center', fontsize=9, 
                       color=color, fontweight='bold')
    
    def _draw_planetary_table(self, ax, positions: Dict[str, PlanetPosition]):
        """Draw planetary positions table"""
        
        ax.clear()
        ax.axis('off')
        ax.set_title('Planetary Positions', fontsize=12, fontweight='bold')
        
        # Create table data
        table_data = []
        headers = ['Planet', 'Rashi', 'Degree', 'Nakshatra', 'House']
        
        planet_order = ['Ascendant', 'Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Rahu', 'Ketu']
        
        for planet in planet_order:
            if planet in positions:
                pos = positions[planet]
                degree_str = f"{pos.degree:02d}°{pos.minute:02d}'"
                retrograde_mark = " (R)" if pos.retrograde else ""
                
                table_data.append([
                    planet + retrograde_mark,
                    pos.rashi,
                    degree_str,
                    pos.nakshatra,
                    str(pos.house)
                ])
        
        # Create table
        table = ax.table(cellText=table_data, colLabels=headers,
                        cellLoc='center', loc='center',
                        colWidths=[0.2, 0.2, 0.15, 0.25, 0.1])
        
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.5)
        
        # Style the table
        for i in range(len(headers)):
            table[(0, i)].set_facecolor('#4CAF50')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        for i in range(1, len(table_data) + 1):
            for j in range(len(headers)):
                if i % 2 == 0:
                    table[(i, j)].set_facecolor('#F5F5F5')
    
    def _draw_dasha_info(self, ax, current_dasha: Dict):
        """Draw current dasha information"""
        
        ax.clear()
        ax.axis('off')
        ax.set_title('Current Dasha Status', fontsize=12, fontweight='bold')
        
        if current_dasha and 'current_mahadasha' in current_dasha:
            dasha_text = f"""
Current Mahadasha: {current_dasha['current_mahadasha']}

Start Date: {current_dasha.get('start_date', 'N/A')}
End Date: {current_dasha.get('end_date', 'N/A')}

Remaining: {current_dasha.get('remaining_years', 0):.1f} years
Completion: {current_dasha.get('completion_percentage', 0):.1f}%

Status: {current_dasha.get('status', 'Active')}
            """
        else:
            dasha_text = "Dasha information not available"
        
        ax.text(0.1, 0.9, dasha_text, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', 
                bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.8))
    
    def _draw_birth_details(self, ax, birth_data: Dict):
        """Draw birth details"""
        
        ax.clear()
        ax.axis('off')
        ax.set_title('Birth Details', fontsize=12, fontweight='bold')
        
        if birth_data:
            birth_text = f"""
Name: {birth_data.get('name', 'N/A')}    |    Date: {birth_data.get('birth_date', 'N/A')}    |    Time: {birth_data.get('birth_time', 'N/A')}    |    Place: {birth_data.get('place', 'N/A')}

Birth Nakshatra: {birth_data.get('birth_nakshatra', 'N/A')}    |    Coordinates: {birth_data.get('latitude', 0):.2f}°N, {birth_data.get('longitude', 0):.2f}°E
            """
        else:
            birth_text = "Birth details not available"
        
        ax.text(0.5, 0.5, birth_text, transform=ax.transAxes, fontsize=10,
                ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.5", facecolor='lightcyan', alpha=0.8))

print("✅ Professional Chart Visualizer loaded")
