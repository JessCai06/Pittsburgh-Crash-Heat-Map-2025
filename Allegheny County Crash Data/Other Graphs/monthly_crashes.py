import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Allegheny County Crash Data/heavy_truck_crashes_cleaned.csv', low_memory=False)

df = df.dropna(subset=['CRASH_MONTH'])


monthly_crash_counts = df['CRASH_MONTH'].value_counts().sort_index()

month_labels = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

plt.figure(figsize=(10, 6))
plt.bar(monthly_crash_counts.index, monthly_crash_counts.values, color='skyblue')
plt.xticks(ticks=range(1, 13), labels=month_labels)
plt.xlabel('Month')
plt.ylabel('Number of Crashes')
plt.title('Heavy Truck Crashes by Month')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(bottom=3200)  # Set y-axis minimum to 3000
plt.tight_layout()
plt.show()
