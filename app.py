from flask import Flask, send_file, jsonify, render_template
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

# More detailed lens catalog
LENS_CATALOG = [
    {"id": 1, "name": "Lens 1", "focal_length": "50mm", "aperture": "f/1.8", "price": 299.99},
    {"id": 2, "name": "Lens 2", "focal_length": "35mm", "aperture": "f/1.4", "price": 499.99},
    {"id": 3, "name": "Lens 3", "focal_length": "85mm", "aperture": "f/1.8", "price": 399.99},
    {"id": 4, "name": "Lens 4", "focal_length": "24-70mm", "aperture": "f/2.8", "price": 899.99},
    {"id": 5, "name": "Lens 5", "focal_length": "70-200mm", "aperture": "f/4", "price": 799.99}
]

def generate_text_image(text: str) -> BytesIO:
    # Create a new image with white background
    width = max(len(text) * 20, 200)  # Adjust width based on text length
    height = 100
    image = Image.new('RGB', (width, height), color='white')
    
    # Create draw object
    draw = ImageDraw.Draw(image)
    
    # Try to use a default font (you might want to specify a custom font file path)
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw the text
    draw.text((x, y), text, fill='black', font=font)
    
    # Save image to BytesIO object
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    
    return img_io

@app.route('/')
def hello_world():
    return send_file('static/index.html')

@app.route('/image/<text>')
def get_image(text):
    img_io = generate_text_image(text)
    return send_file(img_io, mimetype='image/png')

@app.route('/lenses')
def get_lenses():
    return jsonify(LENS_CATALOG)

if __name__ == '__main__':
    app.run()
