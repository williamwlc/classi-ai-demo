import streamlit as st

st.set_page_config(
    page_title="Classi AI",
    page_icon="",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    /* Purple Stop Button */
    div.stButton > button[data-testid="stButton"]:nth-child(2),
    .stButton > button:nth-of-type(2),
    button[kind="secondary"] {
        background-color: #9370DB !important;
        color: white !important;
        border: 2px solid #6A5ACD !important;
        font-weight: bold !important;
    }
    div.stButton > button[data-testid="stButton"]:nth-child(2):hover,
    .stButton > button:nth-of-type(2):hover {
        background-color: #8A2BE2 !important;
        border-color: #4B0082 !important;
        color: white !important;
    }
    
    /* Info Box - Navy/Cyan */
    .info-box {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%) !important;
        color: #00ffff !important;
        padding: 1.5rem !important;
        border-radius: 10px !important;
        border-left: 5px solid #00d4ff !important;
        box-shadow: 0 3px 10px rgba(0, 212, 255, 0.3) !important;
        margin-bottom: 1rem !important;
    }
    .info-box p {
        color: #e0f7ff !important;
        line-height: 1.6 !important;
        font-size: 1.1rem !important;
        margin: 0.5rem 0 !important;
    }
    .info-box strong {
        color: #00ffff !important;
        font-weight: 700 !important;
    }
    
    /* Compact spacing */
    .main-header {
        margin: 1rem 0 !important;
    }
    .section-header {
        margin: 1rem 0 0.5rem 0 !important;
    }
    hr {
        margin: 0.5rem 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header" style="text-align: center; margin-bottom: 0.5rem !important;">Classi AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #888; margin-top: 0 !important; margin-bottom: 1rem !important;">Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</p>', unsafe_allow_html=True)

# About Content
st.markdown("""
<div class="info-box">
<p><strong>Classi AI</strong> is a deep-tech AI infrastructure company. Our core technology is a proprietary <strong>Universal Fluency Layer</strong> designed to enhance and complement voice-to-text and LLM systems across multiple verticals, including EdTech, B2B, and enterprise applications.</p>
<p>Beyond enterprise infrastructure, Classi's consumer SaaS platform is <strong>equally disruptive</strong>. Engineered to serve the over <strong>1 billion non-native English learners globally</strong>, it delivers a comprehensive suite of advanced features, <strong>some first in the market</strong>—including interactive conversational practice, AI-powered tutoring, and precision pronunciation guidance across all four core language skills. By leveraging our Universal Fluency Layer in these highly demanding consumer scenarios, our ecosystem doesn't just compete with legacy EdTech tools—it renders dictionaries, translation apps, and conventional language learning platforms obsolete.</p>
</div>
""", unsafe_allow_html=True)

# Voice Conversion Section
st.markdown('<h2 class="section-header">Voice Conversion</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.button(" Start Conversion", use_container_width=True, type="primary", key="start_btn")

with col2:
    st.button("️ Stop Conversion", use_container_width=True, type="secondary", key="stop_btn")

# Contact
st.markdown("---")
st.markdown("### Contact Us")
st.markdown(" williamwlc@yahoo.com")

# Footer
st.caption("© 2026 Classi AI. All rights reserved.")
