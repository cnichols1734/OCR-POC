import easyocr
import json
import re

reader = easyocr.Reader(['en'])

# Read the image file
image_path = '/Users/cbn/Downloads/chasecc1.png'
result = reader.readtext(image_path)

extracted_text = ""

# Iterate over the OCR result and append to the string
for detection in result:
    text = detection[1]
    extracted_text += text + "\n"

# Output the entire block of text for verification
print("Extracted Text:")
print(extracted_text)

# Modify the regex to search for 'Account Number' or 'Credit Card' followed by digits.
account_number_match = re.search(r'(?:Account Number|Credit Card)[\s:]*([\d\s]+)', extracted_text, re.IGNORECASE)

# If we find a match extract the data
account_number = account_number_match.group(1).replace(" ", "").strip() if account_number_match else None

# Create a JSON object with the data
data = {
    'account_number': account_number
}

# print all extracted data
json_data = json.dumps(data, indent=4)
print("Extracted Data in JSON:")
print(json_data)
