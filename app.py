import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Classi AI",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Fixed text colors and layout
st.markdown("""
<style>
    /* Hide sidebar */
    #MainMenu {visibility: hidden;}
    .sidebar {display: none;}
    
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;700&display=swap');
    
    /* Header Styles */
    .main-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #ffffff; /* Changed to White */
        text-align: left;
        margin: 0;
    }
    
    .tagline {
        font-family: "Times New Roman", Times, serif;
        font-size: 1.2rem;
        color: #cccccc; /* Lighter grey for visibility */
        text-align: left;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* Intro Text - NOW WHITE */
    .intro-text {
        font-size: 1.2rem;
        line-height: 1.8;
        color: #ffffff; /* FIXED: White text */
        text-align: left;
        margin: 2rem 0;
    }
    
    /* VIP Box Styles */
    .vip-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 4px solid #ffd700;
        border-radius: 15px;
        padding: 3rem 2rem;
        margin: 3rem 0;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .vip-title {
        color: #ffd700;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .vip-greeting {
        color: #ffffff;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    
    .vip-content {
        color: #e0e0e0;
        font-size: 1.2rem;
        line-height: 1.6;
        margin: 1.5rem 0;
        text-align: left;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .vip-disclaimer {
        color: #888888;
        font-size: 0.9rem;
        font-style: italic;
        margin-top: 2rem;
        border-top: 1px solid #444;
        padding-top: 1rem;
    }

    /* Voice Icon */
    .voice-container {
        text-align: center;
        margin: 4rem 0;
    }
    
    .voice-icon {
        font-size: 6rem;
        cursor: pointer;
        transition: transform 0.2s;
    }
    
    .voice-icon:hover {
        transform: scale(1.1);
    }
    
    .recording-active {
        animation: pulse 1s infinite;
        color: #ff4444;
    }
    
    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.6; transform: scale(1.05); }
        100% { opacity: 1; transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# Header - Logo and Title
col_logo, col_title = st.columns([1, 4])
with col_logo:
    # Try to load logo.png, fallback to emoji if missing
    try:
        st.image("logo.png", width=120)
    except:
        st.markdown('<div style="font-size: 5rem;">🧠</div>', unsafe_allow_html=True)
        
with col_title:
    st.markdown('<h1 class="main-header">Classi AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Universal Fluency Layer for Voice & Language Systems</p>', unsafe_allow_html=True)

st.markdown("---")

# ONE PARAGRAPH INTRO (WHITE TEXT)
st.markdown("""
<div class="intro-text">
Classi AI is redefining how the world understands spoken language, specifically designed to bridge the fluency gap for non-native English speakers. Unlike other apps that merely estimate what you are saying, we understand the actual context of your conversation. For instance, if you discuss the 'sequel to a famous spy thriller' and mention a 'supporting actor,' our system instantly recognizes the entertainment domain, correctly identifying characters like 'Benji Dunn' rather than misinterpreting them as random phrases. By mapping keywords to real-world entities, we ensure your voice is not just heard, but truly understood.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# VIP INVITATION BOX (FIXED HTML & TRADEMARK SAFE)
st.markdown("""
<div class="vip-box">
    <h2 class="vip-title">🎬 VIP Invitation</h2>
    <p class="vip-greeting">Good evening, distinguished guest.</p>
    
    <div class="vip-content">
        <p>You have been specially selected to join an exclusive circle of innovators shaping the future of human-machine communication.</p>
        
        <p><em>This message will self-destruct in your mind once you've made your decision.</em></p>
        
        <p><strong>Your mission, should you choose to accept it:</strong> Become a founding member of Classi AI's Founder's Circle. Your participation will help revolutionize how millions of people worldwide express themselves in English.</p>
        
        <p><strong>Recording Instructions:</strong><br>
        1. Click the microphone icon below to START recording.<br>
        2. Speak your response.<br>
        3. Click again to STOP and transcribe.</p>
    </div>
    
    <div class="vip-disclaimer">
        Disclaimer: This invitation is a creative parody inspired by classic spy thrillers. Classi AI is an independent project and is not affiliated with, endorsed by, or connected to any major motion picture studios or franchises. No trademark infringement intended.
    </div>
</div>
""", unsafe_allow_html=True)

# VOICE RECORDING SECTION
st.markdown('<div class="voice-container">', unsafe_allow_html=True)

# Initialize session state
if "recording" not in st.session_state:
    st.session_state.recording = False
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

# Display Icon
if st.session_state.recording:
    st.markdown('<div class="voice-icon recording-active">🎤</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #ff4444;'>🔴 RECORDING...</h3>", unsafe_allow_html=True)
else:
    st.markdown('<div class="voice-icon">🎤</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #667eea;'>Click to Record</h3>", unsafe_allow_html=True)

# Buttons
col_start, col_stop = st.columns(2)
with col_start:
    if st.button("▶️ START Recording", use_container_width=True):
        st.session_state.recording = True
        st.rerun()

with col_stop:
    if st.button("️ STOP Recording", use_container_width=True):
        st.session_state.recording = False
        st.session_state.transcript = "This is a placeholder for your transcribed voice message. In the final version, your actual words will appear here."
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Display Transcript
if st.session_state.transcript:
    st.markdown("""
    <div style="background: #f8f9fa; border-left: 5px solid #667eea; padding: 1.5rem; margin: 2rem 0; border-radius: 8px;">
        <h3 style="color: #333; margin-top: 0;">📝 Your Message:</h3>
        <p style="font-size: 1.1rem; color: #333;">""" + st.session_state.transcript + """</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-family: "Times New Roman", serif; margin: 2rem 0;'>
    <p>© 2026 Classi AI. All rights reserved.</p>
    <p style="font-size: 0.8rem;">Secure Access: postmvpsoon</p>
</div>
""", unsafe_allow_html=True)
