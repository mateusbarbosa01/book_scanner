
import pytesseract

from pytesseract import Output
# import cv2

# from PIL import Image


### To do: expand the configure_ocr function to set different languages.


### To do*: explore what to do with the confidence level data. Can we search a dictionrary for close variations of
###         the word found and correct it based on the dictionary? How to define "close" in this context?
###         Can we check the OCR data to see whether this new possible word makes sense?

### To do*: can we calibrate tesseract to better suit our purposes?

### To do: Make it so that extract_text_with_details doesn't show boxes with empty text in it.




def configure_ocr(tesseract_path=None):
    """
    Configure Tesseract OCR settings, including optional custom path to the Tesseract executable.
    """
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # Additional configurations (e.g., OCR language, custom settings) can go here.


def extract_text_from_image(image):
    """
    Extracts text from a given image using Tesseract OCR.

    Args:
        image: The image file or processed image (e.g., numpy array).

    Returns:
        string: The text extracted from the image.
    """
    text = pytesseract.image_to_string(image)
    return text


def extract_text_with_details(image):
    """
    Extracts detailed OCR data, including word-level bounding boxes and confidences.

    Args:
        image: The image file or processed image.

    Returns:
        dict: A dictionary containing the text along with details such as bounding boxes, and confidence levels
    """
    details = pytesseract.image_to_data(image, output_type=Output.DICT)
    return details

if __name__ == "__main__":

#if the image's path is 'C:/Users/mateu/PycharmProjects/book_scanner/data/book_spines/1-side.jpg'
    image_path = 'C:/Users/mateu/PycharmProjects/book_scanner/data/book_spines/1-side.jpg'

    extracted_text = extract_text_from_image(image_path)

    extracted_detail = extract_text_with_details(image_path)

    print(extracted_text)

    print(extracted_detail)