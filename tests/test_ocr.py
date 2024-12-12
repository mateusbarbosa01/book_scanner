import sys
sys.path.append('C:/Users/mateu/PycharmProjects/book_scanner')

import cv2


from ocr import *

print(extract_text_from_image('C:/Users/mateu/PycharmProjects/book_scanner/data/book_spines/1-side.jpg'))


# print(extract_text_with_details('C:/Users/mateu/PycharmProjects/book_scanner/data/book_spines/1-front.jpg'))

# print(pytesseract.image_to_string(Image.open('C:/Users/mateu/PycharmProjects/book_scanner/data/book_spines/1-front.jpg')))






#
# from PIL import Image
#
# print(pytesseract.image_to_string(Image.open('data/book_spines/3-front.jpg')))
#


