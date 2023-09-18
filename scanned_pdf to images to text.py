#Converts scanned pdf to separate images and extract text from it(Language:Tamil)
import sys
sys.stdout.reconfigure(encoding='utf-8')

import fitz  # PyMuPDF
import pytesseract
from PIL import Image

# Replace 'path_to_your_scanned.pdf' with the actual path to your scanned PDF file
pdf_path = 'tamil.pdf'

# Function to extract images and Tamil text from the PDF
def extract_tamil_text_from_pdf(pdf_path):
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

            # Perform OCR to extract Tamil text from the image
            tamil_text = pytesseract.image_to_string(Image.open(image_filename), lang='tam')
            extracted_text.append(tamil_text)

    return extracted_text

# Call the function to extract images and Tamil text from the PDF
extracted_tamil_text = extract_tamil_text_from_pdf(pdf_path)

# # Print or use the extracted Tamil text
# for i, tamil_text in enumerate(extracted_tamil_text, start=1):
#     print(f"Tamil Text from Image {i}:\n{tamil_text}\n")

# Save the extracted Tamil text to a text file
output_file = 'extracted_tamil_text.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    for tamil_text in extracted_tamil_text:
        file.write(tamil_text + '\n')

print(f"Extracted Tamil text saved to {output_file}")
