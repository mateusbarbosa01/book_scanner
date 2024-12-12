from PIL import Image

import pytesseract

# print(pytesseract.image_to_string(Image.open('data/book_spines/1-front.jpg')))


print(pytesseract.image_to_string(Image.open('data/book_spines/3-front.jpg')))











