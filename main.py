import pandas as pd
import streamlit as st
from transformers import pipeline
from functionforDownloadButtons import download_button
from PIL import Image



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

images_ = st.file_uploader("Upload PDF", type=["png","jpg","jpeg"], accept_multiple_files=True)
# Convert PDF to JPG

df = pd.DataFrame(columns=['Image', 'Answer'])
def image_checker(question_):
    nlp = pipeline(
        "document-question-answering",
        model="impira/layoutlm-document-qa",
    )
    if images_ is not None:
        for image in images_:
            image_opened = Image.open(image)
            result = nlp(
                image_opened,
                question_
            )
            new_row = {'Image': image, 'Answer': result}
            df = df.append(new_row, ignore_index=True)
    else:
        st.info(
            f"""
                👆 Upload a .csv file first. Sample to try: [biostats.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv)
                """
        )

        st.stop()

    return (df)

import os

filenames = os.listdir('.')
selected_filename = st.selectbox('Select a file', filenames)


form = st.form(key="annotation")
with form:
    question_ = st.text_input("Enter your query!")

    submitted = st.form_submit_button(label="Submit")


if submitted:

    answer = image_checker(question_)


c29, c30, c31 = st.columns([1, 1, 2])

with c29:

    CSVButton = download_button(
        df,
        "FlaggedFile.csv",
        "Download to CSV",
    )

