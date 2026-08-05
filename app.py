import streamlit as st
import os
from datetime import datetime

# Server-side save folder (optional – only if you want a copy on the server)
SAVE_DIR = r"D:\ufl_test_data\Will_Real_Data\tv_mediumhigh"
os.makedirs(SAVE_DIR, exist_ok=True)

st.title("Voice Recorder")

audio = st.audio_input("Press microphone to record")

if audio is not None:
    st.session_state["current_audio_bytes"] = audio.getvalue()

if "current_audio_bytes" in st.session_state:
    st.audio(st.session_state["current_audio_bytes"])
    
    # Option 1: Save to server (optional)
    if st.button("Save to Server"):
        filename = f"sample_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        filepath = os.path.join(SAVE_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(st.session_state["current_audio_bytes"])
        st.success(f"✅ Saved to server: {filename}")
        # Do NOT delete state – user may also want to download
    
    # Option 2: Download to your phone/computer (this is the key!)
    st.download_button(
        label="📥 Download to your device",
        data=st.session_state["current_audio_bytes"],
        file_name=f"sample_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav",
        mime="audio/wav"
    )
    
    # Clear button to reset for next recording
    if st.button("Clear and record next"):
        del st.session_state["current_audio_bytes"]
        st.rerun()
