# **Book Scanner Project**

This project is a Python-based application designed to
identify and extract text from book spines using OCR (Optical Character Recognition). The system preprocesses images of bookshelves, performs OCR to recognize book titles, authors, and other relevant details, and outputs the results in an easily accessible format.

---

## **Features**
- Preprocesses images for better OCR accuracy (e.g., grayscaling, thresholding).
- Extracts text from book spines using Tesseract OCR.
- Modular code structure for easy maintenance and scalability.
- Supports additional functionality like fuzzy matching and affiliate link generation (optional).



## **Project Structure**

```
book_scanner/
├── main.py              # Main script to run the project
├── ocr.py               # Handles OCR functionality
├── image_processing.py  # Prepares and processes images
├── requirements.txt     # Dependencies for the project
├── README.md            # Project documentation
├── tests/               # Unit tests for modules
│   ├── test_ocr.py      # Tests for OCR functionality
│   ├── test_image_processing.py  # Tests for image processing
└── data/                # Stores sample images for testing
    └── book_spines/
```


## **Setup Instructions**

### **1. Install dependencies**
Make sure Python *XXX* is installed. Use the following commands to set up your environment:

1. Clone the repository:

```python
git clone https://github.com/mateusbarbosa01/book_scanner
cd book_scanner
```
2. Create and activate a virtual environment:


```python 
-m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

3. Install dependencies:

```python
pip install -r requirements.txt
```

### **2. Install Tesseract**
Windows: Download and install Tesseract from UB Mannheim.

Linux/Mac: Install Tesseract using a package manager:
```
sudo apt-get install tesseract-ocr  # Ubuntu/Debian
brew install tesseract              # MacOS
```

Install pytesseract:
```
pip install pytesseract
```
