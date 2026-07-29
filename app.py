import streamlit as st
from audio_recorder_streamlit import audio_recorder
import time
import jiwer
import re

# ============================================================
# PASSWORD PROTECTION
# ============================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Classi AI - Access Restricted")
    password = st.text_input("Enter password:", type="password")
    if st.button("Login"):
        if password == "bftf2026":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password")
    st.stop()

# ============================================================
# MAIN APP
# ============================================================

st.set_page_config(
    page_title="Classi AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
    }
)

# Mobile-responsive CSS
st.markdown("""
    <style>
    @media (max-width: 768px) {
        .main > div {
            padding-top: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        h1 { font-size: 1.5rem; }
        h2 { font-size: 1.2rem; }
    }
    </style>
""", unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
    div.stButton > button {
        font-size: 1.1rem !important;
        font-weight: bold !important;
    }
    
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
    
    .main-header {
        margin: 1rem 0 !important;
    }
    .section-header {
        margin: 1rem 0 0.5rem 0 !important;
        font-size: 2.2rem !important;
    }
    
    .wer-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
        color: #00ff88 !important;
        padding: 1.5rem !important;
        border-radius: 10px !important;
        border-left: 5px solid #00ff88 !important;
        box-shadow: 0 3px 10px rgba(0, 255, 136, 0.3) !important;
        margin: 1rem 0 !important;
    }
    .wer-box h3 {
        color: #00ff88 !important;
        margin-top: 0 !important;
    }
    .wer-box p {
        color: #e0ffe0 !important;
        line-height: 1.6 !important;
        font-size: 1rem !important;
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
<p><strong>Classi AI</strong> is a deep-tech AI infrastructure company. Our core technology is a proprietary <strong>Universal Fluency Layer</strong>—powered by advanced computational linguistics and proprietary acoustic modeling—designed to enhance and complement voice-to-text and LLM systems across multiple verticals, including EdTech, B2B, and enterprise applications.</p>
<p>Beyond enterprise infrastructure, Classi's consumer SaaS platform is equally disruptive. Engineered to serve the over 1 billion non-native English learners globally, it delivers a comprehensive suite of advanced features—some first-to-market—including our flagship "Let's Talk," a highly anticipated learning solution offering configurable topics, conversation types, and more. Coupled with <strong>pronunciation guidance and articulatory diagnostics</strong>, and a robust suite of tools designed to master all four core language skills, our platform squarely fulfills the genuine needs of global students and standardized exam candidates. By leveraging our Universal Fluency Layer in these highly demanding consumer scenarios, our ecosystem doesn't just compete with legacy EdTech tools—it renders dictionaries, translation apps, and conventional language learning platforms obsolete.</p>
</div>
""", unsafe_allow_html=True)

# Voice Conversion Section
st.markdown('<h2 class="section-header">Voice Conversion</h2>', unsafe_allow_html=True)

# Session state initialization
if "recording" not in st.session_state:
    st.session_state.recording = False
if "audio_data" not in st.session_state:
    st.session_state.audio_data = None
if "ground_truth" not in st.session_state:
    st.session_state.ground_truth = ""
if "transcript" not in st.session_state:
    st.session_state.transcript = ""
if "wer_score" not in st.session_state:
    st.session_state.wer_score = None

# Ground Truth Input Box (ABOVE Start Recording)
st.markdown("### 📝 Ground Truth Text")
ground_truth_input = st.text_area(
    "Type or paste the correct transcript here:",
    value=st.session_state.ground_truth,
    height=80,
    placeholder="e.g., The quick brown fox jumps over the lazy dog.",
    key="gt_input"
)

# Update ground truth when user types
if ground_truth_input != st.session_state.ground_truth:
    st.session_state.ground_truth = ground_truth_input

# Recording buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎤 Start Recording", use_container_width=True, type="primary", key="start_btn"):
        st.session_state.recording = True
        st.session_state.audio_data = None
        st.session_state.transcript = ""
        st.session_state.wer_score = None

with col2:
    if st.button("⏹️ Stop & Transcribe", use_container_width=True, type="secondary", key="stop_btn"):
        st.session_state.recording = False
        # Placeholder for transcription (replace with actual ASR call)
        if st.session_state.audio_data:
            st.session_state.transcript = "[Transcript will appear here after ASR processing]"

with col3:
    if st.button("🔄 Reset", use_container_width=True, key="reset_btn"):
        st.session_state.recording = False
        st.session_state.audio_data = None
        st.session_state.ground_truth = ""
        st.session_state.transcript = ""
        st.session_state.wer_score = None
        st.rerun()

# Audio recorder (only shows when recording)
if st.session_state.recording:
    st.markdown("### 🔴 Recording in progress... Speak clearly...")
    audio_bytes = audio_recorder(
        text="",
        recording_color="#e74c3c",
        neutral_color="#3498db",
        icon_size="2x",
        pause_threshold=60.0,
        sample_rate=16000,
    )
    if audio_bytes:
        st.session_state.audio_data = audio_bytes
        st.session_state.recording = False
        st.rerun()

# Show recorded audio
if st.session_state.audio_data:
    st.audio(st.session_state.audio_data, format="audio/wav")
    st.success(f"✅ Recording saved ({len(st.session_state.audio_data)/1000:.1f} KB)")

# ============================================================
# VOICE TO TEXT CONVERSION AREA
# ============================================================
st.markdown("---")
st.markdown("## 📊 Voice-to-Text Conversion")

gt_col, trans_col = st.columns(2)

with gt_col:
    st.markdown("### Ground Truth Text")
    if st.session_state.ground_truth:
        st.info(st.session_state.ground_truth)
    else:
        st.warning("No ground truth entered. Type it above.")

with trans_col:
    st.markdown("### Transcript")
    if st.session_state.transcript:
        st.success(st.session_state.transcript)
        
        # Calculate WER
        if st.session_state.ground_truth:
            # Clean texts for WER calculation
            ref_clean = re.sub(r'[^a-zA-Z0-9\s]', '', st.session_state.ground_truth.lower())
            hyp_clean = re.sub(r'[^a-zA-Z0-9\s]', '', st.session_state.transcript.lower())
            
            if ref_clean and hyp_clean:
                try:
                    wer = jiwer.wer(ref_clean, hyp_clean)
                    st.session_state.wer_score = wer
                except:
                    st.session_state.wer_score = None
    else:
        st.warning("No transcript yet. Record audio and click 'Stop & Transcribe'.")

# WER Display
if st.session_state.wer_score is not None:
    st.markdown(f"""
    <div class="wer-box">
        <h3>📈 Word Error Rate (WER)</h3>
        <p style="font-size: 2rem; font-weight: bold; text-align: center; margin: 1rem 0;">
            {st.session_state.wer_score:.2%}
        </p>
        <p style="text-align: center; color: #aaa;">
            Lower WER = Better Accuracy
        </p>
    </div>
    """, unsafe_allow_html=True)
elif st.session_state.transcript and st.session_state.ground_truth:
    st.error("Unable to calculate WER. Ensure both texts contain recognizable words.")

# Contact
st.markdown("---")
st.markdown("### Contact Us: William@ClassiAIhk.com")

# Footer
st.caption("© 2026 Classi AI. All rights reserved.")

st.markdown("""
<p style="color: #808080; font-size: 17px; margin: 5px 0; line-height: 1.3;">
© Powered by <span style="color: #00FFFF; font-weight: 700;">Nvidia</span> Build.<br>
Cloud Partner: To be confirmed.
</p>
""", unsafe_allow_html=True)
