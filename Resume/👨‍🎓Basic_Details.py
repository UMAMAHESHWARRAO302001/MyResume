import streamlit as st
from PIL import Image

image = Image.open('Image.jpg')

PAGE_TITLE = "Digital CV | Umamahesh Yenamala"

PAGE_ICON = ":wave:"

resume_file = "Resume_.pdf"

NAME = "Umamahesh Yenamala"

DESCRIPTION = """
###### I am 21 years old and a Computer Science Enthusiast and a future seeker, and I love listening to tech-talks and to invent the new things by using the technologies. Most of the times what I do is just sit, drink coffee and learn a new technology. I am greatly into the new emerging.
"""

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

EMAIL = "yenamalaumamahesh@gmail.com"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(image, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("	:telephone_receiver: +91-9121263879")
    st.write("📫", EMAIL)

st.write('\n')

linkedin_url = "https://www.linkedin.com/in/umamahesh-yenamala-a20423197/"
github_url = "https://github.com/UMAMAHESHWARRAO302001"
medium_url = "https://medium.com/@yenamalaumamahesh"
    
col1, col2, col3 = st.columns(3)  # Create three columns for icons
    
with col1:
    st.markdown(f'[<img src="https://img.icons8.com/?size=512&id=13930&format=png" width=48 height=48>]({linkedin_url})', unsafe_allow_html=True)
        
with col2:
    st.markdown(f'[<img src="https://img.icons8.com/?size=512&id=16318&format=png" width=48 height=48>]({github_url})', unsafe_allow_html=True)
        
with col3:
    st.markdown(f'[<img src="https://img.icons8.com/?size=512&id=GlEHSV1RF10y&format=png" width=48 height=48>]({medium_url})', unsafe_allow_html=True)