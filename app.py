import streamlit as st

st.set_page_config(
    page_title="Classi AI - Universal Fluency Layer",
    page_icon="",
    layout="centered"
)

# Title
st.title("Classi AI")
st.markdown("### Engineering the Future of Language Conversion and Mastery with Deep-Tech AI")

st.markdown("---")

# About Section
st.header("About Classi AI")
st.info("""
**Classi AI** is a deep-tech AI infrastructure company. Our core technology is a proprietary **Universal Fluency Layer (UFL)** designed to enhance and complement voice-to-text and LLM systems across multiple verticals, including EdTech, B2B, and enterprise applications.

Beyond enterprise infrastructure, Classi's consumer SaaS platform is equally powerful. Engineered to serve the over **1 billion non-native English learners globally**, it delivers a comprehensive suite of advanced features—including interactive conversational practice, AI-powered tutoring, and precision pronunciation guidance across all four core language skills. By leveraging our Universal Fluency Layer in these highly demanding consumer scenarios, our ecosystem doesn't just compete with legacy EdTech tools—it renders dictionaries, translation apps, and conventional language learning platforms obsolete.
""")

# Technology Stack
st.header("Technology Stack")
st.success("""
**AFE v2 (Acoustic Front End):**
- Stage 1: L1/L2 Baselines & Demographics
- Stage 2: Audio Enhancement & Sex Detection
- Stage 3: Phoneme Inference & UltraData Mapping
- Stage 4: Ultra ASR Manifold Recovery

**GDE v2 (Grammar Diagnostic Engine):**
- Stage 5: Theory-Based Grammar Correction
- Stage 6: Semantic Intent Analysis

**Powered by:** Google Cloud Chirp V3 API, NVIDIA Riva, Whisper-Timestamped
""")

# Contact
st.markdown("---")
st.markdown("### Contact Us")
st.markdown("📧 williamwlc@yahoo.com")

# Footer
st.markdown("---")
st.caption("© 2026 Classi AI. All rights reserved.")
