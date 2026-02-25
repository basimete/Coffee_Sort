import pandas as pd
import os

# --- CONFIG ---
csv_path = os.path.expanduser('~/Desktop/Coffee/Categorised/latte_art_audit.csv')

if not os.path.exists(csv_path):
    print("Error: Could not find the CSV file!")
else:
    # 1. Load the data
    df = pd.read_csv(csv_path)
    
    # 2. Rename Column (Cup Size -> Mug Type)
    if 'cup_size' in df.columns:
        df = df.rename(columns={'cup_size': 'mug_type'})

    # 3. Apply Mug Name Mapping
    mug_mapping = {
        'Big': 'Etsy by the sea (Big)',
        'Medium': 'Boring (Medium)',
        'Small': 'HK living it up (Small)',
        'Egg': 'Spill the egg (Small)'
    }
    # Standardize current values before mapping to ensure they match keys
    if 'mug_type' in df.columns:
        df['mug_type'] = df['mug_type'].str.capitalize().replace(mug_mapping)

    # 4. Logical Cleaning: Abstract and Face shapes don't need a Shape Rank
    # We use .isin() to handle both at once
    df.loc[df['shape_type'].isin(['Abstract', 'Face']), 'shape_rank'] = None
    
    # 5. Standardize Shape Names
    df['shape_type'] = df['shape_type'].str.capitalize()

    # 6. Save the cleaned version
    df.to_csv(csv_path, index=False)
    
    print("--- Data Cleaning Complete ---")
    print(f"✅ Renamed columns and mapped {len(mug_mapping)} mug types.")
    print(f"✅ Standardized Shape Ranks for Abstract/Face categories.")