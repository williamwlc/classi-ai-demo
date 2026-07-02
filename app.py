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

# Custom CSS - COMPACT VERSION
st.markdown("""
<style>
    .main-header {
        text-align: center;
        font-size: 2rem;
        color: #ffffff;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        text-align: center;
        font-size: 1rem;
        color: #aaa;
        margin-bottom: 1rem;
    }
    .company-intro {
        background: linear-gradient(135deg, #1e1e2e 0%, #2a2a3a 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .status-box {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        background: #1e1e2e;
        min-height: 80px;
    }
    .dev-note {
        position: fixed;
        top: 50px;
        right: 10px;
        background: rgba(30, 30, 46, 0.95);
        padding: 8px 12px;
        border-radius: 6px;
        border-left: 3px solid #667eea;
        font-size: 0.75rem;
        color: #aaa;
        z-index: 9999;
        max-width: 350px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        line-height: 1.4;
    }
    .invitation {
        background: linear-gradient(135deg, #667eea20 0%, #764ba220 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        text-align: center;
        border: 2px solid #667eea;
    }
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    h1, h2, h3, p { margin-bottom: 0.5rem !important; }
    .stMarkdown { margin-bottom: 0.2rem !important; }
</style>
""", unsafe_allow_html=True)

# Development Note - Top Right (CLEAN - NO TIMESTAMP)
st.markdown("""
<div class="dev-note">
    <strong style="color: #667eea;">📌 Dev Demo</strong><br>
    Domain masking enabled for clean URL display<br>
    Production migration planned on Google Cloud
</div>
""", unsafe_allow_html=True)

# Password Protection - Short Width (using columns)
pwd_col1, pwd_col2 = st.columns([1, 5])
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
            st.error("⏰ Session expired (30 min). Refresh for new session.")
            st.stop()
        else:
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            st.info(f"⏱️ {minutes}:{seconds:02d} left")

# Minimal spacing
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Experience the difference in real-world voice recognition</p>', unsafe_allow_html=True)

# Company Introduction (COMPACT)
st.markdown("""
<div class="company-intro">
    <h2 style="color: #667eea; margin-top: 0; font-size: 1.5rem;">About Classi AI</h2>
    <p style="font-size: 0.95rem; line-height: 1.5; margin-bottom: 0.5rem;">
        Classi AI is redefining how the world bridges language barriers. While leading applications 
        merely guess at your words, we comprehend the true context of your conversation. 
        Powered by our proprietary <strong>Universal Fluency Layer</strong>, our voice-to-text engine 
        thrives in real-world environments where background noise, heavy accents, idioms, and 
        code-switching cause competitor accuracy to plummet by 30%, 40%, or even more.
    </p>
    <p style="font-size: 0.95rem; line-height: 1.5; margin-bottom: 0;">
        Beyond transcription, Classi's revolutionary SaaS platform is engineered to meet the needs 
        of over 1 billion non-native learners globally through interactive learning, real-time AI 
        coaching, and precision pronunciation guidance.
    </p>
</div>
""", unsafe_allow_html=True)

# Invitation Message (COMPACT)
st.markdown("""
<div class="invitation">
    <h3 style="color: #667eea; margin-top: 0; font-size: 1.2rem;">🚀 Join Our Vision</h3>
    <p style="font-size: 0.95rem; margin-bottom: 0.5rem;">
        We're seeking strategic partners and investors who share our vision of making 
        voice technology truly universal and accessible.
    </p>
    <p style="color: #aaa; margin-bottom: 0; font-size: 0.9rem;">
        <em>Try the demo below and experience the future of voice recognition.</em>
    </p>
</div>
""", unsafe_allow_html=True)

# WORKING AUDIO RECORDING - COMPACT
st.markdown("### 🎤 Upload Voice Recording")
st.info("📱 Desktop: Upload WAV/MP3/M4A | 🎙️ Or record on phone then upload")

uploaded_file = st.file_uploader("", type=['wav', 'mp3', 'm4a', 'ogg'], 
                                  label_visibility="collapsed")

if uploaded_file is not None:
    with st.spinner("🔄 Processing your voice..."):
        # Save uploaded file temporarily
        temp_path = Path(f"temp_{uploaded_file.name}")
        temp_path.write_bytes(uploaded_file.getvalue())
        
        # SIMULATE processing (REPLACE with your actual ASR + GDE)
        time.sleep(2)
        
        # Example corrections (REPLACE with actual logic)
        st.session_state.history.insert(0, {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'raw_text': "other of the danger trail flip stills etc",
            'corrected_text': "Author of the danger trail Philip Steels etc",
            'duration': f"{uploaded_file.size / 16000:.1f}s",
            'filename': uploaded_file.name
        })
        
        # Keep only last 10
        st.session_state.history = st.session_state.history[:10]
        
        # Clean up
        temp_path.unlink(missing_ok=True)
        
        st.success("✅ Voice processed!")
        st.rerun()

# Status Display
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="status-box">
        <h4 style="color: #ff4b4b; margin: 0;">🔴 Raw ASR (Stage 3)</h4>
        <p style="margin: 0.5rem 0 0 0; color: #aaa; min-height: 60px;">
            {}
        </p>
    </div>
    """.format("Waiting for voice input..." if not st.session_state.history else st.session_state.history[0]['raw_text']), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="status-box">
        <h4 style="color: #00ff88; margin: 0;">🟢 Corrected Output (Stage 5)</h4>
        <p style="margin: 0.5rem 0 0 0; color: #aaa; min-height: 60px;">
            {}
        </p>
    </div>
    """.format("Waiting for voice input..." if not st.session_state.history else st.session_state.history[0]['corrected_text']), unsafe_allow_html=True)

# History Section
st.markdown("---")
st.markdown("### 📜 Correction History (Last 10)")

if st.session_state.history:
    for i, item in enumerate(st.session_state.history):
        with st.expander(f"Entry {i+1} - {item['timestamp']} - {item['filename']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**🔴 Raw ASR:**")
                st.write(item['raw_text'])
            with col2:
                st.markdown("**🟢 Corrected:**")
                st.write(item['corrected_text'])
            st.caption(f"Duration: {item['duration']}")
else:
    st.info("🎤 No recordings yet. Upload an audio file above to start!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p style="margin: 0;"><strong>Classi AI</strong> - Bridging language barriers with precision</p>
    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Contact: info@classiaihk.com</p>
</div>
""", unsafe_allow_html=True)
