import streamlit as st
import time
import requests
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="Classi AI", page_icon="🎯", layout="wide", initial_sidebar_state="collapsed")

# ---- Password Gate (1-hour expiration) ----
if "auth_start" not in st.session_state:
    st.session_state.auth_start = None
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Enter Password to Test Drive")
    pwd = st.text_input("Password", type="password")
    if st.button("Unlock"):
        # Replace with your real password(s)
        valid_passwords = ["friend2026", "ClassiFriend1"]
        if pwd in valid_passwords:
            st.session_state.authenticated = True
            st.session_state.auth_start = time.time()
            st.rerun()
        else:
            st.error("Invalid password")
else:
    # Check if password expired (1 hour)
    if time.time() - st.session_state.auth_start > 3600:
        st.session_state.authenticated = False
        st.session_state.auth_start = None
        st.rerun()

    st.markdown('<h1 style="text-align:center;">Classi AI</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 50%, #00d4ff 100%);
        padding: 1rem;
        border-radius: 20px;
        margin-bottom: 0.7rem;
        border: 2px solid #00ffff;
        box-shadow: 0 0 25px rgba(0,255,255,0.3);
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    ">
        <h2 style="color:#ffd966; text-align:center; margin-bottom:1rem;"> Classi AI — Deep-Tech AI Infrastructure</h2>
        <p style="font-size:1rem; line-height:1.3;">
            <strong style="color:#00ffff;">Classi AI</strong> is a deep-tech AI infrastructure company.
            Our core technology is a proprietary 
            <strong style="color:#00ffff;">Universal Fluency Layer</strong> —
            powered by advanced <em>computational linguistics</em> and proprietary 
            <em>acoustic modeling</em> — designed to enhance and complement 
            voice-to-text and LLM systems across multiple verticals, including 
            <strong style="color:#ffd966;">EdTech</strong>, 
            <strong style="color:#ffd966;">B2B</strong>, and 
            <strong style="color:#ffd966;">enterprise</strong> applications.
        </p>
        <p style="font-size:1rem; line-height:1.3;">
            Beyond enterprise infrastructure, Classi’s consumer SaaS platform is equally disruptive. 
            Engineered to serve the over <strong style="color:#ffd966;">1 billion non-native English learners</strong> globally, 
            it delivers a comprehensive suite of advanced features—some first-to-market—including our flagship 
            <strong style="color:#00ffff;">“Let’s Talk,”</strong> a highly anticipated learning solution offering 
            configurable topics, conversation types, and more. Coupled with 
            <strong style="color:#00ffff;">pronunciation guidance and articulatory diagnostics</strong>, 
            and a robust suite of tools designed to master all four core language skills, 
            our platform squarely fulfills the genuine needs of global students and standardized exam candidates.
        </p>
        <p style="font-size:1rem; line-height:1.3;">
            By leveraging our Universal Fluency Layer in these highly demanding consumer scenarios, 
            our ecosystem doesn’t just compete with legacy EdTech tools—it renders 
            <strong style="color:#ffd966;">dictionaries, translation apps, and conventional language learning platforms</strong> obsolete.
        </p>
    </div>
    """, unsafe_allow_html=True)
    # Initialize session state for history and recording count
    if "history" not in st.session_state:
        st.session_state.history = []  # list of dicts: {gt, raw, zinc, carbon, wer, time}
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

    # Backend API placeholder – replace with your actual endpoint
    BACKEND_URL = "https://your-backend-api.com/process"

    if st.button("Submit & Analyze", type="primary", disabled=audio_bytes is None or not gt_text):
        # Save audio to temporary file (Streamlit cloud supports bytes)
        import io, soundfile as sf, librosa
        audio_bytes.seek(0)
        audio_data = audio_bytes.read()
        # Convert to WAV (if not already) – using librosa to load from bytes
        import numpy as np
        try:
            audio, sr = librosa.load(io.BytesIO(audio_data), sr=16000, mono=True)
        except Exception as e:
            st.error(f"Audio loading failed: {e}")
            st.stop()

        # Send to backend (or locally if running on same machine)
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

        # Append to history (max 10)
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

    # ---- Display History and Average WER ----
    if st.session_state.history:
        st.markdown("### 📜 Recent Recordings (Ground Truth vs Corrected Transcript)")
        for entry in st.session_state.history[::-1]:
            with st.expander(f"{entry['time']} | WER: {entry['carbon_wer']:.4f}" if entry['carbon_wer'] else entry['time']):
                st.write(f"**Ground Truth:** {entry['gt']}")
                st.write(f"**Raw ASR:** {entry['raw']}")
                st.write(f"**Zinc ASR:** {entry['zinc']}")
                st.write(f"**Carbon ASR:** {entry['carbon']}")
                if entry['raw_wer'] is not None:
                    st.write(f"**WER:** Raw {entry['raw_wer']:.4f} → Zinc {entry['zinc_wer']:.4f} → Carbon {entry['carbon_wer']:.4f}")

        # Average WER after 5 recordings
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

    st.caption("Session expires 1 hour after login.")
