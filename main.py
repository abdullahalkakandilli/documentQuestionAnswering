from io import BytesIO
from pathlib import Path
import PyPDF2
from PIL import Image
import streamlit as st
import pandas as pd
import tempfile
from functionforDownloadButtons import download_button
from pdf2image import convert_from_path
import pytesseract
from transformers import pipeline
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="✂️", page_title="Logo or Not Logo")


c2, c3 = st.columns([6, 1])


with c2:
    c31, c32 = st.columns([12, 2])
    with c31:
        st.caption("")
        st.title("Logo or Not Logo")
    with c32:
        st.image(
            "images/logo.png",
            width=200,
        )

'''uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file is not None:
    # Make temp file path from uploaded file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        st.markdown("## Original PDF file")
        fp = Path(tmp_file.name)
        fp.write_bytes(uploaded_file.getvalue())
        imgs = convert_from_path(tmp_file.name, 500, poppler_path='poppler-0.68.0/bin')
        imgs[0].save('.jpg', 'JPEG')
        st.markdown(f"Converted images from PDF")
        st.image(imgs)'''

pdf_file = st.file_uploader("Upload PDF", type="pdf")

# Convert PDF to JPG
if pdf_file is not None:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    page = pdf_reader.getPage(0) # Get the first page
    png_image = page.get('/Resources').get('/XObject').getObject().values()[0].getData()

    # Convert the PNG image to a PIL image
    pil_image = Image.open(BytesIO(png_image))

    # Display the converted image
    st.image(pil_image, caption="Converted Image", use_column_width=True)


    # Display the converted image

else:
    st.info(
        f"""
            👆 Upload a .csv file first. Sample to try: [biostats.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv)
            """
    )

    st.stop()

def pdf_checker(question_):
    nlp = pipeline(
        "document-question-answering",
        model="impira/layoutlm-document-qa",
    )

    result = nlp(
        "page.jpg",
        question_
    )
    return (result)

form = st.form(key="annotation")
with form:
    question_ = st.text_input()

    submitted = st.form_submit_button(label="Submit")


if submitted:

    answer = pdf_checker(question_)


c29, c30, c31 = st.columns([1, 1, 2])

with c29:
    st.write(answer)
