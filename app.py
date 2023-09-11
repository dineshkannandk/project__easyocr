from PIL import Image
import streamlit as st
import easyocr as oc
import pandas as pd
import time
import os
import io

st.set_page_config(page_title='Business Card',
                   page_icon='🎴',
                   layout='centered')

st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fil=Image.open('./1.png')

col1,col2=st.columns([1,2])

# Initialize EasyOCR reader
reader = oc.Reader(['en'], gpu=False)

# File upload section
st.markdown("# Welcome to the File Reader")

#f1 = st.file_uploader(':file_folder: **Upload a file** ', type=["jpg", "png", "jpeg"])


# Display a label and file uploader widget
uploaded_file = st.file_uploader("Upload a file", type=["jpg", "png", "jpeg"])
      

if uploaded_file is not None:
    st.image(uploaded_file)
    n=uploaded_file.name
    result=reader.readtext(n)

    name=tuple(result[0])
    role=tuple(result[1])
    phone_number=tuple(result[2])
    email=tuple(result[3])
    website=tuple(result[4])
    with st.expander(" # Click to see the details "):
            st.write( " Name :",name ) 
            st.write("# Role :",role) 
            st.write("# Phone_number :",phone_number) 
            st.write("# Email :",email)
            st.write("# Website :",website)  
else:
    st.write('Please upload the image')













    
    








# my_bar=st.progress(0,r=result)

#for r in range(100):
    #  time.sleep(0.1)
    #  my_bar.progress(r+1,r=result)
    #  st.success("File uploded sucessfully")


# st.expander("click Here to see the details of the card")

