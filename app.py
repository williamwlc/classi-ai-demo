import streamlit as st
import datetime

st.title("Voice Recorder")
st.write("Record and download the file to your phone.")

audio = st.audio_input("Press the microphone to start recording")

if audio is not None:
    st.audio(audio, format="audio/wav")
    if st.button("Download Recording"):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sample_{timestamp}.wav"
        st.download_button(
            label="Download the recording",
            data=audio,
            file_name=filename,
            mime="audio/wav"
        )
        st.success(f"✅ File ready to download: {filename}")
