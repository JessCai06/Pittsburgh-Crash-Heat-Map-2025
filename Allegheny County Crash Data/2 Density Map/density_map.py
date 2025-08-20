# this file creates the crash density map (HTML) in the same folder
import pandas as pd
import folium
from folium.plugins import HeatMap
import branca


df = pd.read_csv('Allegheny County Crash Data/1 Crash Data Cleanup/heavy_truck_crashes_cleaned.csv', low_memory=False)

m = folium.Map(
    location=[df['LATITUDE_DEC'].mean(),df['LONGITUDE_DEC'].mean()],
    zoom_start=10
)

colormap = branca.colormap.LinearColormap(
    ['blue','cyan','lime','orange','red'],
    vmin=0, vmax=1,
    caption='Relative Crash Density'
)
colormap.add_to(m)

heat_data = df[['LATITUDE_DEC','LONGITUDE_DEC']].values.tolist()

HeatMap(
    data=heat_data,
    radius=12,         # pixel radius of each “point”
    blur=18,         # how soft the blobs
    min_opacity=0.4,    # visibility of low‐density areas
    max_opacity=0.9,     # strength of hotspots
    gradient={
    '0.0': 'blue',
    '0.2': 'cyan',
    '0.4': 'lime',
    '0.6': 'orange',
    '0.8': 'red',
    '1.0': 'darkred',
}

).add_to(m)


m.save('Allegheny County Crash Data/2 Density Map/heavy_truck_crashes_density_map.html')