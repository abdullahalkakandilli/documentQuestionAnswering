import pandas as pd
import streamlit as st
from transformers import pipeline
from functionforDownloadButtons import download_button
from PIL import Image
import pytesseract



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

st.set_page_config(page_icon="✂️", page_title="Question to Image")


c2, c3 = st.columns([6, 1])


with c2:
    c31, c32 = st.columns([12, 2])
    with c31:
        st.caption("")
        st.title("Question to Image")
    with c32:
        st.image(
            "images/logo.png",
            width=200,
        )

images_ = st.file_uploader("Upload Images", type=["png","jpg","jpeg"], accept_multiple_files=True)
# Convert PDF to JPG

df = pd.DataFrame()
image_name = []
answer_list = []
def image_checker(question_):

    try:
        nlp = pipeline(
            "document-question-answering",
            model="impira/layoutlm-document-qa",
        )
        if images_ is not None:
            for image in images_:
                image_opened = Image.open(image)
                st.write(image_opened)
                result = nlp(
                    image_opened,
                    question_
                )
                image_name.append(image.name)
                answer_list.append(result[0]['answer'])


            df['Image_name'] = image_name
            df[question_] = answer_list

            st.video('https://youtu.be/GXSWg_1dRrk')
            st.stop()

    except:
        st.write("Upload image")

    return (df)

form = st.form(key="annotation")
with form:
    question_ = st.text_input("Enter your query!")
    questions_ = st.text_area
    submitted = st.form_submit_button(label="Submit")

answer_ = pd.DataFrame()
if submitted:

    answer_ = image_checker(questions_)


c29, c30, c31 = st.columns([1, 1, 2])

with c29:

    CSVButton = download_button(
        answer_,
        "FlaggedFile.csv",
        "Download tos CSV",
    )

c6, c7, c8 = st.columns([1, 6, 1])

with c7:
    st.video('https://youtu.be/GXSWg_1dRrk')