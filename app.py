import streamlit as st
from datetime import datetime
from pathlib import Path
import base64

st.set_page_config(page_title="Classi AI Voice Recorder")
st.title("🎙️ Voice Sample Recorder")
st.markdown("""
**Important:** Keep this page open while recording.  
Switching to another app will **stop** the recording (mobile browser limitation).
""")

# Initialize session state for recording list
if "recordings" not in st.session_state:
    st.session_state.recordings = []

# Record audio (mobile‑compatible)
audio = st.audio_input("Record a voice sample")

if audio is not None:
    # Save to server (Streamlit Cloud instance)
    out_dir = Path("recordings")
    out_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sample_{timestamp}.wav"
    filepath = out_dir / filename

    with open(filepath, "wb") as f:
        f.write(audio.getbuffer())

    # Store metadata
    st.session_state.recordings.append(str(filepath))
    st.success(f"Saved {filename}")

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
        st.rerun()
