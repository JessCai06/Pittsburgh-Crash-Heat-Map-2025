import pandas as pd
import folium
from folium.plugins import HeatMap
import branca

df = pd.read_csv('Allegheny County Crash Data/1 Crash Data Cleanup/heavy_truck_crashes_cleaned.csv', low_memory=False)
weights_df = pd.read_csv('Allegheny County Crash Data/3 Time Series Crash Map/year_weight_models.csv')


df = df.merge(weights_df[['Year', 'Linear_Weight']], how='left', left_on='CRASH_YEAR', right_on='Year')
df = df.dropna(subset=['LATITUDE_DEC', 'LONGITUDE_DEC', 'Linear_Weight'])

m = folium.Map(
    location=[df['LATITUDE_DEC'].mean(), df['LONGITUDE_DEC'].mean()],
    zoom_start=10
)

colormap = branca.colormap.LinearColormap(
    ['blue', 'cyan', 'lime', 'orange', 'red'],
    vmin=0, vmax=1,
    caption='Crash Density Weighted by Recency (Linear)'
)
colormap.add_to(m)
heat_data = df[['LATITUDE_DEC', 'LONGITUDE_DEC', 'Linear_Weight']].values.tolist()


HeatMap(
    data=heat_data,
    radius=12,
    blur=18,
    min_opacity=0.4,
    max_opacity=0.9,
    gradient={
        0.0: 'blue',
        0.2: 'cyan',
        0.4: 'lime',
        0.6: 'orange',
        0.8: 'red',
        1.0: 'darkred',
    }
).add_to(m)

m.save('Allegheny County Crash Data/3 Time Series Crash Map/weighted_heavy_truck_crashes_density_map.html')