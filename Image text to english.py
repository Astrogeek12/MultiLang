#This code converts tamil text from image to english text
import sys
sys.stdout.reconfigure(encoding='utf-8')

import cv2
import pytesseract
from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Replace 'path_to_your_image.jpg' with the actual path to your image file
image_path = 'tamil.png'

# Read the image using OpenCV
image = cv2.imread(image_path)

# Convert the image to grayscale for OCR
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR to extract Tamil text
tamil_text = pytesseract.image_to_string(gray_image, lang='tam')

# Translate the extracted Tamil text to English
translation = translator.translate(tamil_text, src='ta', dest='en')

# Access the translated text
translated_text = translation.text

# Print the extracted and translated text
print("Extracted Tamil Text:")
print(tamil_text)

print("\nTranslated Text (English):")
print(translated_text)

#This code converts tamil text from image to english text
