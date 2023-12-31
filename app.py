import streamlit as st
import pandas as pd
import pytesseract
import PIL.Image
import cv2

st.set_page_config(page_title="Text Extractor")


st.title('Welcome To,')
st.subheader('OptiScripter')
myconfig = r"--psm 6 --oem 3"

df = st.file_uploader(label='Upload The Text with Image File Here : ')

if df:
    text = pytesseract.image_to_string(PIL.Image.open(df), config=myconfig)
    st.write(text)



st.markdown("""
<style>
    body {
        background: linear-gradient(to right, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D, #F56040, #FF9F40);
        color: white; /* Text color */
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #282c34; /* Dark background color */
        padding: 10px;
        text-align: center;
        color: white; /* Text color */
    }
    .social-links {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 10px;
    }
    .social-link {
        margin: 0 15px;
        color: #61dafb; /* Social link color */
        text-decoration: none;
        transition: color 0.3s ease-in-out;
    }
    .social-link:hover {
        color: #ff8c00; /* Hover color */
    }
</style>
<div class="footer">
    <p>Thanks For Using OptiScripter!</p>
    <p> Feel Free To Contact Us Using Below Links !!!!</p>
    <div class="social-links">
        <a href="https://linktr.ee/debanga_prasad07" class="social-link" target="_blank">Linktree</a>
        <a href="https://www.instagram.com/debanga_prasad/" class="social-link" target="_blank">Instagram</a>
        <a href="https://www.linkedin.com/in/debangaprasad/" class="social-link" target="_blank">LinkedIn</a>
        <a href="https://leetcode.com/Debanga_prasad_07/" class="social-link" target="_blank">LeetCode</a>
        <a href="https://github.com/Justmephoenix" class="social-link" target="_blank">GitHub</a>
        <!-- Add more social links as needed -->
    </div>
</div>
""", unsafe_allow_html=True)

