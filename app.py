import streamlit as st
import base64

# Page Configuration
st.set_page_config(
    page_title="Classi AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Mobile Responsive & Clean
st.markdown("""
<style>
    /* Hide default Streamlit menu and sidebar */
    #MainMenu {visibility: hidden;}
    .stSidebar {display: none;}
    
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
    .voice-icon-container {
        text-align: center;
        margin: 3rem 0;
    }
    .voice-icon {
        font-size: 6rem;
        cursor: pointer;
        transition: transform 0.3s;
        display: inline-block;
    }
    .voice-icon:hover {
        transform: scale(1.1);
    }
    .recording-active {
        animation: pulse 1.5s infinite;
        color: #ff4444;
    }
    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.6; transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
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
        .voice-icon { font-size: 5rem; }
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER: LOGO + COMPANY NAME (TOP LEFT) ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    try:
        st.image("logo.png", width=120)
    except:
        st.markdown('<div style="font-size: 5rem;">🎓</div>', unsafe_allow_html=True)
with col_title:
    st.markdown('<h1 class="main-header">Classi AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Universal Fluency Layer for Voice & Language Systems</p>', unsafe_allow_html=True)

st.markdown("---")

# --- ONE PARAGRAPH INTRO (NO SENSITIVE INFO) ---
st.markdown("""
<div class="intro-text">
Classi AI is redefining how the world understands spoken language, specifically designed to bridge the fluency gap for non-native English speakers. Unlike traditional tools that merely transcribe words, our platform comprehends the actual context of your conversation.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- MISSION IMPOSSIBLE VIP INVITATION BOX ---
st.markdown("""
<div class="vip-box">
    <h2 class="vip-title">🎬 VIP Invitation</h2>
    <p class="vip-message">
        <strong>Good evening, distinguished guest.</strong><br><br>
        
        You have been specially selected to join an exclusive circle of innovators shaping the future of human-machine communication. 
        This message will self-destruct in your mind once you've made your decision.<br><br>
        
        <em>Should you choose to accept it, is to become a founding member of Classi AI's Founder's Circle. 
        Your participation will help revolutionize how millions of people worldwide express themselves in English.</em><br><br>
        
        <strong>Recording Instructions:</strong><br>
        Click the microphone icon below to record your response.<br>
        Click once to START recording.<br>
        Click again to STOP and transcribe.
    </p>
</div>
""", unsafe_allow_html=True)

# --- VOICE RECORDING SECTION ---
st.markdown('<div class="voice-icon-container">', unsafe_allow_html=True)
st.markdown('<h2 style="color: #667eea; margin-bottom: 2rem;">️ Record Your Response</h2>', unsafe_allow_html=True)

# Initialize session state for recording
if "recording" not in st.session_state:
    st.session_state.recording = False
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

# Display Voice Icon
if st.session_state.recording:
    voice_html = '<div class="voice-icon recording-active">🎤</div>'
else:
    voice_html = '<div class="voice-icon">🎤</div>'

st.markdown(voice_html, unsafe_allow_html=True)

# Recording Toggle Button
if st.session_state.recording:
    if st.button("️ Stop Recording", type="primary", use_container_width=True):
        st.session_state.recording = False
        # In production, this triggers the actual ASR/GDE pipeline
        st.session_state.transcript = "This is your recorded message. In production, this will display the actual transcription of your voice."
        st.rerun()
else:
    if st.button("🔴 Start Recording", type="primary", use_container_width=True):
        st.session_state.recording = True
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Display Transcript
if st.session_state.transcript:
    st.markdown(f"""
    <div class="transcript-box">
        <h3 style="color: #667eea; margin-top: 0;"> Your Message:</h3>
        <p style="font-size: 1.1rem; line-height: 1.6;">{st.session_state.transcript}</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-family: "Times New Roman", serif; margin: 2rem 0;'>
    <p>© 2026 Classi AI. All rights reserved.</p>
    <p style="font-size: 0.9rem;">Secure Access: postmvpsoon</p>
</div>
""", unsafe_allow_html=True)
