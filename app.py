import streamlit as st
import numpy as np
import librosa
import soundfile as sf
import whisper
import jiwer
import re
import io
import tempfile
from pathlib import Path

# ---------- page config (unchanged) ----------
st.set_page_config(
    page_title="Classi AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get Help": None, "Report a bug": None},
)

# ---------- mobile CSS (unchanged) ----------
st.markdown("""
<style>
@media (max-width: 768px) {
    .main > div { padding-top: 2rem; padding-left: 1rem; padding-right: 1rem; }
    h1 { font-size: 1.5rem; }
    h2 { font-size: 1.2rem; }
}
</style>
""", unsafe_allow_html=True)

# ---------- custom button + info box (unchanged) ----------
st.markdown("""
<style>
    div.stButton > button[data-testid="stButton"]:nth-child(2),
    .stButton > button:nth-of-type(2),
    button[kind="secondary"] {
        background-color: #9370DB !important; color: white !important;
        border: 2px solid #6A5ACD !important; font-weight: bold !important; font-size: 1.1rem !important;
    }
    div.stButton > button[data-testid="stButton"]:nth-child(2):hover,
    .stButton > button:nth-of-type(2):hover {
        background-color: #8A2BE2 !important; border-color: #4B0082 !important; color: white !important;
    }
    div.stButton > button[data-testid="stButton"]:first-child,
    .stButton > button:nth-of-type(1),
    button[kind="primary"] {
        font-size: 1.1rem !important; font-weight: bold !important;
    }
    .info-box {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%) !important;
        color: #00ffff !important; padding: 1.5rem !important; border-radius: 10px !important;
        border-left: 5px solid #00d4ff !important; box-shadow: 0 3px 10px rgba(0,212,255,0.3) !important;
        margin-bottom: 1rem !important;
    }
    .info-box p { color: #e0f7ff !important; line-height: 1.6 !important; font-size: 1.1rem !important; margin: 0.5rem 0 !important; }
    .info-box strong { color: #00ffff !important; font-weight: 700 !important; }
    .main-header { margin: 1rem 0 !important; }
    .section-header { margin: 1rem 0 0.5rem 0 !important; font-size: 2.2rem !important; }
    hr { margin: 0.5rem 0 !important; }
</style>
""", unsafe_allow_html=True)

# ---------- AFE functions (same as before) ----------
def afe_stage1_noise_reduction(y, sr):
    S = librosa.stft(y)
    magnitude, phase = librosa.magphase(S)
    noise_mag = np.mean(magnitude[:, :int(sr * 0.1)], axis=1, keepdims=True)
    mask = (magnitude > 2 * noise_mag).astype(float)
    magnitude_clean = magnitude * mask
    S_clean = magnitude_clean * phase
    return librosa.istft(S_clean, length=len(y))

def afe_stage2_dereverberation(y, sr):
    return librosa.effects.preemphasis(y)

def afe_stage3_normalization(y):
    peak = np.max(np.abs(y))
    if peak > 0:
        y = y / peak * 0.95
    return y

def afe_stage4_pitch_extraction(y, sr):
    f0, _, _ = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    return np.nanmedian(f0)

def afe_pipeline(y, sr):
    y = afe_stage1_noise_reduction(y, sr)
    y = afe_stage2_dereverberation(y, sr)
    y = afe_stage3_normalization(y)
    pitch = afe_stage4_pitch_extraction(y, sr)
    return y, pitch

# ---------- load Whisper once ----------
@st.cache_resource
def load_whisper():
    return whisper.load_model("large-v3", device="cpu")

model = load_whisper()

# ---------- header (unchanged) ----------
st.markdown('<h1 class="main-header" style="text-align: center;">Classi AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #888;">Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</p>', unsafe_allow_html=True)

# ---------- About (unchanged) ----------
st.markdown("""
<div class="info-box">
<p><strong>Classi AI</strong> is a deep-tech AI infrastructure company. Our core technology is a proprietary <strong>Universal Fluency Layer</strong>—powered by advanced computational linguistics and proprietary acoustic modeling—designed to enhance and complement voice-to-text and LLM systems across multiple verticals, including EdTech, B2B, and enterprise applications.</p>
<p>Beyond enterprise infrastructure, Classi's consumer SaaS platform is equally disruptive. Engineered to serve the over 1 billion non-native English learners globally, it delivers a comprehensive suite of advanced features—some first-to-market—including our flagship "Let's Talk," a highly anticipated learning solution offering configurable topics, conversation types, and more. Coupled with <strong>pronunciation guidance and articulatory diagnostics</strong>, and a robust suite of tools designed to master all four core language skills, our platform squarely fulfills the genuine needs of global students and standardized exam candidates. By leveraging our Universal Fluency Layer in these highly demanding consumer scenarios, our ecosystem doesn't just compete with legacy EdTech tools—it renders dictionaries, translation apps, and conventional language learning platforms obsolete.</p>
</div>
""", unsafe_allow_html=True)

# ---------- Voice Conversion Section ----------
st.markdown('<h2 class="section-header">Voice Conversion</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    audio_data = st.audio_input("Record your voice", key="recorder")
with col2:
    ground_truth_text = st.text_input("Enter the text now or after the recording.", placeholder="What you really said...")

if audio_data is not None:
    # Read audio bytes
    audio_bytes = audio_data.getvalue()
    # Load with librosa
    y, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
    st.audio(audio_bytes, format="audio/wav")

    # ---------- AFE processing ----------
    with st.spinner("Applying AFE enhancement..."):
        y_clean, pitch = afe_pipeline(y, sr)
        # Save enhanced audio to a buffer for playback
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            sf.write(tmp.name, y_clean, sr)
            enhanced_audio_path = tmp.name

    st.success("AFE completed.")
    st.audio(enhanced_audio_path, format="audio/wav")

    # ---------- Whisper transcription ----------
    with st.spinner("Transcribing with Whisper v3..."):
        result = model.transcribe(enhanced_audio_path, language="en")
        transcript = result["text"].strip()

    st.subheader("Transcription")
    st.write(transcript)

    # ---------- WER if ground truth provided ----------
    if ground_truth_text.strip():
        ref = ground_truth_text.strip().lower()
        hyp = transcript.lower()
        # Clean punctuation
        ref = re.sub(r'[^a-z0-9 ]', '', ref)
        hyp = re.sub(r'[^a-z0-9 ]', '', hyp)
        wer_score = jiwer.wer(ref, hyp)
        st.metric("Word Error Rate (WER)", f"{wer_score:.2%}")
    else:
        st.info("Enter the expected text above to calculate WER.")

# ---------- Footer (unchanged) ----------
st.markdown("---")
st.markdown("### Contact Us: William@ClassiAIhk.com")
st.caption("© 2026 Classi AI. All rights reserved.")
st.markdown("""
<p style="color: #808080; font-size: 17px; margin: 5px 0; line-height: 1.3;">
© Powered by <span style="color: #00FFFF; font-weight: 700;">Nvidia</span> Build.<br>
Cloud Partner: To be confirmed.
</p>
""", unsafe_allow_html=True)
