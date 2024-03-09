import easyocr
import json
import re


def extract_account_number(image_path):
    result = reader.readtext(image_path)
    extracted_text = ""
    for detection in result:
        text = detection[1]
        extracted_text += text + "\n"
    account_number_match = re.search(
        r"(?:Account Number|Credit Card)[\s:]*([\d\s]+)", extracted_text, re.IGNORECASE
    )
    return (
        account_number_match.group(1).replace(" ", "").strip()
        if account_number_match
        else None
    )


def process_files(file_paths):
    if isinstance(file_paths, str):
        file_paths = [file_paths]
    data = {}
    for file_path in file_paths:
        account_number = extract_account_number(file_path)
        data[file_path] = {"account_number": account_number}
    return data


reader = easyocr.Reader(["en"])

# usage with a single file
# image_paths = '/Users/cbn/Downloads/chase_cc_1.png'

# usage with multiple files
image_paths = [
    "/Users/cbn/Downloads/chase_cc_1.png",
    "/Users/cbn/Downloads/chase statement 2.jpeg",
    "/Users/cbn/Downloads/chase_5.png",
    "/Users/cbn/Downloads/chase_4.jpeg",
    "/Users/cbn/Downloads/chase_3.png",
]

# Process the files and get the data
data = process_files(image_paths)

# Convert to a JSON string and print
json_data = json.dumps(data, indent=4)
print("Extracted Data in JSON:")
print(json_data)