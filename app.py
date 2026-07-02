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

st.write("**Classi AI** is redefining how the world conducts language conversion. Unlike leading apps that merely estimate what you are saying, we understand the actual context of your conversation. Our Universal Fluency Layer enhances voice-to-text systems in realistic situations where voice input contaminated with noise, accents, idioms, and code-switching causes leading language conversion apps to suffer from a deep slump in conversion accuracy by as much as 30 to 45%.")

st.write("For language mastery, Classi's revolutionary SaaS language learning platform fulfills the genuine needs of 1B+ non-native learners globally. By offering interactive learning with corrective feedback across all four English skills, real-time coaching with an interactive AI tutor, pronunciation correction and guidance, and personalized drills, our comprehensive language mastery platform effectively dethrones legacy dictionaries and translation apps.")

st.markdown("---")
st.subheader("🎬 VIP Invitation")
st.write("I am pleased to offer you a VIP invitation to try out my voice-to-text conversion app. Similar to how you speak to chatbots, you are welcome to speak in English and look at the text of your voice instantly. This test drive experience will end one hour after you start using it.")
st.write("Contact: **William@ClassiAIhk.com**")

st.markdown("---")
remaining = timedelta(hours=1) - elapsed
st.info(f"⏱️ Time Remaining: {int(remaining.total_seconds() // 60)}m {int(remaining.total_seconds() % 60)}s")
