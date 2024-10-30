from PIL import Image, ImageDraw, ImageFont
import os
import math

def create_directory():
    os.makedirs('static/images/publications', exist_ok=True)

def create_gradient_background(size, start_color, end_color):
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    
    for y in range(size[1]):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * y / size[1])
        g = int(start_color[1] + (end_color[1] - start_color[1]) * y / size[1])
        b = int(start_color[2] + (end_color[2] - start_color[2]) * y / size[1])
        draw.line([(0, y), (size[0], y)], fill=(r, g, b))
    
    return image

def add_decorative_elements(draw, size):
    # Add subtle circular patterns
    for i in range(0, size[0], 100):
        radius = 30
        draw.arc([i, -radius, i + radius*2, radius], 180, 360, fill='#333333', width=2)
        draw.arc([i, size[1]-radius, i + radius*2, size[1]+radius], 0, 180, fill='#333333', width=2)

def create_placeholder_image(filename, title, subtitle, size=(800, 400)):
    # Create gradient background
    start_color = (26, 26, 26)  # Dark gray
    end_color = (40, 40, 40)    # Slightly lighter gray
    img = create_gradient_background(size, start_color, end_color)
    draw = ImageDraw.Draw(img)

    # Add decorative elements
    add_decorative_elements(draw, size)

    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Add main title
    title_color = '#66b3ff'  # Light blue
    text_wrap_width = 30
    wrapped_text = '\n'.join([title[i:i+text_wrap_width] for i in range(0, len(title), text_wrap_width)])
    
    # Center the text
    bbox = draw.textbbox((0, 0), wrapped_text, font=title_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 3

    # Draw text with subtle shadow
    draw.text((x+2, y+2), wrapped_text, font=title_font, fill='#000000')
    draw.text((x, y), wrapped_text, font=title_font, fill=title_color)

    # Add subtitle
    subtitle_y = y + text_height + 20
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (size[0] - subtitle_width) // 2
    draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill='#cccccc')

    # Add a border
    draw.rectangle([0, 0, size[0]-1, size[1]-1], outline='#333333', width=3)

    img.save(f'static/images/publications/{filename}')
    print(f"Created styled placeholder for {filename}")

def create_all_placeholders():
    create_directory()
    
    placeholders = [
        {
            'filename': 'spaceflight_microbiology.jpg',
            'title': 'Microbiology of Human Spaceflight',
            'subtitle': 'Impact on Health and Habitat Sustainability'
        },
        {
            'filename': 'gut_microbes.jpg',
            'title': 'Pathogenic Phenotypes in Fluid Shear',
            'subtitle': 'Studies on Multidrug Resistant Salmonella'
        },
        {
            'filename': 'sustainable_space.jpg',
            'title': 'Sustainable Space Exploration',
            'subtitle': 'Harnessing Microorganisms for Space Travel'
        },
        {
            'filename': 'spaceflight_book.jpg',
            'title': 'Spaceflight Culture Studies',
            'subtitle': 'Novel Insights into Disease Mechanisms'
        },
        {
            'filename': 'nasa_research.jpg',
            'title': 'NASA Research Project',
            'subtitle': 'Understanding Microbial Interactions in Space'
        }
    ]
    
    for placeholder in placeholders:
        create_placeholder_image(
            placeholder['filename'],
            placeholder['title'],
            placeholder['subtitle']
        )

if __name__ == "__main__":
    create_all_placeholders()
