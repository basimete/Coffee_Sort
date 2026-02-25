import os
import pandas as pd
import exifread

# --- CONFIG ---
csv_path = os.path.expanduser('~/Desktop/Coffee/Categorised/latte_art_audit.csv')
img_dir = os.path.expanduser('~/Desktop/Coffee/Uncategorised')

# Load your current audit data
df = pd.read_csv(csv_path)

def get_exif_data(filename):
    path = os.path.join(img_dir, filename)
    try:
        with open(path, 'rb') as f:
            tags = exifread.process_file(f, stop_tag="EXIF DateTimeOriginal")
            if "EXIF DateTimeOriginal" in tags:
                full_dt = str(tags["EXIF DateTimeOriginal"])
                date_part, time_part = full_dt.split(' ', 1)
                date_part = date_part.replace(':', '-')
                return date_part, time_part
    except:
        pass
    return "Unknown", "Unknown"

print("☕ Enriching and Cleaning Coffee Data...")

# 1. Extract Date and Time from EXIF
df[['date_taken', 'time_taken']] = df['filename'].apply(
    lambda x: pd.Series(get_exif_data(x))
)

# 2. Add Day of Week and Hour (Derived from EXIF)
temp_date = pd.to_datetime(df['date_taken'], errors='coerce')
df['day_of_week'] = temp_date.dt.day_name()

temp_time = pd.to_datetime(df['time_taken'], format='%H:%M:%S', errors='coerce')
df['hour'] = temp_time.dt.hour

# 3. Rename Column and Map Mug Types
if 'cup_size' in df.columns:
    df = df.rename(columns={'cup_size': 'mug_type'})

mug_mapping = {
    'Big': 'Etsy by the sea (Big)',
    'Medium': 'Boring (Medium)',
    'Small': 'HK living it up (Small)',
    'Egg': 'Spill the egg (Small)'
}
df['mug_type'] = df['mug_type'].replace(mug_mapping)

# 4. Remove unnecessary columns
if 'date_processed' in df.columns:
    df = df.drop(columns=['date_processed'])

# 5. Final Formatting: Reorder for a clean Zine CSV
cols_order = ['filename', 'date_taken', 'time_taken', 'day_of_week', 'hour', 
              'shape_type', 'shape_rank', 'color', 'texture', 'mug_type', 'vibes', 'notes']
df = df[[c for c in cols_order if c in df.columns]]

# Save the updated CSV
df.to_csv(csv_path, index=False)



print("\n✨ SUCCESS: Data is enriched and formatted for the Zine.")
print(f"Columns: {list(df.columns)}")
print(df[['filename', 'day_of_week', 'hour', 'mug_type']].head())