import os
import shutil

def move_timeline_image():
    source_path = 'image.png'
    destination_path = 'static/images/research_timeline.png'
    
    # Create the destination directory if it doesn't exist
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Copy and rename the file
    shutil.copy(source_path, destination_path)
    
    print(f"Timeline image copied from {source_path} to {destination_path}")

if __name__ == "__main__":
    move_timeline_image()
