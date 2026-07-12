import streamlit as st

st.set_page_config(
    page_title="Classi AI",
    page_icon="",
    layout="centered"
)

# Custom CSS for button styling
st.markdown("""
<style>
    .stop-button > div > button {
        background-color: #D8BFD8 !important;
        color: #4B0082 !important;
        border: 2px solid #9370DB !important;
        font-weight: bold !important;
    }
    .stop-button > div > button:hover {
        background-color: #DDA0DD !important;
        border-color: #8A2BE2 !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Classi AI")
st.markdown("### Engineering the Future of Language Conversion and Mastery with Deep-Tech AI")

st.markdown("---")

# About Section
st.header("About Classi AI")
st.info("""
**Classi AI** is a deep-tech AI infrastructure company developing advanced solutions for voice AI and language learning applications.

Our platform is designed to serve the global market with innovative AI-powered tools for enhanced communication and learning experiences.
""")

# Voice Recording Section
st.markdown("---")
st.header("Voice Recording")

col1, col2 = st.columns(2)
with col1:
    if st.button("🎤 Start Recording", use_container_width=True, type="primary"):
        st.warning("⚠️ Features coming soon - MVP in development")

with col2:
    # Add custom CSS class for purple button
    st.markdown('<div class="stop-button">', unsafe_allow_html=True)
    if st.button("⏹️ Stop Recording", use_container_width=True):
        st.info("ℹ️ Recording stopped")
    st.markdown('</div>', unsafe_allow_html=True)

# Contact
st.markdown("---")
st.markdown("### Contact Us")
st.markdown("📧 williamwlc@yahoo.com")

# Footer
st.markdown("---")
st.caption("© 2026 Classi AI. All rights reserved.")
