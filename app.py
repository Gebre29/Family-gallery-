import streamlit as st
from PIL import Image
import os

# 1. የገጽ አቀማመጥ (ለስልክ እንዲመች)
st.set_page_config(page_title="ናይ ስድራቤት ጋለሪ", layout="centered")

# 2. ፎቶዎችን መሰብሰብ
folder_path = "images"
photos = [f"{folder_path}/{img}" for img in os.listdir(folder_path) 
          if img.lower().endswith(('.jpg', '.jpeg', '.png', '.heic'))]
photos.sort()

# 3. የሚስጥር ቁጥር (Password) ማረጋገጫ
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("ናይ ስድራቤት መዝገብ")
    password = st.text_input("በጃኹም ሚስጥር ቃል የእትዉ", type="password")
    if st.button("እቶ"):
        if password == "1234": # ሚስጥር ቁጥርህን እዚህ ቀይር
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("ዝተጋገየ ሚስጥር ቃል!")
else:
    # 4. ዋናው የዌብሳይት ገጽ
    st.title("ናይ ስድራቤት ጋለሪ")

    if "index" not in st.session_state:
        st.session_state.index = 0

    # የፎቶ መቆጣጠሪያ ቁልፎች (ጎን ለጎን)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ ንድሕሪት"):
            st.session_state.index = (st.session_state.index - 1) % len(photos)
    
    with col3:
        if st.button("ንቅድሚት ➡️"):
            st.session_state.index = (st.session_state.index + 1) % len(photos)

    # ፎቶውን ማሳየት
    current_photo = photos[st.session_state.index]
    image = Image.open(current_photo)
    st.image(image, use_container_width=True)
    
    # መቁጠሪያ
    st.write(f"<p style='text-align: center;'>ስእሊ {st.session_state.index + 1} ካብ {len(photos)}</p>", unsafe_allow_html=True)