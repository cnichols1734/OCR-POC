import easyocr
import json
import re
import time


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

image_paths = [
    "/Users/cbn/Downloads/chase_cc_1.png",
    "/Users/cbn/Downloads/chase statement 2.jpeg",
    "/Users/cbn/Downloads/chase_5.png",
    "/Users/cbn/Downloads/chase_4.jpeg",
    "/Users/cbn/Downloads/chase_3.png",
]

start_time = time.time()

# Process the files and get the data
data = process_files(image_paths)

end_time = time.time()
execution_time = end_time - start_time

# Convert to a JSON string and print
json_data = json.dumps(data, indent=4)
print(json_data)
print(f"Execution time: {round(execution_time, 2)} seconds")

