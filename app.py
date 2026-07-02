import streamlit as st
import base64
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Classi AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Hide sidebar, mobile responsive
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    .sidebar {display: none;}
    
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;700&display=swap');
    
    .main-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #667eea;
        text-align: left;
        margin: 0;
    }
    
    .tagline {
        font-family: "Times New Roman", Times, serif;
        font-size: 1.1rem;
        color: #666;
        text-align: left;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    .intro-text {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #333;
        text-align: justify;
        margin: 2rem 0;
    }
    
    .vip-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 3px solid #ffd700;
        border-radius: 15px;
        padding: 3rem 2rem;
        margin: 3rem 0;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .vip-title {
        color: #ffd700;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    
    .vip-message {
        color: #fff;
        font-size: 1.3rem;
        line-height: 1.8;
        margin: 1.5rem 0;
    }
    
    .voice-icon {
        font-size: 5rem;
        margin: 2rem 0;
        cursor: pointer;
        transition: transform 0.3s;
    }
    
    .voice-icon:hover {
        transform: scale(1.1);
    }
    
    .recording-active {
        animation: pulse 1.5s infinite;
        color: #ff4444;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    .transcript-box {
        background: #f8f9fa;
        border-left: 5px solid #667eea;
        padding: 1.5rem;
        margin: 2rem 0;
        border-radius: 8px;
        font-size: 1.1rem;
    }
    
    @media (max-width: 768px) {
        .main-header { font-size: 2.5rem; }
        .vip-title { font-size: 1.8rem; }
        .vip-message { font-size: 1.1rem; }
        .voice-icon { font-size: 4rem; }
    }
</style>
""", unsafe_allow_html=True)

# Logo and Header - TOP LEFT
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.markdown('<div style="font-size: 5rem; margin: 0.5rem;">🎓🧠</div>', unsafe_allow_html=True)
with col_title:
    st.markdown('<h1 class="main-header">Classi AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Universal Fluency Layer for Voice & Language Systems</p>', unsafe_allow_html=True)

st.markdown("---")

# ONE PARAGRAPH INTRO - NO SENSITIVE INFO
st.markdown("""
<div class="intro-text">
Classi AI is redefining how the world understands spoken language, specifically designed to bridge the fluency gap for non-native English speakers. Unlike traditional tools that merely transcribe words, our platform comprehends the actual context of your conversation. For instance, if you discuss the 'sequel to Mission Impossible' and mention a 'supporting actor,' our system instantly recognizes the entertainment domain, correctly identifying characters like 'Benji Dunn' rather than misinterpreting them as random phrases. By mapping keywords to real-world entities, we ensure your voice is not just heard, but truly understood, preserving your unique identity and intent in any environment.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# MISSION IMPOSSIBLE VIP INVITATION BOX
st.markdown("""
<div class="vip-box">
    <h2 class="vip-title">🎬 VIP Invitation</h2>
    <p class="vip-message">
        <strong>Good evening, distinguished guest.</strong><br><br>
        
        You have been specially selected to join an exclusive circle of innovators shaping the future of human-machine communication. 
        This message will self-destruct in your mind once you've made your decision.<br><br>
        
        <em>Your mission, should you choose to accept it, is to become a founding member of Classi AI's Founder's Circle. 
        Your participation will help revolutionize how millions of people worldwide express themselves in English.</em><br><br>
        
        <strong>Recording Instructions:</strong><br>
        Click the microphone icon below to record your response.<br>
        Click once to START recording.<br>
        Click again to STOP and transcribe.
    </p>
</div>
""", unsafe_allow_html=True)

# Voice Recording Section
st.markdown('<div style="text-align: center; margin: 3rem 0;">', unsafe_allow_html=True)
st.markdown('<h2 style="color: #667eea; margin-bottom: 2rem;">🎙️ Record Your Response</h2>', unsafe_allow_html=True)

# Initialize session state
if "recording" not in st.session_state:
    st.session_state.recording = False
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

# Voice recording icon
if st.session_state.recording:
    voice_html = '<div class="voice-icon recording-active">🎤</div>'
else:
    voice_html = '<div class="voice-icon">🎤</div>'

st.markdown(voice_html, unsafe_allow_html=True)

# Recording button
if st.session_state.recording:
    if st.button("⏹️ Stop Recording", type="primary", use_container_width=True):
        st.session_state.recording = False
        # Simulated transcript (in real implementation, this would process audio)
        st.session_state.transcript = "This is your recorded message. In production, this will display the actual transcription of your voice."
        st.rerun()
else:
    if st.button(" Start Recording", type="primary", use_container_width=True):
        st.session_state.recording = True
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Display transcript
if st.session_state.transcript:
    st.markdown("""
    <div class="transcript-box">
        <h3 style="color: #667eea; margin-top: 0;">📝 Your Message:</h3>
        <p style="font-size: 1.1rem; line-height: 1.6;">""" + st.session_state.transcript + """</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-family: "Times New Roman", serif; margin: 2rem 0;'>
    <p>© 2026 Classi AI. All rights reserved.</p>
    <p style="font-size: 0.9rem;">Secure Access: postmvpsoon</p>
</div>
""", unsafe_allow_html=True)
