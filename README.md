# Lens Catalog with Image Generator

A simple web application that displays a lens catalog and generates images with lens focal lengths. The application allows users to select different lenses from a catalog and generate images displaying their focal lengths.

## Features
- Interactive lens catalog with detailed specifications
- Dynamic image generation for lens focal lengths
- Responsive web interface

## Setup

1. Create a virtual environment (recommended):

2. Install dependencies:

## Run

1. Start the Flask server:

2. Open your web browser and visit:

## Usage

1. Select a lens from the dropdown menu to view its details
2. The lens details (focal length, aperture, and price) will be displayed
3. Click the "Render Focal Length" button to generate an image
4. The generated image will appear below the lens details

## Project Structure
- `app.py` - Flask application with API endpoints and image generation
- `static/index.html` - Frontend web interface
- `requirements.txt` - Python package dependencies

## Dependencies
- Flask (3.0.2) - Web framework
- Pillow (10.2.0) - Image processing library

## API Endpoints
- `/` - Serves the main web interface
- `/lenses` - Returns the lens catalog data
- `/image/<text>` - Generates and returns a PNG image with the specified text

