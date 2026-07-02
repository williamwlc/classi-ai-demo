import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Classi AI", page_icon="🎓", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

if not st.session_state.authenticated:
    st.title("🔐 Classi AI - VIP Access")
    password = st.text_input("Enter Password", type="password")
    if st.button("Enter"):
        if password == "postmvpsoon":
            st.session_state.authenticated = True
            st.session_state.start_time = datetime.now()
            st.rerun()
        else:
            st.error("Incorrect password")
    st.stop()

elapsed = datetime.now() - st.session_state.start_time
if elapsed > timedelta(hours=1):
    st.session_state.authenticated = False
    st.rerun()

st.title("Classi AI")
st.markdown("*Engineering the Future of Language Conversion and Mastery with Deep-Tech AI*")
st.write("---")

st.write("Classi AI is redefining how the world bridges language barriers. While leading applications merely guess at your words, we comprehend the true context of your conversation. Powered by our proprietary Universal Fluency Layer, our voice-to-text engine thrives in the real world—mastering complex environments where background noise, heavy accents, idioms, and code-switching cause competitor accuracy to plummet by 30%, 40%, or even more.")

st.write("Beyond transcription, Classi’s revolutionary SaaS platform is engineered to meet the needs of over 1 billion non-native learners globally. By delivering interactive, corrective feedback across all four core English skills, real-time AI coaching, precision pronunciation guidance, and personalized drills, our comprehensive ecosystem doesn't just compete with legacy dictionaries and translation apps—it makes them obsolete.")

st.markdown("---")
st.subheader("🎬 VIP Invitation")
st.write("I am pleased to offer you a VIP invitation to try out my voice-to-text conversion app. Similar to how you speak to chatbots, you are welcome to speak in English and look at the text of your voice instantly. This test drive experience will end one hour after you start using it.")
st.write("Contact: **William@ClassiAIhk.com**")

st.markdown("---")
remaining = timedelta(hours=1) - elapsed
st.info(f"⏱️ Time Remaining: {int(remaining.total_seconds() // 60)}m {int(remaining.total_seconds() % 60)}s")

