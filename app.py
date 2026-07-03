import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Classi AI - Voice Demo", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()
if 'recording' not in st.session_state:
    st.session_state.recording = False

PUBLIC_PASSWORD = "postmvpsoon"
SPECIAL_PASSWORD = "Amd13751376Cc13751376)(*!@#"
SESSION_TIMEOUT = 1800

# Custom CSS - LOWER HEADING & TIGHT SPACING
st.markdown("""
<style>
    .stApp { background-color: #0B132B !important; }
    
    /* LOWER HEADING - ADD MORE TOP PADDING */
    .block-container { 
        padding-top: 3rem !important; 
        padding-bottom: 1rem !important; 
    }
    
    .main-header { 
        text-align: center; 
        font-size: 2.5rem !important; 
        color: #ffffff; 
        margin: 1rem 0 0.5rem 0 !important; 
        padding-top: 1rem !important;
    }
    
    .sub-header { 
        text-align: center; 
        font-size: 1.1rem !important; 
        color: #8B9DC3; 
        margin: 0.2rem 0 0.8rem 0 !important; 
    }
    
    .company-intro { 
        background-color: #1C2541 !important; 
        border: 1px solid #3A506B !important; 
        border-radius: 8px; 
        padding: 0.8rem !important;
        margin: 0.2rem 0 !important; 
    }
    
    .company-intro { border-left: 4px solid #5BC0BE !important; }
    .company-intro h2 { font-size: 1.5rem !important; color: #5BC0BE !important; margin: 0 0 0.3rem 0 !important; }
    .company-intro p { font-size: 0.95rem !important; line-height: 1.4 !important; color: #E0E1DD !important; margin: 0 0 0.3rem 0 !important; }
    
    .dev-note { 
        display: inline-block; 
        background-color: #1C2541 !important; 
        border: 1px solid #3A506B !important; 
        padding: 0.2rem 0.5rem !important; 
        border-radius: 4px !important; 
        font-size: 0.75rem !important; 
        color: #8B9DC3 !important; 
        margin: 0.2rem 0 !important; 
    }
    
    .status-box { 
        background-color: #1C2541 !important; 
        border: 1px solid #3A506B !important; 
        border-radius: 6px; 
        padding: 0.5rem !important; 
        margin: 0.2rem 0 !important; 
    }
    
    .status-box h4 { margin: 0 0 0.2rem 0 !important; font-size: 1rem !important; }
    .status-box p { color: #E0E1DD !important; font-size: 0.9rem !important; margin: 0 !important; }
    
    .stButton > button { 
        background-color: #3A506B !important; 
        color: white !important; 
        border: none !important; 
        border-radius: 4px !important; 
        font-size: 0.9rem !important; 
        padding: 0.4rem !important; 
        margin: 0.1rem !important;
    }
    
    .stTextInput > div > div > input { 
        background-color: #1C2541 !important; 
        color: white !important; 
        border: 1px solid #3A506B !important; 
    }
    
    p, h1, h2, h3, h4 { color: #ffffff !important; }
    .stMarkdown p { color: #E0E1DD !important; }
    h3.stMarkdown { margin: 0.5rem 0 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🎙️ Classi AI Voice Demo</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</p>', unsafe_allow_html=True)

pwd_col1, pwd_col2 = st.columns([1, 4])
with pwd_col1:
    password = st.text_input("", type="password", label_visibility="collapsed", key="pwd_top", placeholder="🔐 Access Password")

if password:
    if password == SPECIAL_PASSWORD:
        st.success("✅ Unlimited access granted!")
        st.session_state.session_timeout = None
    elif password == PUBLIC_PASSWORD:
        st.success("✅ Access granted! (1-hour test drive)")
    else:
        elapsed = time.time() - st.session_state.session_start
        remaining = SESSION_TIMEOUT - elapsed
        if elapsed > SESSION_TIMEOUT:
            st.error("⏰ Session expired (30 min)")
            st.stop()
        else:
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            st.info(f"⏱️ {minutes}:{seconds:02d}")

st.markdown("""
<div class="dev-note">
    📌 <strong>Dev Demo</strong> | Address Bar displays ClassiAIhk.com via Streamlit domain masking
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="company-intro">
    <h2>About Classi AI</h2>
    <p>
        Classi AI is redefining how the world bridges language barriers. While leading applications 
        merely guess at your words, we comprehend the true context of your conversation. Powered by our proprietary 
        Universal Fluency Layer, our voice-to-text engine thrives in the real world—mastering complex environments 
        where background noise, heavy accents, idioms, and code-switching cause competitor accuracy to plummet by 30%, 40%, or even more.
    </p>
    <p style="margin-bottom: 0 !important;">
        Beyond transcription, Classi's revolutionary SaaS platform is engineered to meet the needs of over 1 billion non-native learners globally. 
        By delivering interactive, corrective feedback across all four core English skills, real-time AI coaching, precision pronunciation guidance, 
        and personalized drills, our comprehensive ecosystem doesn't just compete with legacy dictionaries and translation apps—it makes them obsolete.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🎤 Voice Microphone")
st.markdown('<div class="record-buttons">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("🔴 Start Recording", use_container_width=True, key="start_rec"):
        st.session_state.recording = True
        st.rerun()
with col2:
    if st.button("⏹️ Stop Recording", use_container_width=True, key="stop_rec"):
        st.session_state.recording = False
        # PLACEHOLDER - MVP INTEGRATION NEEDED HERE
        # This will be replaced by actual engine processing
        st.session_state.history.insert(0, {
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'raw_text': "[MVP Integration Required]",
            'corrected_text': "[MVP Integration Required]",
            'duration': "0.0s"
        })
        st.session_state.history = st.session_state.history[:10]
        st.success("✅ Audio captured - MVP processing pending")
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.recording:
    st.markdown("<p style='color: #ff4b4b; text-align: center; font-weight: bold; margin: 0.2rem 0;'>🔴 RECORDING IN PROGRESS...</p>", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    display_raw = "Waiting for audio..." if not st.session_state.history else st.session_state.history[0]['raw_text']
    st.markdown(f"""
    <div class="status-box">
        <h4 style="color: #ff4b4b; margin: 0;">🔴 Raw ASR</h4>
        <p style="margin: 0; color: #aaa; font-size: 0.9rem;">{display_raw}</p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    display_corrected = "Waiting for audio..." if not st.session_state.history else st.session_state.history[0]['corrected_text']
    st.markdown(f"""
    <div class="status-box">
        <h4 style="color: #00ff88; margin: 0;">🟢 Corrected</h4>
        <p style="margin: 0; color: #aaa; font-size: 0.9rem;">{display_corrected}</p>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.history:
    st.markdown("### 📜 History of the Last 10 Text Transcripts")
    for i, item in enumerate(st.session_state.history[:10]):
        with st.expander(f"#{i+1} - {item['timestamp']} - {item.get('duration', 'N/A')}", expanded=(i==0)):
            col_x, col_y = st.columns(2)
            with col_x:
                st.markdown("**🔴 Raw ASR:**")
                st.write(item['raw_text'])
            with col_y:
                st.markdown("**🟢 Corrected:**")
                st.write(item['corrected_text'])

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #8B9DC3; font-size: 0.8rem; margin-top: 0.5rem;">
    <p>© 2026 Classi AI. All rights reserved. | Contact: <strong>William@ClassiAIhk.com</strong></p>
</div>
""", unsafe_allow_html=True)
