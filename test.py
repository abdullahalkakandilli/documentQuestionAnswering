from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from transformers import pipeline
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
image_ = convert_from_path(r'C:\Users\alka\Masaüstü\testInvoice2.pdf', 500, poppler_path=r'D:\Program Files (x86)\poppler-0.68.0\bin')

image_[0].save('page' + '.jpg', 'JPEG')

nlp = pipeline(
    "document-question-answering",
    model="impira/layoutlm-document-qa",
)

result = nlp(
    "page.jpg",
    "What is the invoice number?"
)



