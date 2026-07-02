import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Classi AI - Universal Fluency Layer",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;700&display=swap');
    
    .main-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    .tagline {
        font-family: "Times New Roman", Times, serif;
        font-size: 1.3rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
        font-style: italic;
    }
    .logo-container {
        text-align: center;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Logo and Header
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.markdown("""
<div style="font-size: 8rem; margin: 1rem;">🎓🧠</div>
<h1 class="main-header">Classi AI</h1>
<p class="tagline">Universal Fluency Layer for Voice & Language Systems</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

# Main Content - Single Page
st.header("🎙️ Test Our Keyword-Enabled Engine")
st.write("Upload a voice message to experience Classi AI in action:")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    
    if st.button("⚡ Process Audio", type="primary"):
        with st.spinner("Processing with Whisper + GDE..."):
            st.success("✅ Processing complete!")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.markdown("### 🔴 Raw ASR Output")
                st.info("Waiting for audio processing...")
            
            with col_b:
                st.markdown("### 🟢 Corrected Output")
                st.info("Waiting for GDE correction...")

st.markdown("---")

st.subheader("💡 The Problem")
st.error("""
- **Whisper Large** and other ASR systems achieve ~9.5% WER on clean audio
- Under real-world noisy conditions (0dB SNR), performance **degrades to 26.4% WER**
- Traditional grammar tools (Grammarly, LanguageTool) are designed for written text, not speech
- L2 speakers face unique challenges: L1 interference, phoneme distortion, accent variations
""")

st.markdown("---")

st.subheader("Sample Corrections (0001-0020)")
corrections = {
    "Original (ASR)": ["The Danger Child", "apologized once more", "Grisham", "reef shot"],
    "Corrected (GDE)": ["Danger Trail", "apologized to Whittemore", "Gregson", "rifle shot"],
    "Method": ["Entertainment DB", "Verb Valency", "Proper Noun Rescue", "Phonetic Mapping"]
}
st.dataframe(pd.DataFrame(corrections), use_container_width=True)

st.markdown("---")

st.subheader("📧 Get In Touch")
st.write("""
We're currently in **pre-MVP stage** and preparing for:
- **Friends & Family Round**: $3M cap or personal loan structure
- **Seed Round**: $8M-$15M valuation target
- **xAI BD Outreach**: Post <12% WER validation

**Interested in partnering or investing?**
""")

contact_form = st.form("contact_form")
name = contact_form.text_input("Name")
email = contact_form.text_input("Email")
message = contact_form.text_area("Message")
submitted = contact_form.form_submit_button("Send Message")

if submitted:
    st.success("Thank you for your interest! We'll be in touch soon.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-family: "Times New Roman", serif;'>
    <p>© 2026 Classi AI. All rights reserved.</p>
    <p>Built with ❤️ for L2 English learners worldwide</p>
</div>
""", unsafe_allow_html=True)
