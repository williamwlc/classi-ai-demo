import streamlit as st
import time
from datetime import datetime
from transformers import pipeline
import os
from pathlib import Path

st.set_page_config(page_title="Classi AI", layout="wide")

# Load lightweight AI model for real transcription
@st.cache_resource
def load_asr_model():
    return pipeline("automatic-speech-recognition", model="openai/whisper-tiny")

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'session_start' not in st.session_state:
    st.session_state.session_start = datetime.now()

# Custom CSS for larger fonts and spacing adjustments
st.markdown("""
<style>
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    .subtitle {
        font-size: 1.4rem !important;
        color: #a0a0a0 !important;
        margin-top: 0 !important;
        margin-bottom: 2rem !important;
    }
    .section-header {
        font-size: 2rem !important;
        margin-top: 0 !important;
        margin-bottom: 0.5rem !important;
    }
    .info-box {
        font-size: 1.15rem !important;
        line-height: 1.8 !important;
        padding: 1.5rem !important;
        margin-bottom: 2rem !important;
    }
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.15rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Main page layout
st.markdown('<h1 class="main-title">🎙️ Classi AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</p>', unsafe_allow_html=True)

# Password protection (optional)
with st.sidebar:
    st.header("Access Control")
    password = st.text_input("Access Password", type="password")
    st.markdown("---")
    st.info("Dev Demo | Address Bar displays ClassiAIhk.com via Streamlit domain masking")

# About Classi AI Section
st.markdown('<h2 class="section-header">About Classi AI</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
<p><strong>Classi AI</strong> is a deep-tech AI infrastructure company. Our core technology is a proprietary <strong>Universal Fluency Layer</strong> designed to enhance and complement voice-to-text and LLM systems across multiple verticals, including EdTech, B2B, and enterprise applications.</p>

<p>Beyond enterprise infrastructure, Classi's consumer SaaS platform is equally powerful. Engineered to serve the over <strong>1 billion non-native English learners globally</strong>, it delivers a comprehensive suite of advanced features—including interactive conversational practice, AI-powered tutoring, and precision pronunciation guidance across all four core language skills. By leveraging our Universal Fluency Layer in these highly demanding consumer scenarios, our ecosystem doesn't just compete with legacy EdTech tools—it renders dictionaries, translation apps, and conventional language learning platforms obsolete.</p>
</div>
""", unsafe_allow_html=True)

# Voice Microphone Section (DISABLED - MVP Debug Pending)
st.markdown('<h2 class="section-header"> Voice Microphone</h2>', unsafe_allow_html=True)
st.warning("⚠️ Voice recording features are temporarily disabled during final MVP debugging. Please check back soon.")

# Footer
st.markdown("---")
st.markdown('<p style="text-align: center; color: #666; font-size: 1.1rem;">© 2026 Classi AI. All rights reserved.</p>', unsafe_allow_html=True)
