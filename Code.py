import os
import pandas as pd
from PIL import Image
import time

# --- CONFIG ---
source_folder = os.path.expanduser('~/Desktop/Coffee/Uncategorised')
output_base = os.path.expanduser('~/Desktop/Coffee/Categorised')
csv_path = os.path.join(output_base, 'latte_art_audit.csv')

os.makedirs(output_base, exist_ok=True)

# 1. Load Data
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    processed_files = df['filename'].tolist()
else:
    df = pd.DataFrame(columns=["filename", "overall_rank", "shape_type", "shape_rank", "color", "texture", "cup_size", "vibes", "notes"])
    processed_files = []

all_photos = sorted([f for f in os.listdir(source_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg', '.heic'))])
photos_to_audit = [f for f in all_photos if f not in processed_files]

print(f"\n--- ☕ AUDIT ACTIVE: {len(photos_to_audit)} REMAINING ---")

new_entries = []
start_session_time = time.time()

try:
    for photo in photos_to_audit:
        img_path = os.path.join(source_folder, photo)
        img = Image.open(img_path)
        img.show()
        
        print(f"\n>>> Photo: {photo}")
        
        def get_safe_input(prompt, is_numeric=True):
            while True:
                val = input(prompt).strip()
                if val.lower() == 'q': raise KeyboardInterrupt
                if val.lower() in ['', 'n', 'na', 'n/a']: return None
                if is_numeric:
                    try:
                        num = int(val)
                        if 1 <= num <= 5: return num
                        else: print("Please enter 1-5.")
                    except ValueError:
                        print("❌ Enter a number (or 'q' to quit).")
                else:
                    return val.capitalize()

        entry = {
            "filename": photo,
            "shape_type": get_safe_input("Shape Type: ", is_numeric=False),
            "shape_rank": get_safe_input("Shape Rank (1-5): "),
            "color": get_safe_input("Color Rank (1-5): "),
            "texture": get_safe_input("Texture Rank (1-5): "),
            "cup_size": get_safe_input("Cup Size: ", is_numeric=False),
            "vibes": get_safe_input("Vibes (1-5): "),
            "notes": input("Notes: ").strip()
        }
        new_entries.append(entry)

except KeyboardInterrupt:
    print("\n\nStopping...")

# 2. Save and Minimal Stats
if new_entries:
    new_df = pd.DataFrame(new_entries)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(csv_path, index=False)
    
    # Simple Planning Metrics
    elapsed = time.time() - start_session_time
    speed = elapsed / len(new_entries)
    remaining = (len(all_photos) - len(df)) * speed / 60
    
    print(f"--- SESSION SUMMARY ---")
    print(f"Speed: {speed:.1f}s per photo")
    print(f"Remaining work: ~{remaining:.1f} minutes")
    print(f"Total processed: {len(df)} / {len(all_photos)}")