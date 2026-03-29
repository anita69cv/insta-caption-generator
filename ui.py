import streamlit as st
from app import generate_captions
from PIL import Image

st.set_page_config(page_title="AI Caption Generator", layout="centered")

st.title("📸 AI Instagram Caption Generator")

st.write("Upload an image and get captions instantly!")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=400)

    if st.button("✨ Generate Captions"):
        # Save image temporarily
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("AI is thinking... 🤖"):
            description, captions = generate_captions("temp.jpg")

        st.subheader("🧠 Image Understanding")
        st.write(description)

        st.subheader("✨ Captions")
        st.write(captions)