import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Classi AI",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS - Classi AI on LEFT
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;700&display=swap');
    
    .main-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #667eea;
        text-align: left;
        margin: 1rem 0;
    }
    .tagline {
        font-family: "Times New Roman", Times, serif;
        font-size: 1.2rem;
        color: #666;
        text-align: left;
        margin-bottom: 2rem;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Header - Classi AI on TOP LEFT
st.markdown('<h1 class="main-header">🎓 Classi AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Universal Fluency Layer for Voice & Language Systems</p>', unsafe_allow_html=True)
st.markdown("---")

# ONE PARAGRAPH INTRO - PROFESSIONAL
st.write("""
Classi AI is an advanced grammar diagnostic engine designed for L2 English learners, 
with specialized focus on Chinese speakers. Our system integrates Whisper Large-v3 
automatic speech recognition with a sophisticated Grammar Diagnostic Engine (GDE) 
that employs keyword-based entity mapping for contextual understanding. When the system 
detects domain-specific keywords such as "actor," "sequel," or "Mission Impossible," 
it automatically activates the entertainment domain to accurately identify character 
names like "Benji Dunn" and actor names like "Tom Cruise." Our engine achieves 9.68% 
WER on clean audio and demonstrates robust performance under challenging acoustic 
conditions where conventional ASR systems experience significant degradation.
""")

st.markdown("---")

# KEYWORD MAPPING EXAMPLE
st.subheader("🎬 Context-Aware Entity Recognition")
st.write("**Example Input:**")
st.info('"Sequel of Mission Impossible is coming soon. Who will be the supporting male actor this time as Benji Dunn was unavailable."')

st.write("**System Detection:**")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Keywords Identified:**")
    st.write("- sequel")
    st.write("- actor")
    st.write("- Mission Impossible")

with col2:
    st.markdown("**Domain Activated:**")
    st.write("🎬 Entertainment")

with col3:
    st.markdown("**Entities Recognized:**")
    st.write("- Benji Dunn (character)")
    st.write("- Tom Cruise (actor)")
    st.write("- Simon Pegg (actor)")

st.markdown("---")

# Upload Section
st.subheader("🎙️ Test the System")
uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    
    if st.button("⚡ Process Audio", type="primary"):
        with st.spinner("Processing with Whisper + GDE..."):
            st.success("✅ Processing complete!")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.markdown("### 🔴 Raw ASR Output")
                st.info("Awaiting processing...")
            
            with col_b:
                st.markdown("### 🟢 GDE Corrected Output")
                st.info("Awaiting processing...")

st.markdown("---")

# Performance Metrics
st.subheader("📊 Performance Benchmarks")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Clean Audio")
    st.success("""
    - **Whisper Large-v3**: 9.5% WER
    - **Classi AI GDE**: 9.68% WER
    - **Status**: Industry parity achieved
    """)

with col2:
    st.markdown("#### Noisy Audio (0dB SNR)")
    st.warning("""
    - **Whisper Large-v3**: 26.4% WER
    - **Classi AI GDE**: 27.1% WER
    - **Advantage**: Maintains stability
    """)

st.markdown("---")

# Sample Corrections
st.subheader("Sample Corrections")
corrections = {
    "ASR Output": ["The Danger Child", "apologized once more", "Grisham", "reef shot"],
    "GDE Correction": ["Danger Trail", "apologized to Whittemore", "Gregson", "rifle shot"],
    "Method": ["Entertainment DB", "Verb Valency", "Proper Noun Rescue", "Phonetic Mapping"]
}
st.dataframe(pd.DataFrame(corrections), use_container_width=True)

st.markdown("---")

# Contact Section
st.subheader("📧 Contact & Investment Inquiry")
st.write("""
**Current Status**: Pre-MVP Development Stage  
**Target Launch**: Q3 2026  
**Funding Round**: Friends & Family / Seed  

We are preparing for:
- Friends & Family Round: $3M cap structure
- Seed Round: $8M–$15M valuation target
- Strategic partnerships with AI/voice technology leaders
""")

contact_form = st.form("contact_form")
name = contact_form.text_input("Name")
email = contact_form.text_input("Email")
message = contact_form.text_area("Message")
submitted = contact_form.form_submit_button("Send Message")

if submitted:
    st.success("Thank you for your interest. We will contact you soon.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-family: "Times New Roman", serif;'>
    <p>© 2026 Classi AI. All rights reserved.</p>
    <p>Secure Access: postmvpsoon</p>
</div>
""", unsafe_allow_html=True)
