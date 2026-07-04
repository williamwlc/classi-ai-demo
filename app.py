import streamlit as st
import time
from datetime import datetime
from transformers import pipeline
import os
from pathlib import Path

st.set_page_config(page_title="Classi AI - Voice Demo", layout="wide")

# Load lightweight AI model for real transcription
@st.cache_resource
def load_asr_model():
    return pipeline("automatic-speech-recognition", model="openai/whisper-tiny")

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()
if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'recording_start_time' not in st.session_state:
    st.session_state.recording_start_time = None

PUBLIC_PASSWORD = "postmvpsoon"
SPECIAL_PASSWORD = "Amd13751376Cc13751376)(*!@#"
SESSION_TIMEOUT = 1800

# Custom CSS with SLOWER blinking animation
st.markdown("""
<style>
    .stApp { background-color: #0B132B !important; }
    
    a.header-anchor { display: none !important; }
    
    .block-container { 
        padding-top: 2rem !important; 
        padding-bottom: 1rem !important; 
    }
    
    .main-header { 
        text-align: center; 
        font-size: 2.5rem !important; 
        color: #ffffff; 
        margin: 0.5rem 0 0.3rem 0 !important; 
    }
    
    .sub-header { 
        text-align: center; 
        font-size: 1.1rem !important; 
        color: #8B9DC3; 
        margin: 0 0 0.5rem 0 !important; 
    }
    
    .about-container { margin: 0 !important; padding: 0 !important; }
    .about-heading {
        font-size: 1.5rem !important;
        color: #5BC0BE !important;
        margin: 0 0 0.3rem 0 !important;
        font-weight: bold;
    }
    
    .company-intro { 
        background-color: #1C2541 !important; 
        border: 1px solid #3A506B !important; 
        border-left: 4px solid #5BC0BE !important;
        border-radius: 8px; 
        padding: 0.6rem 0.8rem !important;
        margin: 0 !important; 
    }
    
    .company-intro p { 
        font-size: 0.95rem !important; 
        line-height: 1.4 !important; 
        color: #E0E1DD !important; 
        margin: 0.2rem 0 !important; 
    }
    .company-intro p:first-child { margin-top: 0 !important; padding-top: 0 !important; }
    .company-intro p:last-child { margin-bottom: 0 !important; padding-bottom: 0 !important; }
    
    .dev-note { 
        display: inline-block; 
        background-color: #1C2541 !important; 
        border: 1px solid #3A506B !important; 
        padding: 0.2rem 0.5rem !important; 
        border-radius: 4px !important; 
        font-size: 0.75rem !important; 
        color: #8B9DC3 !important; 
        margin: 0.2rem 0 !important; 
    }
    
    .status-box { 
        background-color: #1C2541 !important; 
        border: 1px solid #3A506B !important; 
        border-radius: 6px; 
        padding: 0.5rem !important; 
        margin: 0.3rem 0 !important; 
    }
    
    .status-box h4 { margin: 0 0 0.3rem 0 !important; font-size: 1rem !important; }
    .status-box p { color: #E0E1DD !important; font-size: 0.9rem !important; margin: 0 !important; }
    
    .stButton > button { 
        background-color: #3A506B !important; 
        color: white !important; 
        border: none !important; 
        border-radius: 4px !important; 
        font-size: 0.9rem !important; 
        padding: 0.5rem !important; 
        margin: 0.2rem !important;
    }
    
    .stTextInput > div > div > input { 
        background-color: #1C2541 !important; 
        color: white !important; 
        border: 1px solid #3A506B !important; 
    }
    
    p, h1, h2, h3, h4 { color: #ffffff !important; }
    .stMarkdown p { color: #E0E1DD !important; }
    h3.stMarkdown { margin: 0.5rem 0 0.3rem 0 !important; }
    
    /* SLOWER BLINKING ANIMATION (2s instead of 1.5s) */
    .recording-indicator {
        display: inline-block;
        width: 14px;
        height: 14px;
        background-color: #ff4b4b;
        border-radius: 50%;
        margin-right: 10px;
        animation: slow-pulse 2s ease-in-out infinite;
        box-shadow: 0 0 10px rgba(255, 75, 75, 0.6);
    }
    
    @keyframes slow-pulse {
        0%, 100% {
            transform: scale(1);
            opacity: 1;
        }
        50% {
            transform: scale(1.8);
            opacity: 0.3;
        }
    }
    
    .recording-status {
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
        font-size: 1.2rem;
        animation: text-fade 2s ease-in-out infinite;
    }
    
    @keyframes text-fade {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
    }
    
    .pulse-text {
        animation: text-pulse 2s ease-in-out infinite;
    }
    
    @keyframes text-pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</p>', unsafe_allow_html=True)

pwd_col1, pwd_col2 = st.columns([1, 4])
with pwd_col1:
    password = st.text_input("", type="password", label_visibility="collapsed", key="pwd_top", placeholder="🔐 Access Password")

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

st.markdown("""
<div class="dev-note">
    📌 <strong>Dev Demo</strong> | Address Bar displays ClassiAIhk.com via Streamlit domain masking
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="about-container">
    <h2 class="about-heading">About Classi AI</h2>
    <div class="company-intro">
        <p>
            Classi AI is a deep-tech AI infrastructure company. Our core technology is a proprietary Universal Fluency Layer designed to enhance and complement voice-to-text and LLM systems across multiple verticals, including EdTech, B2B, and enterprise applications.
        </p>
        <p>
            Beyond enterprise infrastructure, Classi's consumer SaaS platform is equally powerful. Engineered to serve the over 1 billion non-native English learners globally, it delivers a comprehensive suite of advanced features—including interactive conversational practice, AI-powered tutoring, and precision pronunciation guidance across all four core language skills. By leveraging our Universal Fluency Layer in these highly demanding consumer scenarios, our ecosystem doesn't just compete with legacy EdTech tools—it renders dictionaries, translation apps, and conventional language learning platforms obsolete.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Voice Microphone Section
st.markdown("### 🎤 Voice Microphone")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔴 Start Recording", use_container_width=True, key="start_rec"):
        st.session_state.recording = True
        st.session_state.recording_start_time = time.time()
        st.rerun()

with col2:
    if st.button("⏹️ Stop Recording", use_container_width=True, key="stop_rec"):
        if st.session_state.recording and st.session_state.recording_start_time:
            duration = time.time() - st.session_state.recording_start_time
            duration_str = f"{duration:.1f}s"
            
            st.session_state.recording = False
            st.session_state.recording_start_time = None
            st.success(f"✅ Recording stopped - Duration: {duration_str}")
            st.rerun()

# Show SLOWER blinking indicator when recording
if st.session_state.recording:
    st.markdown("""
    <div class="recording-status">
        <span class="recording-indicator"></span>
        <span class="pulse-text">RECORDING IN PROGRESS... Click STOP when finished</span>
    </div>
    """, unsafe_allow_html=True)

# Audio input for actual recording
audio_value = st.audio_input("Record your voice", key="audio_recorder")

if audio_value:
    with st.spinner("🔄 Processing audio with AI..."):
        # Save audio temporarily
        temp_path = Path("temp_audio.wav")
        temp_path.write_bytes(audio_value.getvalue())
        
        # ACTUAL AI TRANSCRIPTION
        try:
            transcriber = load_asr_model()
            result = transcriber(str(temp_path))
            raw_text = result["text"]
            
            # Simple GDE simulation (replace with your actual MVP logic)
            corrected_text = raw_text
            # Add basic corrections
            corrections = {
                "other of": "author of",
                "flip stills": "Philip Steels", 
                "danger child": "Danger Trail",
                "mission impossble": "Mission Impossible"
            }
            for error, fix in corrections.items():
                corrected_text = corrected_text.lower().replace(error, fix)
            corrected_text = corrected_text.capitalize()
            
            # Add to history
            st.session_state.history.insert(0, {
                'timestamp': datetime.now().strftime("%H:%M:%S"),
                'raw_text': raw_text,
                'corrected_text': corrected_text,
                'duration': duration_str if 'duration_str' in locals() else "N/A"
            })
            st.session_state.history = st.session_state.history[:10]
            
            st.success("✅ Transcription complete!")
            
        except Exception as e:
            st.error(f"Processing error: {str(e)}")
            st.session_state.history.insert(0, {
                'timestamp': datetime.now().strftime("%H:%M:%S"),
                'raw_text': "Error processing audio",
                'corrected_text': str(e),
                'duration': "N/A"
            })
        
        # Clean up
        if temp_path.exists():
            temp_path.unlink()
        
        st.rerun()

# Display current results
col_a, col_b = st.columns(2)
with col_a:
    display_raw = "No recording yet" if not st.session_state.history else st.session_state.history[0]['raw_text']
    st.markdown(f"""
    <div class="status-box">
        <h4 style="color: #ff4b4b; margin: 0;">🔴 Raw ASR</h4>
        <p style="margin: 0; color: #aaa; font-size: 0.9rem;">{display_raw}</p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    display_corrected = "No recording yet" if not st.session_state.history else st.session_state.history[0]['corrected_text']
    st.markdown(f"""
    <div class="status-box">
        <h4 style="color: #00ff88; margin: 0;">🟢 Corrected</h4>
        <p style="margin: 0; color: #aaa; font-size: 0.9rem;">{display_corrected}</p>
    </div>
    """, unsafe_allow_html=True)

# History section
if st.session_state.history:
    st.markdown("### 📜 History of the Last 10 Text Transcripts")
    for i, item in enumerate(st.session_state.history[:10]):
        with st.expander(f"#{i+1} - {item['timestamp']} - {item.get('duration', 'N/A')}", expanded=(i==0)):
            col_x, col_y = st.columns(2)
            with col_x:
                st.markdown("**🔴 Raw ASR:**")
                st.write(item['raw_text'])
            with col_y:
                st.markdown("**🟢 Corrected:**")
                st.write(item['corrected_text'])

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #8B9DC3; font-size: 0.8rem; margin-top: 0.5rem;">
    <p>© 2026 Classi AI. All rights reserved. | Contact: <strong>William@ClassiAIhk.com</strong></p>
</div>
""", unsafe_allow_html=True)
