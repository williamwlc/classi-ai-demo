import streamlit as st
from datetime import datetime
from pathlib import Path
import base64
import hashlib

st.set_page_config(page_title="Classi AI Voice Recorder")
st.title("🎙️ Voice Sample Recorder")
st.markdown("""
**Important:** Keep this page open while recording.  
Switching to another app will **stop** the recording (mobile browser limitation).
""")

# Initialize session state
if "recordings" not in st.session_state:
    st.session_state.recordings = []
if "last_audio_hash" not in st.session_state:
    st.session_state.last_audio_hash = None

# Record audio (mobile‑compatible)
audio = st.audio_input("Record a voice sample")

if audio is not None:
    # Compute a hash of the audio bytes to detect if it's a new recording
    audio_bytes = audio.getbuffer()
    audio_hash = hashlib.md5(audio_bytes).hexdigest()

    # Only save if this is a new recording (not the same as last saved)
    if audio_hash != st.session_state.last_audio_hash:
        out_dir = Path("recordings")
        out_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sample_{timestamp}.wav"
        filepath = out_dir / filename

        # Optional: avoid overwriting if file exists
        if not filepath.exists():
            with open(filepath, "wb") as f:
                f.write(audio_bytes)

            st.session_state.recordings.append(str(filepath))
            st.session_state.last_audio_hash = audio_hash
            st.success(f"Saved {filename}")
        else:
            st.info(f"File {filename} already exists – skipping duplicate.")
    else:
        st.info("Same audio detected – not saving duplicate.")

# Show all recordings and download buttons
if st.session_state.recordings:
    st.subheader("Your recorded clips")
    for filepath in st.session_state.recordings:
        fname = Path(filepath).name
        with open(filepath, "rb") as f:
            st.download_button(
                label=f"Download {fname}",
                data=f,
                file_name=fname
            )
    # Clear all button
    if st.button("Clear all recordings"):
        for fp in st.session_state.recordings:
            Path(fp).unlink(missing_ok=True)
        st.session_state.recordings = []
        st.session_state.last_audio_hash = None  # reset to allow new recordings
        st.rerun()
