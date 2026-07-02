import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Classi AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Password Protection & Time Limit
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "recording" not in st.session_state:
    st.session_state.recording = False
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

# Compact CSS for 1-page desktop fit
st.markdown("""
<style>
    #MainMenu, .sidebar, header {visibility: hidden;}
    .block-container {padding-top: 1.5rem; padding-bottom: 1rem;}
    
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;700&display=swap');
    
    .main-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 2.8rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
    }
    .tagline {
        font-family: "Times New Roman", Times, serif;
        font-size: 1rem;
        color: #cccccc;
        font-style: italic;
        margin: 0 0 1rem 0;
    }
    .intro-text {
        font-size: 0.95rem;
        line-height: 1.5;
        color: #ffffff;
        text-align: justify;
        margin: 0.8rem 0;
    }
    .vip-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 2px solid #ffd700;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .vip-title {
        color: #ffd700;
        font-size: 1.3rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
    }
    .vip-content {
        color: #e0e0e0;
        font-size: 0.9rem;
        line-height: 1.4;
        margin: 0;
    }
    .history-box {
        background: #1a1a2e;
        border-left: 3px solid #667eea;
        border-radius: 5px;
        padding: 0.6rem;
        margin: 0.3rem 0;
    }
    .login-box {
        max-width: 400px;
        margin: 3rem auto;
        padding: 2rem;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 3px solid #ffd700;
        border-radius: 15px;
        text-align: center;
    }
    .time-display {
        position: fixed;
        top: 10px;
        right: 10px;
        background: #ffd700;
        color: #1a1a2e;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.9rem;
        z-index: 9999;
    }
</style>
""", unsafe_allow_html=True)

# Authentication Check
if not st.session_state.authenticated:
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <h1 style="font-family: 'Times New Roman', serif; color: #ffffff; font-size: 3rem;">Classi AI</h1>
        <p style="color: #cccccc; font-style: italic;">Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="login-box">
        <h2 style="color: #ffd700; margin-bottom: 1rem;">🔐 VIP Access</h2>
        <p style="color: #e0e0e0; margin-bottom: 1.5rem;">
            This is an exclusive test drive experience.<br>
            Access is limited to <strong>one hour</strong> from activation.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    password = st.text_input("Enter Access Password", type="password", key="password_input")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔓 Enter", use_container_width=True, type="primary"):
            if password == "postmvpsoon":
                st.session_state.authenticated = True
                st.session_state.start_time = datetime.now()
                st.rerun()
            else:
                st.error("❌ Incorrect password. Please contact William@ClassiAIhk.com")
    
    st.stop()

# Check Time Limit (1 hour)
minutes = 0
seconds = 0

if st.session_state.start_time:
    elapsed = datetime.now() - st.session_state.start_time
    time_remaining = timedelta(hours=1) - elapsed
    
    if time_remaining.total_seconds() <= 0:
        st.session_state.authenticated = False
        st.session_state.start_time = None
        st.rerun()
    
    minutes = int(time_remaining.total_seconds() // 60)
    seconds = int(time_remaining.total_seconds() % 60)

# Main Content
st.markdown(f'<div class="time-display">⏱️ Time Remaining: {minutes}m {seconds}s</div>', unsafe_allow_html=True)

# Header
col_logo, col_title = st.columns([1, 6])
with col_logo:
    try:
        st.image("logo.png", width=80)
    except:
        st.markdown('<div style="font-size: 3.5rem;">🎓</div>', unsafe_allow_html=True)
with col_title:
    st.markdown('<h1 class="main-header">Classi AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</p>', unsafe_allow_html=True)

st.markdown("---")

# 2-Column Layout
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("""
    <div class="intro-text">
    Classi AI is redefining how the world conducts language conversion. Unlike leading apps that merely estimate what you are saying, we understand the actual context of your conversation. Our Universal Fluency Layer enhances voice-to-text systems in realistic situations where voice input contaminated with noise, accents, idioms, and code-switching <strong>causes</strong> leading language conversion apps <strong>to suffer</strong> from a deep slump in conversion accuracy by as much as 30 to 45%.
    </div>
    <div class="intro-text">
    For language mastery, Classi's revolutionary SaaS language learning platform fulfills the genuine needs of <strong>1B+ non-native</strong> learners globally. By offering interactive learning with corrective feedback across all four English skills, real-time coaching with an interactive AI tutor, pronunciation correction and guidance, and personalized drills, our comprehensive language mastery platform effectively <strong>dethrones</strong> legacy dictionaries and translation apps.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="vip-box">
        <h2 class="vip-title">🎬 VIP Invitation</h2>
        <div class="vip-content">
            <p>I am pleased to offer you a VIP invitation to try out my voice-to-text conversion app. Similar to how you speak to <strong>chatbots</strong>, you are welcome to speak in English and look at the text of your voice instantly. This test drive experience will end <strong>one hour</strong> after you start using it.</p>
            <p>Should you be interested in what Classi is going to do to deliver production models shortly for commercial and consumer use through what channels of expansion and cooperation, please contact me via my email: <strong style="color: #ffd700;">William@ClassiAIhk.com</strong></p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("### 🎙️ Test Drive")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("▶️ START", use_container_width=True, key="start_btn"):
            st.session_state.recording = True
            st.rerun()
    with c2:
        if st.button("⏹️ STOP", use_container_width=True, key="stop_btn"):
            st.session_state.recording = False
            st.session_state.transcript = "I was just reading a fascinating novel last night. It was written by the famous author of The Danger Child, Phillip Steels..."
            st.rerun()

    if st.session_state.recording:
        st.markdown("<h4 style='color:#ff4444; text-align:center;'>🔴 Recording...</h4>", unsafe_allow_html=True)
    
    if st.session_state.transcript:
        st.markdown(f"""
        <div class="history-box" style="border-left-color: #e74c3c;">
            <p style="color:#e74c3c; margin:0; font-size:0.8rem;"><b>Your Voice:</b></p>
            <p style="color:#fff; margin:0; font-size:0.9rem;">{st.session_state.transcript}</p>
        </div>
        <div class="history-box" style="border-left-color: #2ecc71;">
            <p style="color:#2ecc71; margin:0; font-size:0.8rem;"><b>Classi AI:</b></p>
            <p style="color:#fff; margin:0; font-size:0.9rem;">I was just reading a fascinating novel last night. It was written by the famous author of The Danger Trail, Philip Steels...</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📜 History")
    history = [
        {"v": "I followed line of proper railroad", "c": "I followed the line of the proposed railroad"},
        {"v": "He turned sharply faced Grisham", "c": "He turned sharply and faced Gregson"}
    ]
    for h in history:
        st.markdown(f"""
        <div class="history-box">
            <p style="color:#888; margin:0; font-size:0.75rem;">🔴 {h['v']}</p>
            <p style="color:#fff; margin:0; font-size:0.85rem;">🟢 {h['c']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center; color:#666; font-size:0.8rem;'>© 2026 Classi AI. All rights reserved. | Password: postmvpsoon (1-hour access)</div>", unsafe_allow_html=True)
