import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Open camera"):
    camera_image = st.camera_input("Camera")
if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

with st.expander("Upload image"):
    upload_image = st.file_uploader("Upload Image")
if upload_image:
    uploaded_img = Image.open(upload_image)
    gray_uploaded_img = uploaded_img.convert("L")
    st.image(gray_uploaded_img)

