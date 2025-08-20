# this file creates an output map in HTML in the same folder
import pandas as pd
import folium

df = pd.read_csv("Greater Pittsburgh Food Bank\geocoded_locations.csv")

map_with_pins = folium.Map( zoom_start=11)

for _, row in df.iterrows():
    popup_text = f"<b>{row['LOCATION_TITLE']}</b>"
    folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=popup_text,
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map_with_pins)

# Save to HTML
map_with_pins.save("Greater Pittsburgh Food Bank\map_with_dropped_pins.html")
