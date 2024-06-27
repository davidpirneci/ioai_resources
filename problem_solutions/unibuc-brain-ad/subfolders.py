import os
import shutil
import pandas as pd

# Create a DataFrame
df = pd.read_csv('validation_labels.txt')

# Define the source and target directories
source_dir = 'val'
class_0_dir = 'class_0'
class_1_dir = 'class_1'

# Create target directories if they don't exist
os.makedirs(class_0_dir, exist_ok=True)
os.makedirs(class_1_dir, exist_ok=True)

# Move images to corresponding class directories
for index, row in df.iterrows():
    image_id = f"{row['id']:06d}"
    image_class = row['class']
    source_path = os.path.join(source_dir, f"{image_id}.png")
    if image_class == 0:
        target_path = os.path.join(class_0_dir, f"{image_id}.png")
    else:
        target_path = os.path.join(class_1_dir, f"{image_id}.png")
    
    if os.path.exists(source_path):
        shutil.move(source_path, target_path)
    else:
        print(f"Warning: {source_path} does not exist.")

print("Images have been moved to the corresponding class folders.")
