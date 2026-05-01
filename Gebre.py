import streamlit as st
import os

# የገጹን ስም እና አቀማመጥ ማስተካከል
st.set_page_config(page_title="የቤተሰብ ፎቶ ጋለሪ", layout="wide")

st.title("📸 እንኳን ወደ ቤተሰባችን የፎቶ ጋለሪ በሰላም መጡ!")
st.write("---")

# ፎቶዎቹ ያሉበትን ቦታ መፈለግ (በዋናው ፎልደር ውስጥ)
photo_dir = "." 
# በሪፖዚተሪህ ውስጥ ያሉትን ፎቶዎች መለየት
photos = [f for f in os.listdir(photo_dir) if f.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG'))]

if photos:
    # ፎቶዎቹን በሶስት ረድፍ (Columns) ከፋፍሎ ማሳየት
    cols = st.columns(3)
    for index, photo in enumerate(sorted(photos)):
        with cols[index % 3]:
            st.image(photo, use_container_width=True, caption=f"ፎቶ: {photo}")
else:
    st.warning("በዚህ የ GitHub ፎልደር (Repository) ውስጥ ምንም ፎቶ አልተገኘም! እባክህ ፎቶዎችን መጫንህን አረጋግጥ።")

st.write("---")
st.info("በ Gebre29 የተገነባ")
