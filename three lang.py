#So this basically takes a document any lang(tamil,telugu,hindi) and convert it to english text doc
import sys
sys.stdout.reconfigure(encoding='utf-8')

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from googletrans import Translator
from langdetect import detect

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    extracted_text = []

    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        image_list = page.get_images(full=True)

        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_data = base_image["image"]

            # Save the image as a file
            image_filename = f"page_{page_number + 1}_image_{image_index + 1}.png"
            with open(image_filename, "wb") as image_file:
                image_file.write(image_data)
            # Perform language detection on the extracted text
            text = pytesseract.image_to_string(Image.open(image_filename))

            # Detect the language of the extracted text
            detected_language = detect(text)

            # Define language codes for Telugu and Hindi
            telugu_lang_code = 'te'
            hindi_lang_code = 'hi'

            # Set the appropriate language for Tesseract OCR based on the detected language
            if detected_language == telugu_lang_code:
                lang = 'tel'  # Telugu language code
            elif detected_language == hindi_lang_code:
                lang = 'hin'  # Hindi language code
            else:
                lang = 'tam'  # Default to Tamil if language detection is uncertain

            # Perform OCR to extract text from the image with the detected language
            
            extracted_text.append(pytesseract.image_to_string(Image.open(image_filename), lang=lang))

    return extracted_text

# Call the function to extract text from the PDF
pdf_path = 'tamil.pdf'  # Replace with your PDF file path
extracted_text = extract_text_from_pdf(pdf_path)

# Translate the extracted text to English if it's not already in English
translator = Translator()
translated_text = []

for text in extracted_text:
    translation = translator.translate(text, src='auto', dest='en')
    translated_text.append(translation.text)

# Save the translated English text to a text file
translated_output_file = 'translated_english_text.txt'
with open(translated_output_file, 'w', encoding='utf-8') as file:
    for english_text in translated_text:
        file.write(english_text + '\n')

print(f"Translated English text saved to {translated_output_file}")


