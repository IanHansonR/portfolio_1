import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

st.title("Ian Hanson's Python Portfolio")
st.subheader("About Me")
st.write("Welcome to my python portfolio. Here I have compiled all the "
         "projects I have made to date. All projects can be accessed "
         "through the navigation menu on the upper left-hand side of the "
         "page. I am working towards becoming a python developer with a "
         "focus on automation and machine learning.")
image = Image.open("/Users/ianhanson/Library/Mobile Documents/"
                   "com~apple~CloudDocs/Images/IMG_0584.JPG")
st.image(image, use_column_width=True)

