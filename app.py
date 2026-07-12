import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Classi AI - Universal Fluency Layer",
    page_icon="",
    layout="centered"
)

# Custom CSS for larger fonts and professional spacing
st.markdown("""
<style>
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
        text-align: center;
    }
    .subtitle {
        font-size: 1.4rem !important;
        color: #666666 !important;
        margin-top: 0 !important;
        margin-bottom: 2rem !important;
        text-align: center;
    }
    .section-header {
        font-size: 2rem !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        color: #1f1f1f !important;
    }
    .info-box {
        font-size: 1.15rem !important;
        line-height: 1.8 !important;
        padding: 2rem !important;
        margin-bottom: 2rem !important;
        background-color: #f8f9fa !important;
        border-radius: 10px !important;
        border-left: 5px solid #FF4B4B !important;
    }
    .tech-stack {
        font-size: 1.1rem !important;
        line-height: 2 !important;
        padding: 1.5rem !important;
        background-color: #ffffff !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 8px !important;
        margin-bottom: 1.5rem !important;
    }
    .recording-section {
        text-align: center;
        padding: 2rem;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin: 2rem 0;
    }
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.15rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Main page layout
st.markdown('<h1 class="main-title">Classi AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</p>', unsafe_allow_html=True)

st.markdown("---")

# About Classi AI Section
st.markdown('<h2 class="section-header">About Classi AI</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
<p><strong>Classi AI</strong> is a deep-tech AI infrastructure company. Our core technology is a proprietary <strong>Universal Fluency Layer (UFL)</strong> designed to enhance and complement voice-to-text and LLM systems across multiple verticals, including EdTech, B2B, and enterprise applications.</p>

<p>Beyond enterprise infrastructure, Classi's consumer SaaS platform is equally powerful. Engineered to serve the over <strong>1 billion non-native English learners globally</strong>, it delivers a comprehensive suite of advanced features—including interactive conversational practice, AI-powered tutoring, and precision pronunciation guidance across all four core language skills. By leveraging our Universal Fluency Layer in these highly demanding consumer scenarios, our ecosystem doesn't just compete with legacy EdTech tools—it renders dictionaries, translation apps, and conventional language learning platforms obsolete.</p>
</div>
""", unsafe_allow_html=True)

# Voice Recording Section
st.markdown('<h2 class="section-header">Voice Recording</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="recording-section">
    <p style="font-size: 1.2rem; margin-bottom: 1.5rem;">Test our Universal Fluency Layer with your voice</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("🎤 Start Recording", use_container_width=True, type="primary"):
        st.warning("⚠️ Voice recording features are temporarily disabled during final MVP debugging. Please check back soon.")

with col2:
    if st.button("⏹️ Stop Recording", use_container_width=True):
        st.info("ℹ️ Recording stopped. (Demo mode)")

# Technology Stack Section
st.markdown('<h2 class="section-header">Technology Stack</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="tech-stack">
<strong>AFE v2 (Acoustic Front End):</strong><br>
• Stage 1: L1/L2 Baselines & Demographics<br>
• Stage 2: Audio Enhancement & Sex Detection<br>
• Stage 3: Phoneme Inference & UltraData Mapping<br>
• Stage 4: Ultra ASR Manifold Recovery<br><br>

<strong>GDE v2 (Grammar Diagnostic Engine):</strong><br>
• Stage 5: Theory-Based Grammar Correction<br>
• Stage 6: Semantic Intent Analysis<br><br>

<strong>Powered by:</strong> Google Cloud Chirp V3 API, NVIDIA Riva, Whisper-Timestamped
</div>
""", unsafe_allow_html=True)

# Current Status
st.markdown('<h2 class="section-header">Current Status</h2>', unsafe_allow_html=True)
st.info("🚀 **MVP Development in Progress**\n\nOur team is actively developing and testing the full pipeline with 20+ test cases. Expected completion: Q3 2026")

# Contact Section
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h3 style="margin-bottom: 1rem;">Contact Us</h3>
    <p style="font-size: 1.2rem; color: #666;">
        📧 williamwlc@yahoo.com
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<p style="text-align: center; color: #666; font-size: 1rem; margin-top: 2rem;">© 2026 Classi AI. All rights reserved.</p>', unsafe_allow_html=True)
