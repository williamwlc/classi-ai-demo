import streamlit as st
import time
from datetime import datetime
import hashlib
import os

# Page config
st.set_page_config(page_title="Classi AI - Voice Demo", layout="wide")

# Initialize session state
if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'history' not in st.session_state:
    st.session_state.history = []
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()
if 'accessed_ips' not in st.session_state:
    st.session_state.accessed_ips = set()

# SPECIAL PASSWORD for unlimited testing (change this!)
SPECIAL_PASSWORD = "ClassiDemo2024!"  # Share this with your partner/investors

# Session timeout: 30 minutes (1800 seconds)
SESSION_TIMEOUT = 1800

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        font-size: 2.5rem;
        color: #FF4B4B;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        font-size: 1.2rem;
        color: #aaa;
        margin-bottom: 2rem;
    }
    .company-intro {
        background: linear-gradient(135deg, #1e1e2e 0%, #2a2a3a 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border-left: 5px solid #667eea;
    }
    .mic-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 3rem 0;
    }
    .mic-icon {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .mic-icon.recording {
        animation: pulse 1.5s ease-in-out infinite;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    .status-box {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        background: #1e1e2e;
        min-height: 120px;
    }
    .history-item {
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
        background: #2a2a3a;
        border-radius: 5px;
    }
    .dev-note {
        position: fixed;
        top: 10px;
        right: 10px;
        background: rgba(30, 30, 46, 0.95);
        padding: 12px 18px;
        border-radius: 8px;
        border-left: 3px solid #667eea;
        font-size: 0.85rem;
        color: #aaa;
        z-index: 9999;
        max-width: 380px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .invitation {
        background: linear-gradient(135deg, #667eea20 0%, #764ba220 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 2rem 0;
        text-align: center;
        border: 2px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Development Note (Top Right)
st.markdown("""
<div class="dev-note">
    <strong style="color: #667eea;">📌 Development Demo</strong><br>
    Hosted on Streamlit Cloud for rapid iteration.<br>
    Access: <strong>ClassiAIhk.com</strong> | 
    Production migration planned on Google Cloud
</div>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Experience the difference in real-world voice recognition</p>', unsafe_allow_html=True)

# Company Introduction
st.markdown("""
<div class="company-intro">
    <h2 style="color: #667eea; margin-top: 0;">About Classi AI</h2>
    <p style="font-size: 1.05rem; line-height: 1.6;">
        Classi AI is redefining how the world bridges language barriers. While leading applications 
        merely guess at your words, we comprehend the true context of your conversation. 
        Powered by our proprietary <strong>Universal Fluency Layer</strong>, our voice-to-text engine 
        thrives in real-world environments where background noise, heavy accents, idioms, and 
        code-switching cause competitor accuracy to plummet by 30%, 40%, or even more.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 0;">
        Beyond transcription, Classi's revolutionary SaaS platform is engineered to meet the needs 
        of over 1 billion non-native learners globally through interactive learning, real-time AI 
        coaching, and precision pronunciation guidance.
    </p>
</div>
""", unsafe_allow_html=True)

# Invitation Message
st.markdown("""
<div class="invitation">
    <h3 style="color: #667eea; margin-top: 0;">🚀 Join Our Vision</h3>
    <p style="font-size: 1.1rem; margin-bottom: 1rem;">
        We're seeking strategic partners and investors who share our vision of making 
        voice technology truly universal and accessible.
    </p>
    <p style="color: #aaa; margin-bottom: 0;">
        <em>Try the demo below and experience the future of voice recognition.</em>
    </p>
</div>
""", unsafe_allow_html=True)

# Password Protection
password = st.sidebar.text_input("🔐 Access Password", type="password")

if password:
    if password == SPECIAL_PASSWORD:
        st.sidebar.success("✅ Unlimited access granted!")
        st.session_state.session_timeout = None  # No timeout for special password
    else:
        # Regular user - check session timeout
        elapsed = time.time() - st.session_state.session_start
        remaining = SESSION_TIMEOUT - elapsed
        
        if elapsed > SESSION_TIMEOUT:
            st.error("⏰ Session expired (30 minutes). Please refresh for a new session.")
            st.stop()
        else:
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            st.sidebar.info(f"⏱️ Session: {minutes}:{seconds:02d} remaining")

# IP Tracking (simple implementation)
user_ip = st.context.headers.get("X-Real-IP", "unknown") if hasattr(st, 'context') else "unknown"
ip_hash = hashlib.md5(user_ip.encode()).hexdigest()

if ip_hash in st.session_state.accessed_ips and 'first_visit' not in st.session_state:
    st.warning("⚠️ One demo session per visitor. Thank you for your interest!")
    st.stop()
else:
    st.session_state.accessed_ips.add(ip_hash)
    st.session_state.first_visit = False

# Voice Recording Component
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Microphone Icon
    mic_class = "mic-icon recording" if st.session_state.recording else "mic-icon"
    st.markdown(f"""
    <div class="mic-container">
        <div class="{mic_class}">
            <svg width="80" height="80" viewBox="0 0 24 24" fill="white">
                <path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/>
                <path d="M17 11c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/>
            </svg>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Recording Controls
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🎤 Start Recording", use_container_width=True, type="primary", disabled=st.session_state.recording):
            st.session_state.recording = True
            st.rerun()
    
    with col_b:
        if st.button("⏹️ Stop Recording", use_container_width=True, disabled=not st.session_state.recording):
            st.session_state.recording = False
            # SIMULATED transcription (replace with your actual ASR logic)
            st.session_state.history.insert(0, {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'raw_text': "This is simulated raw ASR output",
                'corrected_text': "This is corrected output from Classi AI",
                'duration': "3.2s"
            })
            # Keep only last 10
            st.session_state.history = st.session_state.history[:10]
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
        with st.expander(f"Entry {i+1} - {item['timestamp']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**🔴 Raw ASR:**")
                st.write(item['raw_text'])
            with col2:
                st.markdown("**🟢 Corrected:**")
                st.write(item['corrected_text'])
            st.caption(f"Duration: {item['duration']}")
else:
    st.info("🎤 No history yet. Click 'Start Recording' to begin!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p style="margin: 0;"><strong>Classi AI</strong> - Bridging language barriers with precision</p>
    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Contact: info@classiaihk.com</p>
</div>
""", unsafe_allow_html=True)
