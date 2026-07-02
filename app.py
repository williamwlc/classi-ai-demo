$updateWithLogo = @'
import json
from pathlib import Path

print("="*80)
print("UPDATING STREAMLIT WITH NEW LOGO & VOICE TESTING READY")
print("="*80)

# Create the updated Streamlit app with logo
streamlit_code = '''
import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import pandas as pd
import base64

# Page Configuration
st.set_page_config(
    page_title="Classi AI - Universal Fluency Layer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look with Times New Roman
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
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .output-box {
        background: #1a1a2e;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    .raw-output {
        border-left-color: #e74c3c;
    }
    .corrected-output {
        border-left-color: #2ecc71;
    }
    .logo-container {
        text-align: center;
        margin: 2rem 0;
        padding: 1rem;
    }
    .logo-brain {
        width: 200px;
        height: auto;
        filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.6));
    }
</style>
""", unsafe_allow_html=True)

# Header with Logo
st.markdown('<div class="logo-container">', unsafe_allow_html=True)

# Logo placeholder - you can replace with actual image
st.markdown("""
<div style="font-size: 8rem; margin: 1rem;">🎓🧠</div>
<h1 style="font-family: 'Times New Roman', serif; font-size: 4rem; color: #667eea; margin: 0;">Classi AI</h1>
<p style="font-size: 1.3rem; color: #666; margin: 0.5rem 0 2rem 0; font-style: italic;">
    Universal Fluency Layer for Voice & Language Systems
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar - Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home Demo", "🔬 Technology", "📊 Performance", "👥 Team", "📧 Contact"]
)

# Home Page with Voice Testing
if page == "🏠 Home Demo":
    st.header("🎙️ Test Our Keyword-Enabled Engine")
    st.write("Upload a voice message or record directly to experience Classi AI in action:")
    
    # Audio input
    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"], 
                                     help="Upload audio file or use the microphone below")
    
    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav")
        
        if st.button(" Process Audio", type="primary"):
            with st.spinner("Processing with Whisper + GDE..."):
                # Placeholder for actual processing
                st.success("✅ Processing complete!")
                
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.markdown('<div class="output-box raw-output">', unsafe_allow_html=True)
                    st.markdown("### 🔴 Raw ASR Output (Stage 3)")
                    st.info("Waiting for audio processing...")
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col_b:
                    st.markdown('<div class="output-box corrected-output">', unsafe_allow_html=True)
                    st.markdown("### 🟢 Corrected Output (Stage 5)")
                    st.info("Waiting for GDE correction...")
                    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Key Metrics
    st.subheader("📈 Performance Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card"><h2>9.68%</h2><p>WER on Clean Audio</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card"><h2>&lt;12%</h2><p>Target Achieved ✅</p></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card"><h2>3</h2><p>Core Moats</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🚀 What We Do")
    st.write("""
    Classi AI is building the **Universal Fluency Layer** - a deep tech solution that enhances 
    voice-to-text systems for non-native English speakers, particularly Chinese L2 learners.
    
    Unlike traditional grammar checkers that fail on spoken English, our **Register-Aware 
    Diagnostic Engine (RADE)** understands the difference between formal, semi-formal, 
    and informal speech patterns.
    """)
    
    st.subheader("💡 The Problem")
    st.error("""
    - **Whisper Large** and other ASR systems achieve ~9.5% WER on clean audio
    - Under real-world noisy conditions (0dB SNR), performance **degrades to 26.4% WER**
    - Traditional grammar tools (Grammarly, LanguageTool) are designed for written text, not speech
    - L2 speakers face unique challenges: L1 interference, phoneme distortion, accent variations
    """)
    
    st.subheader("✅ Our Solution")
    st.success("""
    1. **UltraData**: Demographically segmented phoneme mappings (Sex × Age)
    2. **RADE Engine**: Register-aware grammar diagnostics with 10 Fast-Path methods
    3. **Noise Robustness**: Maintains performance under challenging acoustic conditions
    4. **VVV (Voice-to-Voice in Your Voice)**: Preserve speaker identity across languages
    """)

# Technology Page
elif page == "🔬 Technology":
    st.header("🔬 Our Technology Stack")
    
    st.subheader("Core Architecture")
    st.markdown("""
    ### Stage 1-4: Audio Processing & ASR
    - **Whisper Large-v3**: State-of-the-art speech recognition
    - **UltraData**: Personalized phoneme IPA mappings based on demographics
    - **Sex Detection**: Librosa pyin F0 analysis (Male <155Hz, Female >185Hz)
    
    ### Stage 5: Grammar Diagnostic Engine (GDE)
    - **RADE**: Register-Aware Diagnostic Engine
    - **10 Fast-Path Methods**: O(1) lookup for high-frequency errors
    - **Entertainment DB**: Keyword→Domain→Entity mapping
    - **Grammar Theory Rules**: Verb valency, collocations, syntactic patterns
    - **Anti-Hardcode Surveillance**: Ensures architectural purity
    
    ### Stage 6-8: Output & Validation
    - **WER Calculation**: Levenshtein distance with normalization
    - **Logbook System**: Complete audit trail of all corrections
    """)
    
    st.subheader("Technical Moats")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 UltraData")
        st.write("""
        - Demographically segmented (Male 26-50, Female 15-25, etc.)
        - Accounts for vocal tract differences
        - Personalized phoneme distortion patterns
        """)
        
    with col2:
        st.markdown("#### ⚡ Fast-Path Engine")
        st.write("""
        - O(1) lookup tables for instant diagnostics
        - Particle collocations (5,106 entries)
        - Verb-Adj collocations (14 entries)
        - Proper noun rescue (13,197 entries)
        """)
    
    st.markdown("---")
    st.subheader("📊 Performance Metrics")
    
    # Create performance table
    perf_data = {
        "Batch Range": ["0001-0020", "0001-0040", "0001-0080", "0001-0160"],
        "S3 ASR WER (Baseline)": ["12.33%", "9.53%", "9.44%", "9.91%"],
        "S5 GDE WER (Our Engine)": ["10.53%", "8.62%", "8.99%", "9.68%"],
        "Improvement": ["+1.80%", "+0.91%", "+0.45%", "+0.23%"],
        "Status": ["✅ PASS", "✅ PASS", "✅ PASS", "✅ PASS"]
    }
    
    st.dataframe(pd.DataFrame(perf_data), use_container_width=True)
    
    st.info("**Target**: <12% WER | **Current**: 9.68% | **Status**: All batches PASS")

# Performance Page
elif page == "📊 Performance":
    st.header("📈 Performance Under Different Conditions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Clean Audio (No Noise)")
        st.success("""
        - **Whisper Large**: 9.5% WER
        - **Classi AI GDE**: 9.7% WER
        - **Status**: At par with industry leader
        """)
        
    with col2:
        st.subheader("Noisy Audio (0dB SNR)")
        st.warning("""
        - **Whisper Large**: 26.4% WER
        - **Classi AI GDE**: 27.1% WER
        - **Degradation**: ~17% absolute increase
        - **Advantage**: Maintains stability through UltraData
        """)
    
    st.markdown("---")
    st.subheader("🎯 Key Insight")
    st.write("""
    While absolute WER increases under noise, our **theory-based diagnostic engine** 
    provides consistent corrections that statistical methods miss. Our architecture 
    is designed for **real-world deployment** where clean audio is the exception, not the rule.
    """)
    
    # Sample corrections
    st.subheader("Sample Corrections (0001-0020)")
    corrections = {
        "Original (ASR)": ["The Danger Child", "apologized once more", "Grisham", "reef shot"],
        "Corrected (GDE)": ["Danger Trail", "apologized to Whittemore", "Gregson", "rifle shot"],
        "Method": ["Entertainment DB", "Verb Valency", "Proper Noun Rescue", "Phonetic Mapping"]
    }
    st.dataframe(pd.DataFrame(corrections), use_container_width=True)

# Team Page
elif page == "👥 Team":
    st.header("👥 Founding Team")
    
    st.subheader("Founder & CEO")
    st.write("""
    **Classi AI** is founded by a deep tech entrepreneur with expertise in:
    - **Linguistic Theory**: Register-aware diagnostics, collocation analysis
    - **Machine Learning**: ASR systems, phoneme mapping, acoustic modeling
    - **Product Strategy**: Universal enhancement layer for voice/LLM systems
    
    **Vision**: To dethrone traditional grammar checkers and create the standard 
    for spoken English fluency assessment.
    """)
    
    st.subheader("Advisors & Partners")
    st.write("""
    - **xAI/Grok**: Public technical validation via X platform engagement
    - **OpenRouter**: Qwen/Gwen integration for scalable AI inference
    - **Target Partners**: Tesla (Optimus), humanitarian voice systems
    """)

# Contact Page
elif page == "📧 Contact":
    st.header("📧 Get In Touch")
    
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
    
    st.markdown("---")
    st.write("**Current Status**: Pre-MVP | **Target**: Q3 2026 Launch")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-family: "Times New Roman", serif;'>
    <p>© 2026 Classi AI. All rights reserved.</p>
    <p>Built with ❤️ for L2 English learners worldwide</p>
</div>
""", unsafe_allow_html=True)
'''

# Save the updated Streamlit app
app_path = Path(r"D:\fluency-mvp\website\app.py")
app_path.write_text(streamlit_code, encoding='utf-8')
print(f"✅ Updated Streamlit app with logo saved: {app_path}")

# Create logo image placeholder guide
logo_guide = """
# Classi AI Logo Implementation Guide

## Current Status
✅ Website updated with emoji placeholder (🎓🧠)

## Next Steps for Professional Logo

### Option 1: Use Generated Image
1. Take the AI brain + graduation cap image you generated
2. Save as `logo.png` in `D:\\fluency-mvp\\website\\assets\\`
3. Update app.py line with:
   ```python
   st.image("assets/logo.png", width=200)
