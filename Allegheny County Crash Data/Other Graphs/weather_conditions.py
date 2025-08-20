import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Allegheny County Crash Data/heavy_truck_crashes_cleaned.csv', low_memory=False)

weather_codes = {
    1: "Blowing Sand, Soil, Dirt",
    2: "Blowing Snow",
    3: "Clear",
    4: "Cloudy",
    5: "Fog, Smog, Smoke",
    6: "Freezing Rain or Drizzle",
    7: "Rain",
    8: "Severe Crosswinds",
    9: "Sleet or Hail",
    10: "Snow",
    98: "Other",
    99: "Unknown"
}

df['WEATHER'] = df['WEATHER'].replace(weather_codes)

weather_counts = df['WEATHER'].value_counts().sort_values(ascending=False)
weather_counts_filtered = weather_counts.drop(['Unknown', 'Other'], errors='ignore')
x = np.arange(len(weather_counts_filtered))
y = weather_counts_filtered.values

slope, intercept = np.polyfit(x, y, 1)
y_fit = slope * x + intercept

plt.figure(figsize=(12, 6))
plt.bar(weather_counts_filtered.index, y, color='lightblue', label='Crash Count')
plt.plot(weather_counts_filtered.index, y_fit, color='red', linestyle='--', label='LSRL')
plt.title('Crash Counts by Weather Condition with Line of Best Fit')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Crashes')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

print(f"LSRL Equation: y = {slope:.2f}x + {intercept:.2f}")
