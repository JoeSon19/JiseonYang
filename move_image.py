import os
import shutil

def move_profile_picture():
    source_path = 'jiseon yang.jpg'
    destination_path = 'static/images/profile_picture.jpg'
    
    # Create the destination directory if it doesn't exist
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Copy and rename the file
    shutil.copy(source_path, destination_path)
    
    print(f"Profile picture copied from {source_path} to {destination_path}")

if __name__ == "__main__":
    move_profile_picture()
