#!pip install pytesseract opencv-python
import cv2
import pytesseract

# Install Tesseract OCR if not already installed
#!sudo apt install tesseract-ocr

# Update the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract" 

def preprocess_image(image_path):
    image_path ="/content/np6.jpeg"
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding for better contrast between text and background
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh

def extract_text_from_image(image_path):
    processed_image = preprocess_image(image_path)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(processed_image, config='--psm 6')  # '--psm 6' is for single uniform block of text
    return text

# Example usage:
image_path = 'license_plate.jpg' 
extracted_text = extract_text_from_image(image_path)

print("Extracted Text:", extracted_text)