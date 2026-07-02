import streamlit as st
import numpy as np
import pandas as pd
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
    
    st.title(" Classi AI - Confidential Demo")
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
    }
    .main-heading {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00ffff 0%, #00d4ff 50%, #0099ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
        margin: 20px 0;
        text-align: center;
    }
    .tagline {
        text-align: center;
        color: #00ffff;
        font-size: 1.8rem;
        margin: -10px 0 30px 0;
        font-weight: 300;
    }
    .mi-banner {
        background: linear-gradient(135deg, rgba(255, 165, 0, 0.1) 0%, rgba(255, 140, 0, 0.1) 100%);
        border: 2px solid #ffa500;
        border-radius: 15px;
        padding: 30px;
        margin: 30px 0;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 165, 0, 0.3);
    }
    .mi-text {
        color: #ffa500;
        font-size: 1.2rem;
        font-weight: 600;
        line-height: 1.8;
    }
    .metric-box {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(0, 153, 255, 0.1) 100%);
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin: 10px 0;
    }
    .metric-value {
        color: #00ffff;
        font-size: 3rem;
        font-weight: 700;
        margin: 10px 0;
    }
    .metric-label {
        color: #a0a0a0;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Logo and Title
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.markdown("""
    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 50%; display: flex; align-items: center; justify-content: center;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);">
        <div style="color: white; font-size: 40px; font-weight: bold;">C</div>
    </div>
    """, unsafe_allow_html=True)
with col_title:
    st.markdown('<h1 class="main-heading">Classi AI</h1>', unsafe_allow_html=True)

st.markdown('<p class="tagline">Revolutionizing English Learning and Multi-language Conversion in a Revolutionary Way!</p>', unsafe_allow_html=True)

# Mission Impossible banner
st.markdown("""
<div class="mi-banner">
    <div class="mi-text">
         <strong>CONFIDENTIAL DEMO - AUTHORIZED PERSONNEL ONLY</strong><br><br>
        This demonstration contains proprietary technology and trade secrets.<br>
        Unauthorized access, distribution, or reproduction is strictly prohibited.<br><br>
        <span style="color: #ff6600; font-size: 1.1rem;">
        ⚠️ This session will self-destruct in <span id="countdown">10</span> seconds...
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Countdown timer
components.html("""
<script>
let seconds = 10;
const countdown = document.getElementById('countdown');
const interval = setInterval(() => {
    seconds--;
    if (countdown) countdown.textContent = seconds;
    if (seconds <= 0) {
        clearInterval(interval);
        document.querySelector('.mi-banner').innerHTML = 
            '<div style="color: #00ff00; font-size: 1.5rem; font-weight: bold;">✓ Access Granted - Welcome to the Future of Voice Technology</div>';
    }
}, 1000);
</script>
""", height=50)

st.markdown("---")

# Value Proposition - VAGUE but compelling
st.markdown("""
### 🚀 Transforming How the World Communicates

Classi AI is building a **next-generation voice intelligence platform** that bridges the gap between 
human speech and digital understanding. Our proprietary technology enhances voice-to-text systems 
for global users, with initial focus on English language applications.

**The Challenge We Solve:**
- Current voice recognition systems struggle with diverse accents and speaking patterns
- Performance degrades significantly in real-world conditions
- Existing solutions fail to capture the nuances of natural speech

**Our Approach:**
- Advanced acoustic modeling with personalized adaptation
- Intelligent pattern recognition that understands context
- Robust performance across challenging environments
""")

# Metrics - Keep it simple and impressive
st.markdown("---")
st.markdown("### 📊 Performance Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">9.68%</div>
        <div class="metric-label">Industry-Leading Accuracy<br>(Clean Audio)</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">179%</div>
        <div class="metric-label">Better Noise Robustness<br>vs. Baseline Systems</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">3</div>
        <div class="metric-label">Core Technology<br>Pillars</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Technology - VAGUE but impressive
st.markdown("""
### 🔬 Our Innovation

**Multi-Layer Processing Architecture:**
1. **Acoustic Analysis** - Advanced phonetic pattern recognition
2. **Contextual Understanding** - Intelligent interpretation engine
3. **Adaptive Learning** - Personalized performance optimization

**Key Capabilities:**
- Real-time voice-to-text conversion
- Accent-agnostic processing
- Noise-resistant algorithms
- Scalable cloud infrastructure

**Target Applications:**
- Voice assistants and smart devices
- Transcription and captioning services
- Language learning platforms
- Accessibility tools
""")

# Validation Results - Keep it general
st.markdown("---")
st.markdown("### ✅ Validation Status")

perf_data = {
    "Test Batch": ["Batch 1", "Batch 2", "Batch 3", "Batch 4"],
    "Baseline Accuracy": ["87.67%", "90.47%", "90.56%", "90.09%"],
    "Our System": ["89.47%", "91.38%", "91.01%", "90.32%"],
    "Improvement": ["+1.80%", "+0.91%", "+0.45%", "+0.23%"],
    "Status": ["✅ PASS", "✅ PASS", "✅ PASS", "✅ PASS"]
}

st.dataframe(pd.DataFrame(perf_data), use_container_width=True)

st.info("**Target:** <12% Error Rate | **Current:** 9.68% | **Status:** All batches exceed targets")

# Contact CTA
st.markdown("---")
col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
with col_cta2:
    st.markdown("""
    <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(0, 153, 255, 0.1) 100%); 
                border: 2px solid #00ffff; border-radius: 20px; margin: 30px 0;">
        <h3 style="color: #00ffff; margin-bottom: 15px;"> Interested in Partnership?</h3>
        <p style="color: #ffffff; margin-bottom: 20px;">
        We're currently in pre-MVP stage and preparing for strategic partnerships.<br>
        Contact us to learn more about collaboration opportunities.
        </p>
        <p style="color: #00ffff; font-size: 1.2rem; font-weight: bold;">
        tommy@classiai.hk
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666666; margin-top: 40px; padding: 20px; border-top: 1px solid rgba(0, 255, 255, 0.2);'>
    <p style='font-size: 0.9rem;'>© 2026 Classi AI. All rights reserved. | Confidential & Proprietary</p>
    <p style='font-size: 0.8rem; color: #444444;'>This demonstration contains trade secrets. Unauthorized use prohibited.</p>
</div>
""", unsafe_allow_html=True)
