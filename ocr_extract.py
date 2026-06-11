#!/usr/bin/env python3
"""
OCR Image Text Extractor
Extracts text from images using OCR and saves it to a text file.
"""

import sys
import os
from pathlib import Path

try:
    from PIL import Image
    import pytesseract
except ImportError:
    print("Error: Required libraries not found.")
    print("Please install dependencies: pip install pytesseract pillow")
    sys.exit(1)


def extract_text_from_image(image_path, output_path=None):
    """
    Extract text from an image using OCR and save to a text file.
    
    Args:
        image_path (str): Path to the input image file
        output_path (str): Path to the output text file (optional)
    
    Returns:
        str: The extracted text
    """
    # Check if image file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return None
    
    # Generate output path if not provided
    if output_path is None:
        image_stem = Path(image_path).stem
        output_path = f"{image_stem}_extracted.txt"
    
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Extract text using OCR
        print(f"Extracting text from {image_path}...")
        extracted_text = pytesseract.image_to_string(image)
        
        # Save to text file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        
        print(f"Text successfully extracted and saved to: {output_path}")
        print(f"Character count: {len(extracted_text)}")
        
        return extracted_text
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ocr_extract.py <image_path> [output_path]")
        print("Example: python3 ocr_extract.py photo.jpg")
        print("Example: python3 ocr_extract.py photo.jpg output.txt")
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    extract_text_from_image(image_path, output_path)


if __name__ == "__main__":
    main()
