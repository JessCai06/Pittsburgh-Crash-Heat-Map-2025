import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import colormaps 

df = pd.read_csv('Allegheny County Crash Data/heavy_truck_crashes_cleaned.csv', low_memory=False)
df['CRASH_MONTH'] = pd.to_numeric(df['CRASH_MONTH'], errors='coerce')
df['CRASH_YEAR'] = pd.to_numeric(df['CRASH_YEAR'], errors='coerce')
df = df.dropna(subset=['CRASH_MONTH', 'CRASH_YEAR'])

grouped = df.groupby(['CRASH_YEAR', 'CRASH_MONTH']).size().unstack(fill_value=0)
years = grouped.index.astype(int)

norm = mcolors.Normalize(vmin=years.min(), vmax=years.max())
cmap = colormaps['coolwarm']

fig, ax = plt.subplots(figsize=(14, 8))

for year in years:
    color = cmap(norm(year))
    ax.plot(range(1, 13), grouped.loc[year], label=str(year), color=color)

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(range(1, 13))
ax.set_xticklabels(month_labels)

ax.set_xlabel('Month')
ax.set_ylabel('Crash Count')
ax.set_title('Monthly Heavy Truck Crash Counts by Year (Color Gradient by Recency)')
ax.grid(True, linestyle='--', alpha=0.6)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])  # required dummy array for colorbar
cbar = fig.colorbar(sm, ax=ax, pad=0.01)
cbar.set_label('Crash Year')

plt.tight_layout()
plt.show()
