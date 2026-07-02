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

# ONE PARAGRAPH INTRO
st.write("""
Classi AI is a revolutionary grammar diagnostic engine designed specifically for L2 English learners, 
particularly Chinese speakers. Our technology combines **Whisper Large-v3** ASR with an advanced 
**Grammar Diagnostic Engine (GDE)** that uses keyword-based entity mapping to understand context. 
For example, when our system detects keywords like "actor," "sequel," or "Mission Impossible," it 
automatically triggers the movies domain to correctly identify character names like "Benji Dunn" and 
actor names like "Tom Cruise," achieving **9.68% WER** on clean audio and maintaining robust performance 
even under noisy conditions where traditional ASR systems fail.
""")

st.markdown("---")

# MISSION IMPOSSIBLE EXAMPLE
st.subheader("🎬 Keyword Mapping in Action")
st.write("**Example:** When you say:")
st.info('"Sequel of Mission Impossible is coming soon. Who will be the supporting male actor this time as Benji Dunn was dead."')

st.write("**Our GDE detects:**")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Keywords:**")
    st.write("- sequel")
    st.write("- actor")
    st.write("- Mission Impossible")

with col2:
    st.markdown("**Domain:**")
    st.write("🎬 Movies")

with col3:
    st.markdown("**Entities:**")
    st.write("- Benji Dunn (character)")
    st.write("- Tom Cruise (actor)")
    st.write("- Simon Pegg (actor)")

st.markdown("---")

# Upload Section
st.subheader("🎙️ Test It Now")
uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    
    if st.button("⚡ Process", type="primary"):
        with st.spinner("Processing..."):
            st.success("✅ Done!")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.markdown("### 🔴 Raw ASR")
                st.info("Waiting...")
            
            with col_b:
                st.markdown("### 🟢 Corrected")
                st.info("Waiting...")

st.markdown("---")

# Contact
st.subheader("📧 Contact")
st.write("**Pre-MVP Stage** | Target: Q3 2026 Launch")

contact_form = st.form("contact")
name = contact_form.text_input("Name")
email = contact_form.text_input("Email")
msg = contact_form.text_area("Message")
submitted = contact_form.form_submit_button("Send")

if submitted:
    st.success("Thank you!")
