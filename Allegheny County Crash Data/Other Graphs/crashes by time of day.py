import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors


df = pd.read_csv('Allegheny County Crash Data/heavy_truck_crashes_cleaned.csv', low_memory=False)

df = df.dropna(subset=['CRASH_YEAR', 'HOUR_OF_DAY'])
df['CRASH_YEAR'] = pd.to_numeric(df['CRASH_YEAR'], errors='coerce')
df['HOUR_OF_DAY'] = pd.to_numeric(df['HOUR_OF_DAY'], errors='coerce')

df = df[(df['HOUR_OF_DAY'] >= 0) & (df['HOUR_OF_DAY'] <= 23)]
df = df[(df['CRASH_YEAR'] >= 2004) & (df['CRASH_YEAR'] <= 2023)]


years = sorted(df['CRASH_YEAR'].unique())
norm = mcolors.Normalize(vmin=min(years), vmax=max(years))
cmap = plt.colormaps.get_cmap('coolwarm')  # Cool blue to warm red
colors = [cmap(norm(year)) for year in years]

plt.figure(figsize=(12, 6))

for year, color in zip(years, colors):
    yearly_data = df[df['CRASH_YEAR'] == year]
    hour_counts = yearly_data['HOUR_OF_DAY'].value_counts().sort_index()
    plt.plot(hour_counts.index, hour_counts.values, label=str(year), color=color)

plt.title('Hourly Heavy Truck Crashes by Year (2004-2023)')
plt.xlabel('Hour of Day (24h)')
plt.ylabel('Number of Crashes')
plt.xticks(range(0, 24))
plt.grid(axis='y', linestyle='--', alpha=0.5)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

plt.tight_layout()
plt.show()

# i need to 1) normalize rainy days based on actual number of days it rained.
# 2) add weather conditions into heat map
# 3) checking beibei's code