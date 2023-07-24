import pytesseract 
import io
import base64 
from PIL import Image
from csv import writer

# func return text from image
def read_image(base64_string:str) -> str:
    
    # Connect to tesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Get pure base64 string
    base64_string= base64_string.split(", ")[1]
    base64_image = str.encode(base64_string)

    # Convert the image format to BytesIO therefore the Image could read the file
    text = pytesseract.image_to_string(
                                        Image.open(io.BytesIO(base64.decodebytes(base64_image))),
                                        lang='eng',
                                        config='--psm 10 --oem 3 ')
    return text

# func add data
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='',encoding='utf-8-sig') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)