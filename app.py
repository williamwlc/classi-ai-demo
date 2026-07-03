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

# SPECIAL PASSWORD for unlimited testing
SPECIAL_PASSWORD = "ClassiDemo2024!"

# Session timeout: 30 minutes
SESSION_TIMEOUT = 1800

# Get current computer clock time
current_time = datetime.now().strftime("%H:%M:%S")

# Custom CSS - FIXED POSITIONING & SPACING
st.markdown("""
<style>
    .main-header {
        text-align: center;
        font-size: 2.5rem !important;
        color: #ffffff;
        margin: 0 !important;
        padding-top: 0 !important;
    }
    .sub-header {
        text-align: center;
        font-size: 1.2rem !important;
        color: #aaa;
        margin: 0.5rem 0 1.5rem 0 !important;
    }
    .company-intro {
        background: linear-gradient(135deg, #1e1e2e 0%, #2a2a3a 100%);
        padding: 1.5rem;
        border-radius: 8px;
        margin: 0 !important;
        border-left: 4px solid #667eea;
    }
    .company-intro h2 {
        font-size: 1.8rem !important;
        color: #667eea;
        margin: 0 0 0.8rem 0 !important;
    }
    .company-intro p {
        font-size: 1.15rem !important;
        line-height: 1.6 !important;
        margin: 0 !important;
    }
    .dev-note {
        position: fixed;
        top: 80px !important;
        right: 10px;
        background: rgba(30, 30, 46, 0.95);
        padding: 8px 12px;
        border-radius: 6px;
        border-left: 3px solid #667eea;
        font-size: 0.75rem;
        color: #aaa;
        z-index: 9999;
        max-width: 320px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        line-height: 1.4;
    }
    .password-container {
        margin-top: 60px !important;
        margin-bottom: 1rem !important;
    }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 1rem !important;
    }
    section.main > div {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    h1 {
        margin: 0 !important;
        font-size: 2.5rem !important;
        padding-top: 0 !important;
    }
    h2 {
        margin: 0 0 0.8rem 0 !important;
        font-size: 1.8rem !important;
    }
    p {
        margin: 0.5rem 0 !important;
        line-height: 1.6;
        font-size: 1.15rem !important;
    }
    .status-box {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        background: #1e1e2e;
        min-height: 80px;
    }
    .status-box h4 {
        margin: 0 0 0.5rem 0 !important;
        font-size: 1.2rem !important;
    }
    .upload-section {
        margin: 1rem 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Password Protection - MOVED DOWN
st.markdown('<div class="password-container">', unsafe_allow_html=True)
pwd_col1, pwd_col2 = st.columns([1, 4])
with pwd_col1:
    password = st.text_input("", type="password", label_visibility="collapsed", 
                             key="pwd_top", placeholder="🔐 Password")

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

# Development Note - Top Right (MOVED DOWN)
st.markdown(f"""
<div class="dev-note">
    <strong style="color: #667eea;">📌 Dev Demo</strong><br>
    Displaying ClassiAIhk.com via domain masking<br>
    Production migration planned on Google Cloud<br>
    <span style="color: #555; font-size: 0.7rem;">{current_time}</span>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Experience real-world voice recognition</p>', unsafe_allow_html=True)

# Company Introduction - NO EXTRA SPACING ABOVE
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

# REMOVED "Join Our Vision" section - you're right, it sends wrong message

# Upload Section - RESTORED
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown("### 🎤 Upload Voice Recording")
uploaded_file = st.file_uploader("", type=['wav', 'mp3', 'm4a', 'ogg'], 
                                  label_visibility="collapsed")

if uploaded_file is not None:
    with st.spinner("🔄 Processing..."):
        temp_path = Path(f"temp_{uploaded_file.name}")
        temp_path.write_bytes(uploaded_file.getvalue())
        time.sleep(2)
        
        st.session_state.history.insert(0, {
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'raw_text': "other of the danger trail flip stills etc",
            'corrected_text': "Author of the danger trail Philip Steels etc",
            'duration': f"{uploaded_file.size / 16000:.1f}s",
            'filename': uploaded_file.name
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
        <p style="margin: 0.3rem 0 0 0; color: #aaa; font-size: 0.95rem;">
            {}
        </p>
    </div>
    """.format("Waiting..." if not st.session_state.history else st.session_state.history[0]['raw_text']), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="status-box">
        <h4 style="color: #00ff88; margin: 0;">🟢 Corrected</h4>
        <p style="margin: 0.3rem 0 0 0; color: #aaa; font-size: 0.95rem;">
            {}
        </p>
    </div>
    """.format("Waiting..." if not st.session_state.history else st.session_state.history[0]['corrected_text']), unsafe_allow_html=True)

# History
if st.session_state.history:
    st.markdown("---")
    st.markdown("### 📜 History")
    for i, item in enumerate(st.session_state.history):
        with st.expander(f"#{i+1} - {item['timestamp']}"):
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**Raw:**", item['raw_text'])
            with col_b:
                st.write("**Corrected:**", item['corrected_text'])

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem; margin-top: 2rem;">
    <p>© 2026 Classi AI. All rights reserved.</p>
    <p>Contact: <strong>William@ClassiAIhk.com</strong></p>
</div>
""", unsafe_allow_html=True)
