import streamlit as st
import datetime
import os

# For Android: save to external storage (common for voice apps)
SAVE_DIR = "/storage/emulated/0/voice_clips"  # Android
# For iPhone: use the Documents folder
# SAVE_DIR = "/private/var/mobile/Containers/Data/Application/.../Documents"

os.makedirs(SAVE_DIR, exist_ok=True)

st.title("Voice Recorder")
st.write("Record and save directly to your phone's voice_clips folder.")

audio = st.audio_input("Press the microphone to start recording")

if audio is not None:
    st.audio(audio, format="audio/wav")
    if st.button("Save Recording"):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sample_{timestamp}.wav"
        filepath = os.path.join(SAVE_DIR, filename)
        
        with open(filepath, "wb") as f:
            f.write(audio.getvalue())
        
        st.success(f"✅ Saved to: {filepath}")
