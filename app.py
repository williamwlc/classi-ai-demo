import streamlit as st
import time
import requests
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="Classi AI — Universal Voice Filter & Correction Engine", page_icon="🎯", layout="wide", initial_sidebar_state="collapsed")

# ============================================================
# COMPANY INTRO (PUBLICLY VISIBLE)
# ============================================================
st.markdown("""
<div style="
    background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 50%, #00d4ff 100%);
    padding: 0.7rem 1rem;
    border-radius: 20px;
    margin-bottom: 0.7rem;
    border: 2px solid #00ffff;
    box-shadow: 0 0 25px rgba(0,255,255,0.3);
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
    text-align: center;
">
    <h2 style="color:#ffd966; text-align:center; margin-bottom:0.4rem; font-size:1.4rem; letter-spacing:0.5px;">Classi AI &mdash; Universal Voice Filter &amp; Correction Engine</h2>
    <p style="font-size:1.3rem; line-height:1.4; margin:0.2rem 0; font-weight:600; color:#00ffff;">
        Adapts to Heavy Accents &amp; Street Noise.
    </p>
    <p style="font-size:1.3rem; line-height:1.4; margin:0.2rem 0; font-weight:600; color:#00ffff;">
        Suppresses Major Hallucinations.
    </p>
    <p style="font-size:1rem; line-height:1.3; margin-top:1.5rem; text-align:left;">
        <strong style="color:#00ffff;">Classi AI</strong> builds a proprietary 
        <strong style="color:#00ffff;">Universal Voice Filter &amp; Correction Engine</strong> &mdash; 
        engineered to <strong style="color:#ffd966;">improve</strong> 
        voice-to-text accuracy under real-world noise, 
        <strong style="color:#ffd966;">reduce</strong> hallucination risk, and stabilize 
        downstream model outputs across 
        <strong style="color:#ffd966;">enterprise</strong>, 
        <strong style="color:#ffd966;">B2B</strong>, and 
        <strong style="color:#ffd966;">high-consequence consumer applications</strong>.
    </p>
    <p style="font-size:1rem; line-height:1.3; text-align:left;">
        The same filter works on <strong style="color:#00ffff;">any pair of languages</strong>. 
        Today we handle Chinese-accented English. More pairs follow as we grow.
    </p>
    <p style="font-size:1rem; line-height:1.3; text-align:left;">
        Leveraging this engine, Classi's consumer platform serves the global market of over 
        <strong style="color:#ffd966;">1 billion non-native English speakers</strong>. 
        Built for <strong style="color:#00ffff;">root-cause diagnostic precision</strong>, 
        the platform delivers a comprehensive suite of learning tools &mdash; including our flagship 
        <strong style="color:#00ffff;">"Let's Talk"</strong> conversational engine, 
        real-time <strong style="color:#00ffff;">articulatory diagnostics</strong>, and 
        <strong style="color:#00ffff;">structural mastery tools</strong> for standardized exam candidates.
    </p>
    <p style="font-size:1rem; line-height:1.3; text-align:left;">
        By deploying our Universal Voice Filter in these demanding consumer environments, 
        Classi raises the accuracy bar for voice-driven tools &mdash; 
        <strong style="color:#ffd966;">outperforming conventional language learning platforms</strong> 
        on the acoustic challenges that matter most.
    </p>
</div>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []
if "recording_count" not in st.session_state:
    st.session_state.recording_count = 0

# ---- Recording Section ----
col1, col2 = st.columns(2)
with col1:
    st.markdown("**🎤 Record your sentence**  \n<small>*Recommended length: at least 5 seconds*</small>", unsafe_allow_html=True)
    audio_bytes = st.audio_input("Record", label_visibility="collapsed")

with col2:
    st.markdown("**📝 Ground truth (what you said)**  \n<small>*Type or paste before/after recording*</small>", unsafe_allow_html=True)
    gt_text = st.text_area("Ground truth", placeholder="e.g., I like to read books", height=100, label_visibility="collapsed")

BACKEND_URL = "https://your-backend-api.com/process"

if st.button("Submit & Analyze", type="primary", disabled=audio_bytes is None or not gt_text):
    audio_bytes.seek(0)
    audio_data = audio_bytes.read()
    try:
        files = {"file": ("audio.wav", audio_bytes, "audio/wav")}
        data = {"ground_truth": gt_text}
        response = requests.post(BACKEND_URL, files=files, data=data, timeout=120)
        if response.status_code == 200:
            result = response.json()
            raw_asr = result.get("raw_asr", "")
            zinc_asr = result.get("zinc_asr", "")
            carbon_asr = result.get("carbon_asr", "")
            raw_wer = result.get("raw_wer", None)
            zinc_wer = result.get("zinc_wer", None)
            carbon_wer = result.get("carbon_wer", None)
        else:
            st.error(f"Backend error {response.status_code}")
            st.stop()
    except Exception as e:
        st.error(f"Connection to backend failed: {e}")
        st.stop()

    history_entry = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "gt": gt_text,
        "raw": raw_asr,
        "zinc": zinc_asr,
        "carbon": carbon_asr,
        "raw_wer": raw_wer,
        "zinc_wer": zinc_wer,
        "carbon_wer": carbon_wer,
    }
    st.session_state.history.append(history_entry)
    if len(st.session_state.history) > 10:
        st.session_state.history = st.session_state.history[-10:]
    st.session_state.recording_count += 1

if st.session_state.history:
    st.markdown("### 📜 Recent Recordings (Ground Truth vs Corrected Transcript)")
    for entry in st.session_state.history[::-1]:
        with st.expander(f"{entry['time']} | WER: {entry['carbon_wer']:.4f}" if entry['carbon_wer'] else entry['time']):
            st.write(f"**Ground Truth:** {entry['gt']}")
            st.write(f"**Raw ASR:** {entry['raw']}")
            st.write(f"**Enhanced ASR:** {entry['zinc']}")
            st.write(f"**Classi Output:** {entry['carbon']}")
            if entry['raw_wer'] is not None:
                st.write(f"**WER:** Raw {entry['raw_wer']:.4f} → Enhanced {entry['zinc_wer']:.4f} → Classi {entry['carbon_wer']:.4f}")

    if st.session_state.recording_count >= 5:
        carbon_wers = [e['carbon_wer'] for e in st.session_state.history if e['carbon_wer'] is not None]
        if carbon_wers:
            avg_wer = np.mean(carbon_wers)
            st.markdown(f"""
            <div style="background:#0b3d91;padding:1.5rem;border-radius:12px;text-align:center;">
                <h3 style="color:white;">📊 Average Word Error Rate</h3>
                <p style="font-size:2.5rem;font-weight:bold;color:#ffd966;">{avg_wer:.4f}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Complete at least 5 valid recordings to see average WER.")
    else:
        st.info(f"Record at least 5 sentences to see average WER. Currently: {st.session_state.recording_count}")
