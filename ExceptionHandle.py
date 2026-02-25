import os
import pandas as pd
from PIL import Image

# --- CONFIG ---
csv_path = os.path.expanduser('~/Desktop/Coffee/Categorised/latte_art_audit.csv')
img_dir = os.path.expanduser('~/Desktop/Coffee/Uncategorised')

df = pd.read_csv(csv_path)

def is_actually_missing(val):
    """Checks if a value is truly empty/NaN."""
    return pd.isna(val) or str(val).strip().lower() in ['nan', 'none', '']

print("🔍 Targeted Scan for Errors...")

for index, row in df.iterrows():
    # 1. Check if shape_type is a number OR missing
    shape_val = str(row['shape_type'])
    is_numeric_error = shape_val.isdigit()
    is_shape_missing = is_actually_missing(row['shape_type'])
    
    # 2. Check if shape_rank is missing for "rankable" shapes
    # We ignore Abstract, Face, or N/A shapes
    is_rankable = str(row['shape_type']) in ['Heart', 'Tulip', 'Rosetta']
    rank_missing = is_rankable and is_actually_missing(row['shape_rank'])

    if is_numeric_error or is_shape_missing or rank_missing:
        # Show exactly why it's flagging it
        reason = "Numeric Error" if is_numeric_error else "Missing Shape" if is_shape_missing else "Missing Rank for Rankable Shape"
        print(f"\n⚠️ Row {index} needs attention. Reason: {reason}")
        
        # Open image
        try:
            img_path = os.path.join(img_dir, row['filename'])
            img = Image.open(img_path)
            img.show()
        except:
            print(f"Could not find image: {row['filename']}")

        # Input fixes
        print(f"File: {row['filename']}")
        fix_shape = input(f"Enter correct Shape (Current: {row['shape_type']}): ").strip()
        if fix_shape: 
            df.at[index, 'shape_type'] = fix_shape.capitalize()
        
        # Only ask for rank if the new shape is rankable
        if df.at[index, 'shape_type'] in ['Heart', 'Tulip', 'Rosetta']:
            fix_rank = input(f"Enter Shape Rank (Current: {row['shape_rank']}): ").strip()
            if fix_rank:
                df.at[index, 'shape_rank'] = int(fix_rank)

        df.to_csv(csv_path, index=False)
        print("✅ Fixed.")

print("\n--- Clean! All numeric errors and missing ranks for classic shapes resolved. ---")