import streamlit as st
import os

# ናይቲ ገፅ ሽምን ኣቀማምጣን ምምዕርራይ
st.set_page_config(page_title="ናይ ቤተሰብ ማህደረ-መልክዕ", layout="wide")

# ሚስጢር ቃል (Password) መረጋገፂ ተግባር
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        # ቃለ-መእተዊ (Login) ገፅ
        st.title("🔐 ውሑስ ዝኾነ ገፅ")
        password = st.text_input("በጃኹም ናይ ስድራ ቤት ሚስጢር ቃል (Password) የእትዉ", type="password")
        
        if st.button("እተዉ"):
            if password == "1234": # እቲ ሚስጢር ቁፅሪ ኣብዚ ክትቅይሮ ትኽእል ኢኻ
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ ዝተጋገየ ሚስጢር ቃል! በጃኹም ደጊምኩም ፈትኑ።")
        return False
    return True

# ሚስጢር ቃል ትኽክል እንተኾይኑ ጥራሕ ስእልታት የርእይ
if check_password():
    st.title("📸 እንቋዕ ናብ ናይ ቤተሰብ ማህደረ-መልክዕ ብሰላም መፃእኹም!")
    st.write("---")

    # ስእልታት ዘለውሉ ቦታ ምርካብ
    photo_dir = "." 
    photos = [f for f in os.listdir(photo_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

    if photos:
        # ስእልታት ኣብ ሰለስተ መስርዕ (Columns) ከፊልካ ምርኣይ
        cols = st.columns(3)
        for index, photo in enumerate(sorted(photos)):
            with cols[index % 3]:
                st.image(photo, use_container_width=True, caption=f"ስእሊ: {photo}")
    else:
        st.warning("ኣብዚ ማህደር ዝተረኸበ ስእሊ የለን!")

    # መውፅኢ መጠወቂ (Logout)
    if st.sidebar.button("ውፃእ (Logout)"):
        st.session_state["password_correct"] = False
        st.rerun()
