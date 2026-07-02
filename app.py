import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Classi AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Compact Desktop Layout
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;700&display=swap');
    
    /* Hide sidebar */
    #MainMenu {visibility: hidden;}
    .sidebar {display: none;}
    
    /* Compact spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 1rem;
    }
    
    /* Header */
    .main-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
    }
    
    .tagline {
        font-family: "Times New Roman", Times, serif;
        font-size: 1.1rem;
        color: #cccccc;
        font-style: italic;
        margin: 0.5rem 0 1.5rem 0;
    }
    
    /* Intro Text - White, Compact */
    .intro-text {
        font-size: 1.05rem;
        line-height: 1.6;
        color: #ffffff;
        text-align: justify;
        margin: 1rem 0;
    }
    
    /* VIP Box - Compact */
    .vip-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 3px solid #ffd700;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        text-align: center;
    }
    
    .vip-title {
        color: #ffd700;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
    }
    
    .vip-content {
        color: #e0e0e0;
        font-size: 0.95rem;
        line-height: 1.5;
        margin: 0.5rem 0;
    }
    
    .vip-email {
        color: #ffd700;
        font-weight: bold;
        margin-top: 0.5rem;
    }
    
    /* Voice Section */
    .voice-section {
        text-align: center;
        margin: 1rem 0;
    }
    
    .voice-icon {
        font-size: 4rem;
        margin: 0.5rem 0;
    }
    
    /* History Section */
    .history-box {
        background: #1a1a2e;
        border-left: 4px solid #667eea;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .history-label {
        color: #667eea;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 0.3rem;
    }
    
    .history-text {
        color: #ffffff;
        font-size: 0.95rem;
        margin: 0;
    }
    
    /* Columns spacing */
    .stColumn {
        padding: 0 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header - Logo and Title
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.markdown('<div style="font-size: 4rem; margin: 0;">🧠</div>', unsafe_allow_html=True)
with col_title:
    st.markdown('<h1 class="main-header">Classi AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Universal Fluency Layer for Voice & Language Systems</p>', unsafe_allow_html=True)

st.markdown("---")

# PROOFREAD CONTENT - COMPACT LAYOUT
col1, col2 = st.columns([2, 1])

with col1:
    # INTRODUCTION (Proofread & Refined)
    st.markdown("""
    <div class="intro-text">
    <strong>Classi AI: Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</strong><br><br>
    
    Classi AI is redefining how the world conducts language conversion. Unlike leading apps that merely estimate what you are saying, we understand the actual context of your conversation. Our Universal Fluency Layer enhances voice-to-text systems in realistic situations where voice input contaminated with noise, accents, idioms, and code-switching render leading language conversion apps suffer from a deep slump in conversion accuracy by as much as 30 to 45%.<br><br>
    
    For language mastery, Classi's revolutionary SaaS language learning platform fulfills the genuine needs of 1B+ non-native learners globally. By offering interactive learning with corrective feedback across all four English skills, real-time coaching with an interactive AI tutor, pronunciation correction and guidance, and personalized drills, our comprehensive language mastery platform effectively dethrones legacy dictionaries and translation apps.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # VIP INVITATION (Proofread & Concise)
    st.markdown("""
    <div class="vip-box">
        <h2 class="vip-title">🎬 VIP Invitation</h2>
        <div class="vip-content">
            <p style="margin: 0.5rem 0;">
                I am pleased to offer you a VIP invitation to try our voice-to-text conversion app. 
                Similar to how you speak to chatbots, you are welcome to speak in English and see 
                the text of your voice instantly.
            </p>
            <p style="margin: 0.5rem 0; color: #ffd700;">
                <em>This test drive experience will end one hour after you start using it.</em>
            </p>
            <p style="margin: 0.5rem 0;">
                Should you be interested in what Classi AI is going to do to deliver production models 
                shortly for commercial and consumer use through what channels of expansion and cooperation, 
                please contact me via email:
            </p>
            <p class="vip-email">William@ClassiAIhk.com</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # VOICE RECORDING SECTION (Compact)
    st.markdown('<div class="voice-section">', unsafe_allow_html=True)
    st.markdown('<div class="voice-icon">🎤</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #667eea; margin: 0.5rem 0;'>Click to Record</h3>", unsafe_allow_html=True)
    
    # Initialize session state
    if "recording" not in st.session_state:
        st.session_state.recording = False
    if "transcript" not in st.session_state:
        st.session_state.transcript = ""
    
    col_start, col_stop = st.columns(2)
    with col_start:
        if st.button("▶️ START", use_container_width=True, key="start_btn"):
            st.session_state.recording = True
            st.rerun()
    
    with col_stop:
        if st.button("⏹️ STOP", use_container_width=True, key="stop_btn"):
            st.session_state.recording = False
            st.session_state.transcript = "This is your transcribed voice message. In production, your actual words will appear here."
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display transcript if exists
    if st.session_state.transcript:
        st.markdown(f"""
        <div style="background: #f8f9fa; padding: 0.8rem; border-radius: 5px; margin-top: 1rem;">
            <p style="color: #333; margin: 0; font-size: 0.9rem;"><strong>Your Message:</strong><br>
            {st.session_state.transcript}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# HISTORY SECTION (New - Compact)
st.subheader("📜 Recording History")

# Initialize history in session state
if "history" not in st.session_state:
    st.session_state.history = [
        {"time": "19:45", "voice": "Sequel of Mission Impossible coming soon", "corrected": "Sequel to Mission Impossible is coming soon"},
        {"time": "19:42", "voice": "Who supporting male actor this time", "corrected": "Who will be the supporting male actor this time"},
        {"time": "19:38", "voice": "Benji Dunn was dead", "corrected": "Benji Dunn was unavailable"}
    ]

# Display history (last 5 entries)
for entry in st.session_state.history[-5:]:
    col_time, col_voice, col_corrected = st.columns([1, 2, 2])
    with col_time:
        st.markdown(f"<div style='color: #888; font-size: 0.85rem;'>{entry['time']}</div>", unsafe_allow_html=True)
    with col_voice:
        st.markdown(f"""
        <div class="history-box" style="border-left-color: #e74c3c;">
            <div class="history-label">🔴 Your Voice</div>
            <p class="history-text">{entry['voice']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col_corrected:
        st.markdown(f"""
        <div class="history-box" style="border-left-color: #2ecc71;">
            <div class="history-label">🟢 Classi AI Correction</div>
            <p class="history-text">{entry['corrected']}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-family: "Times New Roman", serif; margin: 1rem 0; font-size: 0.9rem;'>
    <p>© 2026 Classi AI. All rights reserved. | Secure Access: postmvpsoon</p>
</div>
""", unsafe_allow_html=True)
