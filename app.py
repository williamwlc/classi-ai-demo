import streamlit as st
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Classi AI Voice Recorder")
st.title("🎙️ Voice Sample Recorder")
st.write("Tap the button, speak, then stop. Download the file to build your real‑life dataset.")

# Record audio – works on mobile browsers (HTTPS required)
audio = st.audio_input("Record a voice sample")

if audio is not None:
    # Save to a local folder (create if needed)
    out_dir = Path("recordings")
    out_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sample_{timestamp}.wav"
    filepath = out_dir / filename

    with open(filepath, "wb") as f:
        f.write(audio.getbuffer())

    st.success(f"Saved {filename}")
    # Let user download the file
    with open(filepath, "rb") as f:
        st.download_button("Download recording", f, file_name=filename)
