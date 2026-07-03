import streamlit as st
import time
from datetime import datetime
from pathlib import Path

# Page config
st.set_page_config(page_title="Classi AI - Voice Demo", layout="wide")

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()
if 'recording' not in st.session_state:
    st.session_state.recording = False

# SPECIAL PASSWORD for unlimited testing
SPECIAL_PASSWORD = "ClassiDemo2024!"

# Session timeout: 30 minutes
SESSION_TIMEOUT = 1800

# Custom CSS - COMPACT LAYOUT
st.markdown("""
<style>
    .main-header {
        text-align: center;
        font-size: 2.5rem !important;
        color: #ffffff;
        margin: 0 !important;
        padding: 0 !important;
    }
    .sub-header {
        text-align: center;
        font-size: 1.1rem !important;
        color: #aaa;
        margin: 0.3rem 0 1rem 0 !important;
    }
    .company-intro {
        background: linear-gradient(135deg, #1e1e2e 0%, #2a2a3a 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0 !important;
        border-left: 4px solid #667eea;
    }
    .company-intro h2 {
        font-size: 1.5rem !important;
        color: #667eea;
        margin: 0 0 0.5rem 0 !important;
    }
    .company-intro p {
        font-size: 1rem !important;
        line-height: 1.5 !important;
        margin: 0 !important;
    }
    .password-wrapper {
        margin: 0.5rem 0 !important;
        padding: 0 !important;
    }
    .dev-note {
        text-align: center;
        background: rgba(30, 30, 46, 0.95);
        padding: 0.5rem;
        border-radius: 6px;
        border-left: 3px solid #667eea;
        font-size: 0.75rem;
        color: #aaa;
        margin: 0.5rem 0 !important;
    }
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0.5rem !important;
    }
    section.main > div {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    h1 {
        margin: 0 !important;
        font-size: 2.5rem !important;
        padding: 0 !important;
    }
    h2 {
        margin: 0 0 0.5rem 0 !important;
        font-size: 1.5rem !important;
    }
    h3 {
        margin: 0 0 0.4rem 0 !important;
        font-size: 1.2rem !important;
    }
    p {
        margin: 0.3rem 0 !important;
        line-height: 1.5;
        font-size: 1rem !important;
    }
    .status-box {
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.3rem 0;
        background: #1e1e2e;
        min-height: 70px;
    }
    .status-box h4 {
        margin: 0 0 0.4rem 0 !important;
        font-size: 1.1rem !important;
    }
    .upload-section {
        margin: 0.8rem 0 !important;
        padding: 0.5rem 0 !important;
    }
    .history-section {
        margin: 0.8rem 0 !important;
        padding: 0.5rem 0 !important;
    }
    .stFileUploader {
        margin: 0.3rem 0 !important;
        padding: 0 !important;
    }
    .record-buttons {
        display: flex;
        gap: 1rem;
        margin: 0.8rem 0;
    }
    .record-buttons button {
        flex: 1;
        padding: 0.8rem !important;
        font-size: 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Header - VERY TOP
st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Experience real-world voice recognition</p>', unsafe_allow_html=True)

# Password Protection
st.markdown('<div class="password-wrapper">', unsafe_allow_html=True)
pwd_col1, pwd_col2 = st.columns([1, 4])
with pwd_col1:
    password = st.text_input("", type="password", label_visibility="collapsed", 
                             key="pwd_top", placeholder="🔐 Access Password")

if password:
    if password == SPECIAL_PASSWORD:
        st.success("✅ Unlimited access!")
        st.session_state.session_timeout = None
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
st.markdown('</div>', unsafe_allow_html=True)

# Dev Note - BELOW PASSWORD (no timestamp)
st.markdown("""
<div class="dev-note">
    <strong style="color: #667eea;">📌 Dev Demo</strong> | Displaying ClassiAIhk.com via domain masking | Production migration planned on Google Cloud
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
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown("### 🎤 Record or Upload Voice")

# Recording buttons
col_rec1, col_rec2 = st.columns(2)
with col_rec1:
    if st.button("🔴 Start Recording", use_container_width=True, key="start_rec"):
        st.session_state.recording = True
        st.rerun()

with col_rec2:
    if st.button("⏹️ Stop Recording", use_container_width=True, key="stop_rec"):
        st.session_state.recording = False
        # Simulate processing (replace with actual GDE call)
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
    st.markdown("<p style='color: #ff4b4b; text-align: center; font-weight: bold;'>🔴 RECORDING IN PROGRESS... Click STOP when finished</p>", unsafe_allow_html=True)

# File upload fallback
uploaded_file = st.file_uploader("Or upload audio file", type=['wav', 'mp3', 'm4a', 'ogg'], 
                                  label_visibility="collapsed", key="file_upload")

if uploaded_file is not None:
    with st.spinner("🔄 Processing..."):
        temp_path = Path(f"temp_{uploaded_file.name}")
        temp_path.write_bytes(uploaded_file.getvalue())
        time.sleep(2)
        
        # HERE: Call your actual GDE engine
        # raw_text, corrected_text = process_audio(temp_path)
        
        st.session_state.history.insert(0, {
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'raw_text': f"Processed {uploaded_file.name}",
            'corrected_text': "GDE correction will appear here",
            'duration': f"{uploaded_file.size / 16000:.1f}s"
        })
        st.session_state.history = st.session_state.history[:10]
        temp_path.unlink(missing_ok=True)
        st.success("✅ Processed!")
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Status Display
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="status-box">
        <h4 style="color: #ff4b4b; margin: 0;">🔴 Raw ASR</h4>
        <p style="margin: 0; color: #aaa; font-size: 0.95rem;">
            {}
        </p>
    </div>
    """.format("Waiting..." if not st.session_state.history else st.session_state.history[0]['raw_text']), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="status-box">
        <h4 style="color: #00ff88; margin: 0;">🟢 Corrected</h4>
        <p style="margin: 0; color: #aaa; font-size: 0.95rem;">
            {}
        </p>
    </div>
    """.format("Waiting..." if not st.session_state.history else st.session_state.history[0]['corrected_text']), unsafe_allow_html=True)

# History Section - Last 10 Transcriptions
if st.session_state.history:
    st.markdown('<div class="history-section">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.85rem; margin: 0.5rem 0;">
    <p>© 2026 Classi AI. All rights reserved. | Contact: <strong>William@ClassiAIhk.com</strong></p>
</div>
""", unsafe_allow_html=True)
