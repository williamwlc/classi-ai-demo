import streamlit as st
import time
from datetime import datetime

# Page config
st.set_page_config(page_title="Classi AI - Voice Demo", layout="wide")

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()
if 'recording' not in st.session_state:
    st.session_state.recording = False

# PASSWORDS
PUBLIC_PASSWORD = "postmvpsoon"
SPECIAL_PASSWORD = "Amd13751376Cc13751376)(*!@#"

SESSION_TIMEOUT = 1800

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0B132B !important;
    }
    .block-container {
        padding-top: 4rem !important;
        padding-bottom: 2rem !important;
    }
    .main-header {
        text-align: center;
        font-size: 2.8rem !important;
        color: #ffffff;
        margin: 1rem 0 0.5rem 0 !important;
        font-weight: 700;
    }
    .sub-header {
        text-align: center;
        font-size: 1.2rem !important;
        color: #8B9DC3;
        margin: 0 0 2rem 0 !important;
    }
    .company-intro, .status-box {
        background-color: #1C2541 !important;
        border: 1px solid #3A506B !important;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0 !important;
    }
    .company-intro {
        border-left: 5px solid #5BC0BE !important;
    }
    .company-intro h2 {
        font-size: 1.8rem !important;
        color: #5BC0BE !important;
        margin: 0 0 1rem 0 !important;
    }
    .company-intro p {
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
        color: #E0E1DD !important;
        margin: 0 !important;
    }
    /* Dev Note - SAME SMALL SIZE as password box */
    .dev-note {
        display: inline-block;
        background-color: #1C2541 !important;
        border: 1px solid #3A506B !important;
        padding: 0.4rem 0.8rem !important;
        border-radius: 6px !important;
        font-size: 0.8rem !important;
        color: #8B9DC3 !important;
        margin: 0.5rem 0 !important;
        line-height: 1.3 !important;
    }
    .status-box h4 {
        margin: 0 0 0.5rem 0 !important;
        font-size: 1.2rem !important;
    }
    .status-box p {
        color: #E0E1DD !important;
        font-size: 1rem !important;
        margin: 0 !important;
    }
    .stButton > button {
        background-color: #3A506B !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        font-size: 1rem !important;
        padding: 0.8rem !important;
    }
    .stButton > button:hover {
        background-color: #5BC0BE !important;
        color: #0B132B !important;
    }
    .stTextInput > div > div > input {
        background-color: #1C2541 !important;
        color: white !important;
        border: 1px solid #3A506B !important;
    }
    p, h1, h2, h3, h4 {
        color: #ffffff !important;
    }
    .stMarkdown p {
        color: #E0E1DD !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Experience real-world voice recognition</p>', unsafe_allow_html=True)

# Password Protection
pwd_col1, pwd_col2 = st.columns([1, 4])
with pwd_col1:
    password = st.text_input("", type="password", label_visibility="collapsed", 
                             key="pwd_top", placeholder="🔐 Access Password")

if password:
    if password == SPECIAL_PASSWORD:
        st.success("✅ Unlimited access granted!")
        st.session_state.session_timeout = None
    elif password == PUBLIC_PASSWORD:
        st.success("✅ Access granted! (1-hour test drive)")
    else:
        elapsed = time.time() - st.session_state.session_start
        remaining = SESSION_TIMEOUT - elapsed
        if elapsed > SESSION_TIMEOUT:
            st.error("⏰ Session expired (30 min)")
            st.stop()
        else:
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            st.info(f"⏱️ {minutes}:{seconds:02d}")

# Dev Note - SMALL BOX (same size as password input)
st.markdown("""
<div class="dev-note">
    📌 <strong>Dev Demo</strong> | ClassiAIhk.com via domain masking | Google Cloud migration planned
</div>
""", unsafe_allow_html=True)

# Company Introduction
st.markdown("""
<div class="company-intro">
    <h2>About Classi AI</h2>
    <p>
        Classi AI is redefining how the world bridges language barriers. While leading applications 
        merely guess at your words, we comprehend the true context. Powered by our proprietary 
        <strong>Universal Fluency Layer</strong>, our engine thrives where noise, accents, idioms, 
        and code-switching cause competitor accuracy to plummet by 30-45%.
    </p>
</div>
""", unsafe_allow_html=True)

# Recording Section
st.markdown("### 🎤 Record Voice")

col_rec1, col_rec2 = st.columns(2)
with col_rec1:
    if st.button("🔴 Start Recording", use_container_width=True, key="start_rec"):
        st.session_state.recording = True
        st.rerun()

with col_rec2:
    if st.button("⏹️ Stop Recording", use_container_width=True, key="stop_rec"):
        st.session_state.recording = False
        st.session_state.history.insert(0, {
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'raw_text': "other of the danger trail flip stills etc",
            'corrected_text': "Author of the danger trail Philip Steels etc",
            'duration': "3.2s"
        })
        st.session_state.history = st.session_state.history[:10]
        st.success("✅ Processed!")
        st.rerun()

if st.session_state.recording:
    st.markdown("<p style='color: #ff4b4b; text-align: center; font-weight: bold; font-size: 1.2rem;'>🔴 RECORDING IN PROGRESS... Click STOP when finished</p>", unsafe_allow_html=True)

# Status Display
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="status-box">
        <h4 style="color: #ff4b4b; margin: 0;">🔴 Raw ASR</h4>
        <p style="margin: 0; color: #aaa; font-size: 1rem;">
            {}
        </p>
    </div>
    """.format("Waiting..." if not st.session_state.history else st.session_state.history[0]['raw_text']), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="status-box">
        <h4 style="color: #00ff88; margin: 0;">🟢 Corrected</h4>
        <p style="margin: 0; color: #aaa; font-size: 1rem;">
            {}
        </p>
    </div>
    """.format("Waiting..." if not st.session_state.history else st.session_state.history[0]['corrected_text']), unsafe_allow_html=True)

# History
if st.session_state.history:
    st.markdown("### 📜 History of Rolling Last 10 Text Transcriptions")
    for i, item in enumerate(st.session_state.history[:10]):
        with st.expander(f"#{i+1} - {item['timestamp']} - {item.get('duration', 'N/A')}", expanded=(i==0)):
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("**🔴 Raw ASR:**")
                st.write(item['raw_text'])
            with col_b:
                st.markdown("**🟢 Corrected:**")
                st.write(item['corrected_text'])

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #8B9DC3; font-size: 0.9rem; margin-top: 2rem;">
    <p>© 2026 Classi AI. All rights reserved. | Contact: <strong>William@ClassiAIhk.com</strong></p>
</div>
""", unsafe_allow_html=True)
