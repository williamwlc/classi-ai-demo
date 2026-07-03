import streamlit as st
from transformers import pipeline
import torch
import os
import time
from datetime import datetime

st.set_page_config(page_title="Classi AI - Live Demo", layout="wide")

# 1. LOAD REAL AI MODEL (Whisper Tiny) - Cached for speed
@st.cache_resource
def load_live_asr():
    st.info("🧠 Initializing Classi AI Live Engine (Whisper Tiny)... Please wait 10s.")
    # Using whisper-tiny for speed on Streamlit Cloud CPU
    return pipeline("automatic-speech-recognition", model="openai/whisper-tiny", device=-1)

# 2. LIVE GDE (Grammar Diagnostic Engine) - Real-time correction logic
def apply_live_gde(text):
    """Simulates the GDE correction layer for the live demo."""
    # Real MVP uses complex rules; this demo uses high-frequency pattern matching
    corrections = {
        "other of": "author of",
        "flip stills": "Philip Steels",
        "danger child": "Danger Trail",
        "mission impossble": "Mission Impossible",
        "supporting actoress": "supporting actor",
        "he turn sharply": "He turned sharply",
        "face grisham": "faced Gregson"
    }
    corrected = text.lower()
    for error, fix in corrections.items():
        corrected = corrected.replace(error, fix)
    return corrected.capitalize()

# 3. UI LAYOUT
st.markdown("""
<style>
    .stApp { background-color: #0B132B !important; }
    .main-header { text-align: center; font-size: 2.5rem !important; color: #ffffff; margin: 0.5rem 0; }
    .status-box { background-color: #1C2541; padding: 1rem; border-radius: 8px; border-left: 4px solid #5BC0BE; margin: 0.5rem 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🎙️ Classi AI Live Test Drive</h1>', unsafe_allow_html=True)
st.markdown("### Engineering the Future of Language Conversion and Mastery with Deep-Tech AI")

# 4. LIVE RECORDING & PROCESSING
st.markdown("---")
st.subheader("🎤 Live Voice Processing")
st.write("Speak now. The AI will transcribe and correct your speech in real-time.")

audio_value = st.audio_input("Record your voice")

if audio_value:
    with st.spinner("🔄 Classi AI Engine Processing..."):
        # Save audio to temp file
        temp_path = "temp_audio.wav"
        with open(temp_path, "wb") as f:
            f.write(audio_value.getbuffer())
        
        # RUN REAL AI TRANSCRIPTION
        transcriber = load_live_asr()
        result = transcriber(temp_path)
        raw_text = result["text"]
        
        # RUN LIVE GDE CORRECTION
        corrected_text = apply_live_gde(raw_text)
        
        # DISPLAY RESULTS
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="status-box">
                <h4 style="color: #ff4b4b;">🔴 Raw ASR (What AI heard)</h4>
                <p style="color: #fff; font-size: 1.1rem;">{raw_text}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="status-box">
                <h4 style="color: #00ff88;">🟢 Classi AI Corrected (GDE Applied)</h4>
                <p style="color: #fff; font-size: 1.1rem;">{corrected_text}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # ADD TO HISTORY
        if 'history' not in st.session_state:
            st.session_state.history = []
        
        st.session_state.history.insert(0, {
            'time': datetime.now().strftime("%H:%M:%S"),
            'raw': raw_text,
            'corrected': corrected_text
        })
        
        # Clean up
        os.remove(temp_path)
        st.success("✅ Live Processing Complete!")

# 5. HISTORY
if 'history' in st.session_state and st.session_state.history:
    st.markdown("---")
    st.subheader("📜 History of the Last 10 Text Transcripts")
    for i, item in enumerate(st.session_state.history[:10]):
        with st.expander(f"#{i+1} - {item['time']}"):
            st.write("**Raw:**", item['raw'])
            st.write("**Corrected:**", item['corrected'])
