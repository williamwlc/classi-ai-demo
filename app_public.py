import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Classi AI - Voice Demo", layout="wide")

# Initialize session state
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()

# PUBLIC PASSWORD (share with interested parties)
PUBLIC_PASSWORD = "postmvpsoon"

# Session timeout: 60 minutes for public users
SESSION_TIMEOUT = 3600

current_time = datetime.now().strftime("%H:%M:%S")

st.markdown("""
<style>
    .main-header { text-align: center; font-size: 2rem; margin: 0 !important; }
    .sub-header { text-align: center; color: #aaa; margin: 0.3rem 0 1rem 0 !important; }
    .dev-note {
        position: fixed; top: 10px; right: 10px;
        background: rgba(30, 30, 46, 0.95);
        padding: 6px 10px; border-radius: 6px;
        font-size: 0.7rem; color: #aaa; z-index: 9999;
    }
    .block-container { padding-top: 0.5rem !important; }
    h1 { margin: 0 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="dev-note">
    <strong>📌 Dev Demo</strong><br>
    Displaying ClassiAIhk.com via domain masking<br>
    <span style="color: #555;">{current_time}</span>
</div>
""", unsafe_allow_html=True)

# Password Protection
password = st.text_input("🔐 Enter Password", type="password", key="public_pwd")

if password:
    if password == PUBLIC_PASSWORD:
        st.success("✅ Access granted!")
        
        # Check session timeout
        elapsed = time.time() - st.session_state.session_start
        remaining = SESSION_TIMEOUT - elapsed
        
        if elapsed > SESSION_TIMEOUT:
            st.error("⏰ Session expired (60 minutes). Please refresh.")
            st.stop()
        else:
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            st.info(f"⏱️ Session: {minutes}:{seconds:02d} remaining")
        
        st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Experience real-world voice recognition</p>', unsafe_allow_html=True)

        st.markdown("""
        ### About Classi AI
        Classi AI redefines voice recognition with our **Universal Fluency Layer**, handling noise, 
        accents, and idioms where competitors fail by 30-45%.

        ### Seeking Partners
        We're looking for strategic partners and investors. Contact: info@classiaihk.com
        
        ---
        **Note:** This is a read-only demo. For full access with voice upload capabilities, 
        please contact us directly.
        """)
    else:
        st.error("❌ Incorrect password. Please contact us for access.")
else:
    st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Experience real-world voice recognition</p>', unsafe_allow_html=True)
    st.info("🔒 **Password Required** - Please enter the password above to view the demo.")
    
    st.markdown("""
    ### About Classi AI
    Classi AI is redefining voice recognition technology with our proprietary **Universal Fluency Layer**.
    
    **Interested?** Enter the password above or contact us at info@classiaihk.com
    """)
