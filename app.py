import streamlit as st
import os
from datetime import datetime

SAVE_DIR = r"D:\ufl_test_data\Will_Real_Data\tv_mediumhigh"
os.makedirs(SAVE_DIR, exist_ok=True)

st.title("Voice Recorder")

audio = st.audio_input("Press microphone to record")

# Store audio bytes in session state when a new recording is present
if audio is not None:
    st.session_state["current_audio_bytes"] = audio.getvalue()

# Show save controls if audio is stored
if "current_audio_bytes" in st.session_state:
    st.audio(st.session_state["current_audio_bytes"])
    
    if st.button("Save Recording"):
        filename = f"sample_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        filepath = os.path.join(SAVE_DIR, filename)
        
        with open(filepath, "wb") as f:
            f.write(st.session_state["current_audio_bytes"])
            
        st.success(f"✅ Saved {filename}")
        
        # Clear state so it's ready for next clip
        del st.session_state["current_audio_bytes"]
