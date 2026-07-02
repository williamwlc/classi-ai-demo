import streamlit as st
import streamlit.components.v1 as components
import json
from datetime import datetime
import base64

import time

if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()

# Check if session expired (60 minutes = 3600 seconds)
if time.time() - st.session_state.session_start > 3600:
    st.error("Session expired. Please request a new access link.")
    st.stop()

# Page config
st.set_page_config(page_title="Classi AI - Voice Demo", layout="wide")

# Initialize session state
if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'history' not in st.session_state:
    st.session_state.history = []

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        font-size: 2.5rem;
        color: #FF4B4B;
        margin-bottom: 2rem;
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
    }
    .history-item {
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
        background: #2a2a3a;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
st.markdown("### Experience the difference in real-world voice recognition")

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
        if st.button("🎤 Start Recording", use_container_width=True, type="primary"):
            st.session_state.recording = True
            st.rerun()
    
    with col_b:
        if st.button("⏹️ Stop Recording", use_container_width=True, disabled=not st.session_state.recording):
            st.session_state.recording = False
            # Simulate transcription (replace with your actual ASR logic)
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
        <p style="margin: 0.5rem 0 0 0; color: #aaa;">
            {}
        </p>
    </div>
    """.format("Waiting for voice input..." if not st.session_state.history else st.session_state.history[0]['raw_text'] if st.session_state.history else "Waiting for voice input..."), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="status-box">
        <h4 style="color: #00ff88; margin: 0;">🟢 Corrected Output (Stage 5)</h4>
        <p style="margin: 0.5rem 0 0 0; color: #aaa;">
            {}
        </p>
    </div>
    """.format("Waiting for voice input..." if not st.session_state.history else st.session_state.history[0]['corrected_text'] if st.session_state.history else "Waiting for voice input..."), unsafe_allow_html=True)

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
    st.info("No history yet. Start recording to see corrections!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>Powered by Classi AI's Universal Fluency Layer</p>
    <p>Handling noise, accents, idioms, and code-switching with precision</p>
</div>
""", unsafe_allow_html=True)
