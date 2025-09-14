import pandas as pd

INPUT_CSV  = 'Allegheny County Crash Data/1 Crash Data Cleanup/Allegheny County Crash Data.csv'
OUTPUT_CSV = 'Allegheny County Crash Data/1 Crash Data Cleanup/heavy_truck_crashes_cleaned.csv'

# fields to filter on
FILTER_COLS = [
    'COMM_VEH_COUNT',     # Total Commercial vehicles involved
    'HVY_TRUCK_RELATED',  # At least one Heavy Truck involved? (0 = No, 1 = Yes)
    'SMALL_TRUCK_COUNT',  # Total amount of Small Trucks involved
    'HEAVY_TRUCK_COUNT'   # Total amount of Heavy Trucks involved
]

def dms_to_dd(dms_str: str) -> float:
    dms_str = dms_str.strip()
    deg, rest = dms_str.split()
    mins, secs = rest.split(':')
    return float(deg) + float(mins)/60 + float(secs)/3600

def safe_dms_to_dd(s):
    try:
        return dms_to_dd(s)
    except Exception:
        return None


df = pd.read_csv(INPUT_CSV, dtype=str)

df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

# 3. Convert filter columns to numeric (invalid → 0)
for col in FILTER_COLS:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)


mask = df[FILTER_COLS].gt(0).any(axis=1)
df = df.loc[mask].copy()
df['CRASH_MONTH'] = pd.to_numeric(df['CRASH_MONTH'], errors='coerce')

df['LATITUDE_DEC']  = df['LATITUDE'].apply(safe_dms_to_dd)
df['LONGITUDE_DEC'] = df['LONGITUDE'].apply(safe_dms_to_dd)*-1

df = df.dropna(subset=['LATITUDE_DEC','LONGITUDE_DEC'])

df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved {len(df)} records to '{OUTPUT_CSV}'.")
