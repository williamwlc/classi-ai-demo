import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Classi AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Mobile Responsive
st.markdown("""
<style>
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
    .voice-container {
        text-align: center;
        margin: 3rem 0;
    }
    .voice-icon {
        width: 150px;
        height: 150px;
        background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem auto;
        box-shadow: 0 8px 20px rgba(155, 89, 182, 0.4);
        cursor: pointer;
        transition: transform 0.3s;
    }
    .voice-icon:hover {
        transform: scale(1.05);
    }
    .voice-icon.recording {
        animation: pulse 1.5s infinite;
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        box-shadow: 0 8px 20px rgba(231, 76, 60, 0.5);
    }
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(231, 76, 60, 0.7); }
        50% { transform: scale(1.1); box-shadow: 0 0 0 20px rgba(231, 76, 60, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(231, 76, 60, 0); }
    }
    .mic-icon {
        font-size: 4rem;
    }
    .output-box {
        background: #1a1a2e;
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        border-left: 5px solid #667eea;
    }
    .output-box.raw {
        border-left-color: #e74c3c;
    }
    .output-box.corrected {
        border-left-color: #2ecc71;
    }
    .output-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .output-content {
        font-size: 1.1rem;
        color: #aaa;
        min-height: 60px;
    }
    .status-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 0.5rem;
    }
    .status-dot.red {
        background: #e74c3c;
    }
    .status-dot.green {
        background: #2ecc71;
    }
    .password-line {
        text-align: center;
        color: #888;
        font-size: 0.9rem;
        margin-top: 2rem;
        font-family: "Times New Roman", serif;
    }
    @media (max-width: 768px) {
        .main-header { font-size: 2.5rem; }
        .voice-icon { width: 120px; height: 120px; }
        .mic-icon { font-size: 3rem; }
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

# --- ONE PARAGRAPH INTRO (WITH NEW LINE) ---
st.markdown("""
<div class="intro-text">
Classi AI is redefining how the world understands spoken language, specifically designed to bridge the fluency gap for non-native English speakers. <strong>Unlike other apps that estimate you're speaking, we understand you're speaking.</strong> Our platform comprehends the actual context of your conversation. For instance, if you discuss the 'sequel to Mission Impossible' and mention a 'supporting actor,' our system instantly recognizes the entertainment domain, correctly identifying characters like 'Benji Dunn' rather than misinterpreting them as random phrases. By mapping keywords to real-world entities, we ensure your voice is not just heard, but truly understood, preserving your unique identity and intent in any environment.
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
        
        <em>Your mission, should you choose to accept it, is to become a founding member of Classi AI's Founder's Circle. 
        Your participation will help revolutionize how millions of people worldwide express themselves in English.</em><br><br>
        
        <strong>Recording Instructions:</strong><br>
        Click the microphone icon below to record your response.<br>
        Click once to START recording.<br>
        Click again to STOP and transcribe.
    </p>
</div>
""", unsafe_allow_html=True)

# --- VOICE RECORDING INTERFACE (LIKE YOUR IMAGE) ---
st.markdown('<div class="voice-container">', unsafe_allow_html=True)

# Initialize session state
if "recording" not in st.session_state:
    st.session_state.recording = False
if "transcript" not in st.session_state:
    st.session_state.transcript = ""
if "corrected" not in st.session_state:
    st.session_state.corrected = ""

# Voice Icon
if st.session_state.recording:
    st.markdown('<div class="voice-icon recording"><div class="mic-icon">🎤</div></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="voice-icon"><div class="mic-icon">🎤</div></div>', unsafe_allow_html=True)

st.markdown('<p style="color: #9b59b6; font-size: 1.2rem; margin-bottom: 2rem;">Voice Message Icon</p>', unsafe_allow_html=True)

# Recording Button
if st.session_state.recording:
    if st.button("⏹️ Stop Recording", type="primary", use_container_width=True):
        st.session_state.recording = False
        # Simulated output (replace with actual ASR/GDE in production)
        st.session_state.transcript = "Sequel of Mission Impossible is coming soon. Who will be the supporting male actor this time as Benji Dunn was unavailable."
        st.session_state.corrected = "Sequel of Mission Impossible is coming soon. Who will be the supporting male actor this time as Benji Dunn was unavailable."
        st.rerun()
else:
    if st.button("🔴 Start Recording", type="primary", use_container_width=True):
        st.session_state.recording = True
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- OUTPUT BOXES (LIKE YOUR IMAGE) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="output-box raw">
        <div class="output-title">
            <span class="status-dot red"></span>
            <span style="color: #3498db;">Raw ASR (Stage 3)</span>
        </div>
        <div class="output-content">
            {st.session_state.transcript if st.session_state.transcript else "Waiting for voice input..."}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="output-box corrected">
        <div class="output-title">
            <span class="status-dot green"></span>
            <span style="color: #2ecc71;">Corrected Output (Stage 5)</span>
        </div>
        <div class="output-content">
            {st.session_state.corrected if st.session_state.corrected else "Waiting for voice input..."}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PASSWORD LINE ---
st.markdown('<div class="password-line">Secure Access: postmvpsoon</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-family: "Times New Roman", serif; margin: 2rem 0;'>
    <p>© 2026 Classi AI. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
