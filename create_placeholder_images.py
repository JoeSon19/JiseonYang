from PIL import Image, ImageDraw, ImageFont
import os

def create_gradient_image(width, height, text, filename):
    # Create a new image with gradient background
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # Create a gradient background
    for y in range(height):
        r = int((y / height) * 50)  # Dark gradient
        g = int((y / height) * 60)
        b = int((y / height) * 80)
        for x in range(width):
            draw.point((x, y), fill=(r, g, b))
    
    # Add text
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 30)
    except:
        font = ImageFont.load_default()
        
    # Calculate text position for center alignment
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Add a semi-transparent overlay for better text visibility
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle([(0, y-10), (width, y+text_height+10)], fill=(0, 0, 0, 128))
    image.paste(Image.alpha_composite(Image.new('RGBA', image.size), overlay).convert('RGB'))
    
    # Draw text
    draw = ImageDraw.Draw(image)
    draw.text((x, y), text, fill='white', font=font)
    
    # Save image
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename)
    print(f"Created placeholder for {os.path.basename(filename)}")

# Create placeholder images
images = [
    ("spaceflight_microbiology.jpg", "Spaceflight Microbiology Research"),
    ("gut_microbes.jpg", "Gut Microbes Study"),
    ("sustainable_space.jpg", "Sustainable Space Research"),
    ("spaceflight_book.jpg", "Spaceflight Research Book"),
    ("nasa_research.jpg", "NASA Research Project")
]

for img_file, text in images:
    filepath = f"static/images/publications/{img_file}"
    create_gradient_image(800, 600, text, filepath)
