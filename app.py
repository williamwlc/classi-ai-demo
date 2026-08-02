import streamlit as st
import datetime
import os

# ========== YOUR RECORDING FOLDER ==========
SAVE_DIR = r"D:\ufl_test_data\Will_Real_Data\tv_medhigh"
os.makedirs(SAVE_DIR, exist_ok=True)

st.title("Voice Recorder")
st.write("Record your voice and save as WAV.")

audio = st.audio_input("Press the microphone to start recording")

if audio is not None:
    st.audio(audio, format="audio/wav")
    
    if st.button("Save Recording"):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sample_{timestamp}.wav"
        filepath = os.path.join(SAVE_DIR, filename)
        
        # Avoid overwriting existing files
        counter = 1
        while os.path.exists(filepath):
            filename = f"sample_{timestamp}_{counter}.wav"
            filepath = os.path.join(SAVE_DIR, filename)
            counter += 1
        
        # Save the file
        with open(filepath, "wb") as f:
            f.write(audio.getvalue())
        
        st.success(f"✅ Saved as {filename}")
        
        # Clear audio state to prevent duplicate background saves
        st.session_state.audio_input = None
        
        # Force page refresh to show updated file list
        st.rerun()

st.write("---")
st.write("Recorded files are saved to:")
st.code(SAVE_DIR)
