import pdfplumber as pdfplumber
import streamlit as st
import pandas as pd
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
def extract_data(feed):
    data = []
    with pdfplumber.load(feed) as pdf:
        pages = pdf.pages
        for p in pages:
            data.append(p.extract_tables())
    return None

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    df = extract_data(uploaded_file)

st.write(df)

'''if uploaded_file is not None:
    image_ = convert_from_path(uploaded_file)
    image_[0].save('page' + '.jpg', 'JPEG')
    uploaded_file.seek(0)

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
'''