import os
import requests
from PIL import Image
from io import BytesIO

def create_directory():
    os.makedirs('static/images/publications', exist_ok=True)

def download_and_save_image(url, filename, size=(800, 600)):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(f'static/images/publications/{filename}')
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

def create_placeholder_image(filename, text, size=(800, 600)):
    img = Image.new('RGB', size, color='#1a1a1a')
    img.save(f'static/images/publications/{filename}')
    print(f"Created placeholder for {filename}")

def save_publication_images():
    create_directory()
    
    # Images for each publication with fallback URLs
    images = [
        {
            'primary_url': 'https://journals.asm.org/cms/10.1128/mmbr.00144-23/asset/7217a188-b344-4482-97ea-a19a24c97bc2/assets/images/large/mmbr.00144-23.f001.jpg',
            'fallback_url': 'https://www.asm.org/ASM/media/Press-Releases/2019/bacteria-in-space.jpg',
            'filename': 'spaceflight_microbiology.jpg',
            'description': 'Microbiology in Space'
        },
        {
            'primary_url': 'https://www.tandfonline.com/doi/cover-img/10.1080/19490976.2024.2357767',
            'fallback_url': 'https://www.nature.com/articles/s41522-021-00240-5/figures/1',
            'filename': 'gut_microbes.jpg',
            'description': 'Gut Microbes'
        },
        {
            'primary_url': 'https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-023-37070-2/MediaObjects/41467_2023_37070_Fig1_HTML.png',
            'fallback_url': 'https://www.nature.com/articles/s41467-023-37070-2/figures/1',
            'filename': 'sustainable_space.jpg',
            'description': 'Sustainable Space'
        },
        {
            'primary_url': 'https://media.springernature.com/w306/springer-static/cover-hires/book/978-1-4939-3277-1',
            'fallback_url': 'https://link.springer.com/book/10.1007/978-1-4939-3277-1',
            'filename': 'spaceflight_book.jpg',
            'description': 'Spaceflight Book'
        },
        {
            'primary_url': 'https://www.nasa.gov/wp-content/uploads/2023/03/iss067e054069.jpg',
            'fallback_url': 'https://www.nasa.gov/sites/default/files/thumbnails/image/iss063e039393.jpg',
            'filename': 'nasa_research.jpg',
            'description': 'NASA Research'
        }
    ]
    
    for image in images:
        success = download_and_save_image(image['primary_url'], image['filename'])
        if not success:
            print(f"Trying fallback URL for {image['filename']}")
            success = download_and_save_image(image['fallback_url'], image['filename'])
        
        if not success:
            print(f"Creating placeholder for {image['filename']}")
            create_placeholder_image(image['filename'], image['description'])

if __name__ == "__main__":
    save_publication_images()
