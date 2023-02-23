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

uploaded_file = st.file_uploader(
    " ",
    key="1",
    help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
)

if uploaded_file is not None:
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
