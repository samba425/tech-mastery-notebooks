from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from pathlib import Path
input_path = "/Users/sambasiva/Documents/ML&AI(DS)/personal work/tech-mastery-notebooks/images/image.png"
output1 = "/Users/sambasiva/Documents/ML&AI(DS)/personal work/tech-mastery-notebooks/images/image_modern.png"
output2 = "/Users/sambasiva/Documents/ML&AI(DS)/personal work/tech-mastery-notebooks/images/image_ultra_modern.png"
print("Creating modern images...")
img = Image.open(input_path)
width, height = img.size
new_width = width + 100
new_height = height + 120
modern_img = Image.new('RGB', (new_width, new_height), '#FFFFFF')
draw = ImageDraw.Draw(modern_img, 'RGBA')
for y in range(new_height):
    ratio = y / new_height
    r = int(240 + (255 - 240) * ratio)
    g = int(245 + (255 - 245) * ratio)
    b = int(250 + (255 - 250) * ratio)
    draw.line([(0, y), (new_width, y)], fill=(r, g, b))
for y in range(80):
    ratio = y / 80
    r = int(20 + (60 - 20) * ratio)
    g = int(100 + (140 - 100) * ratio)
    b = int(200 + (255 - 200) * ratio)
    draw.line([(0, y), (new_width, y)], fill=(r, g, b))
accent_color = (0, 212, 255, 150)
draw.polygon([(0, 0), (150, 0), (0, 150)], fill=accent_color)
draw.polygon([(new_width, new_height), (new_width-150, new_height), (new_width, new_height-150)], fill=accent_color)
side_accent = (255, 100, 150, 100)
draw.rectangle([0, new_height//2-3, 40, new_height//2+3], fill=side_accent)
x_offset = (new_width - width) // 2
y_offset = 100
shadow = Image.new('RGBA', img.size, (0, 0, 0, 0))
shadow_draw = ImageDraw.Draw(shadow)
shadow_draw.rectangle([5, 5, img.size[0]-5, img.size[1]-5], fill=(0, 0, 0, 60))
shadow = shadow.filter(ImageFilter.GaussianBlur(10))
modern_img.paste(shadow, (x_offset + 5, y_offset + 5), shadow)
if img.mode == 'RGBA':
    modern_img.paste(img, (x_offset, y_offset), img)
else:
    modern_img.paste(img, (x_offset, y_offset))
draw = ImageDraw.Draw(modern_img, 'RGBA')
border_color = (0, 212, 255, 200)
for i in range(3):
    draw.rectangle([x_offset-i, y_offset-i, x_offset+width+i, y_offset+height+i], outline=border_color, width=1)
try:
    title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
except:
    title_font = ImageFont.load_default()
title = "RAG ARCHITECTURE - MODERNIZED"
draw.text((new_width//2 + 2, 32), title, fill=(0, 0, 0, 100), font=title_font, anchor='mm')
draw.text((new_width//2, 30), title, fill='white', font=title_font, anchor='mm')
enhancer = ImageEnhance.Contrast(modern_img)
modern_img = enhancer.enhance(1.1)
enhancer = ImageEnhance.Sharpness(modern_img)
modern_img = enhancer.enhance(1.2)
modern_img.save(output1, 'PNG', quality=95)
print(f"Saved: {output1}")
new_width = int(width * 1.3)
new_height = int(height * 1.3)
ultra_img = Image.new('RGB', (new_width, new_height))
draw = ImageDraw.Draw(ultra_img, 'RGBA')
for y in range(new_height):
    for x in range(new_width):
        ratio_x = x / new_width
        ratio_y = y / new_height
        r = int(30 + (180 - 30) * ratio_x + (50 * ratio_y))
        g = int(80 + (100 - 80) * ratio_y)
        b = int(200 + (255 - 200) * ratio_x)
        draw.point((x, y), fill=(r, g, b))
ultra_img = ultra_img.filter(ImageFilter.GaussianBlur(30))
for i in range(5):
    x = (new_width // 5) * i + 50
    y = (new_height // 5) * (i % 3) + 50
    for r in range(100, 0, -10):
        alpha = int(30 * (r / 100))
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(255, 255, 255, alpha))
x_offset = (new_width - width) // 2
y_offset = (new_height - height) // 2
glass_padding = 30
glass_rect = [x_offset - glass_padding, y_offset - glass_padding, x_offset + width + glass_padding, y_offset + height + glass_padding]
draw.rectangle(glass_rect, fill=(255, 255, 255, 40))
draw.rectangle(glass_rect, outline=(255, 255, 255, 120), width=2)
if img.mode == 'RGBA':
    ultra_img.paste(img, (x_offset, y_offset), img)
else:
    ultra_img.paste(img, (x_offset, y_offset))
enhancer = ImageEnhance.Contrast(ultra_img)
ultra_img = enhancer.enhance(1.15)
ultra_img.save(output2, 'PNG', quality=95)
print(f"Saved: {output2}")
print("Done!")







