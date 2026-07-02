import streamlit as st
import streamlit.components.v1 as components

# ============================================================================
# PASSWORD PROTECTION
# ============================================================================
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.set_page_config(page_title="Classi AI - Login", layout="centered")
    
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%); }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🔒 Classi AI - Confidential Demo")
    st.markdown("### Restricted Access")
    
    password = st.text_input("Enter access code:", type="password", key="password_input")
    
    if st.button("Login", key="login_btn"):
        if password == "classi2026invest":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Invalid access code")
    
    st.markdown("---")
    st.markdown("*For investor inquiries, contact: tommy@classiai.hk*")
    st.stop()

# ============================================================================
# MAIN APP - GUARDED VERSION
# ============================================================================
st.set_page_config(
    page_title="Classi AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Hide sidebar completely
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stSidebar {display: none !important;}
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1429 100%);
        color: #ffffff;
    }
    .header-container {
        display: flex;
        align-items: center;
        margin-bottom: 40px;
        padding-top: 20px;
    }
    .logo-circle {
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #00ffff 0%, #0099ff 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 15px;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.4);
    }
    .logo-text {
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    .company-name {
        font-size: 28px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 1px;
    }
    .mi-box {
        background: rgba(20, 20, 30, 0.8);
        border: 2px solid #00ffff;
        border-radius: 12px;
        padding: 25px;
        max-width: 700px;
        margin: 0 auto 40px auto;
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
    }
    .mi-text {
        color: #e0e0e0;
        font-size: 1.1rem;
        line-height: 1.6;
        font-style: italic;
    }
    .countdown {
        color: #ff4444;
        font-weight: bold;
        font-size: 1.2rem;
        margin-top: 15px;
    }
    .intro-section {
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
        padding: 0 20px;
    }
    .intro-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 20px;
        background: linear-gradient(90deg, #00ffff 0%, #0099ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .intro-text {
        font-size: 1.2rem;
        line-height: 1.8;
        color: #b0b0b0;
    }
</style>
""", unsafe_allow_html=True)

# 1. Header: Logo + Classi AI (Top Left)
st.markdown("""
<div class="header-container">
    <div class="logo-circle">
        <div class="logo-text">C</div>
    </div>
    <div class="company-name">Classi AI</div>
</div>
""", unsafe_allow_html=True)

# 2. Mission Impossible Box (Center, Smaller)
st.markdown("""
<div class="mi-box">
    <div class="mi-text">
        "If you choose to accept the VIP invitation to partake in Classi's state-of-the-art 
        voice-to-text Experiential Voyage, you are free to talk to me in English through the 
        Voice message icon. The text of your voice message will be shown instantly."
    </div>
    <div class="countdown">
        ⚠️ This website will disintegrate in <span id="countdown">10</span> seconds...
    </div>
</div>
""", unsafe_allow_html=True)

# Countdown Timer Script
components.html("""
<script>
let seconds = 10;
const countdown = document.getElementById('countdown');
const interval = setInterval(() => {
    seconds--;
    if (countdown) countdown.textContent = seconds;
    if (seconds <= 0) {
        clearInterval(interval);
        document.querySelector('.mi-box').innerHTML = 
            '<div style="color: #00ff00; font-size: 1.2rem; font-weight: bold;">✓ Access Granted. Welcome to the future of voice intelligence.</div>';
    }
}, 1000);
</script>
""", height=60)

# 3. Strong Introduction (No Tech Details)
st.markdown("""
<div class="intro-section">
    <div class="intro-title">Redefining Global Voice Interaction</div>
    <div class="intro-text">
        Classi AI is building the next generation of voice intelligence infrastructure. 
        We bridge the gap between human expression and digital understanding, ensuring that 
        every voice is captured with unprecedented clarity and precision. 
        <br><br>
        Designed for the future of communication, our platform transforms how the world 
        interacts with technology—making voice the ultimate interface for everyone, everywhere.
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #555555; margin-top: 50px; font-size: 0.8rem;'>
    <p>© 2026 Classi AI. All rights reserved. | Confidential & Proprietary</p>
</div>
""", unsafe_allow_html=True)
