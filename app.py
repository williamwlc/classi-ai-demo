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
if 'recording_start_time' not in st.session_state:
    st.session_state.recording_start_time = None

PUBLIC_PASSWORD = "postmvpsoon"
SPECIAL_PASSWORD = "Amd13751376Cc13751376)(*!@#"
SESSION_TIMEOUT = 1800

# Custom CSS - REMOVE LINK SYMBOL & FIX SPACING
st.markdown("""
<style>
    .stApp { background-color: #0B132B !important; }
    
    /* HIDE ANCHOR/LINK SYMBOLS */
    a.header-anchor { display: none !important; }
    .stMarkdown h2::before { content: none !important; }
    
    .block-container { 
        padding-top: 2rem !important; 
        padding-bottom: 1rem !important; 
    }
    
    .main-header { 
        text-align: center; 
        font-size: 2.5rem !important; 
        color: #ffffff; 
        margin: 0.5rem 0 0.3rem 0 !important; 
    }
    
    .sub-header { 
        text-align: center; 
        font-size: 1.1rem !important; 
        color: #8B9DC3; 
        margin: 0 0 0.5rem 0 !important; 
    }
    
    /* TIGHT SPACING FOR ABOUT SECTION */
    .about-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .about-heading {
        font-size: 1.5rem !important;
        color: #5BC0BE !important;
        margin: 0 0 0.3rem 0 !important;
        font-weight: bold;
    }
    
    .company-intro { 
        background-color: #1C2541 !important; 
        border: 1px solid #3A506B !important; 
        border-left: 4px solid #5BC0BE !important;
        border-radius: 8px; 
        padding: 0.8rem !important;
        margin: 0 !important; 
    }
    
    .company-intro p { 
        font-size: 0.95rem !important; 
        line-height: 1.4 !important; 
        color: #E0E1DD !important; 
        margin: 0.3rem 0 !important; 
    }
    
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
        margin: 0.3rem 0 !important; 
    }
    
    .status-box h4 { margin: 0 0 0.3rem 0 !important; font-size: 1rem !important; }
    .status-box p { color: #E0E1DD !important; font-size: 0.9rem !important; margin: 0 !important; }
    
    .stButton > button { 
        background-color: #3A506B !important; 
        color: white !important; 
        border: none !important; 
        border-radius: 4px !important; 
        font-size: 0.9rem !important; 
        padding: 0.5rem !important; 
        margin: 0.2rem !important;
    }
    
    .stTextInput > div > div > input { 
        background-color: #1C2541 !important; 
        color: white !important; 
        border: 1px solid #3A506B !important; 
    }
    
    p, h1, h2, h3, h4 { color: #ffffff !important; }
    .stMarkdown p { color: #E0E1DD !important; }
    h3.stMarkdown { margin: 0.5rem 0 0.3rem 0 !important; }
    
    .recording-indicator {
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
        margin: 0.3rem 0;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
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

# ABOUT SECTION - COMPACT LAYOUT
st.markdown("""
<div class="about-container">
    <h2 class="about-heading">About Classi AI</h2>
    <div class="company-intro">
        <p style="margin-top: 0 !important;">
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
</div>
""", unsafe_allow_html=True)

# VOICE MICROPHONE SECTION
st.markdown("### 🎤 Voice Microphone")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔴 Start Recording", use_container_width=True, key="start_rec"):
        st.session_state.recording = True
        st.session_state.recording_start_time = time.time()
        st.rerun()

with col2:
    if st.button("⏹️ Stop Recording", use_container_width=True, key="stop_rec"):
        if st.session_state.recording and st.session_state.recording_start_time:
            # Calculate duration
            duration = time.time() - st.session_state.recording_start_time
            duration_str = f"{duration:.1f}s"
            
            # Reset recording state
            st.session_state.recording = False
            
            # ADD TO HISTORY WITH ACTUAL DURATION
            st.session_state.history.insert(0, {
                'timestamp': datetime.now().strftime("%H:%M:%S"),
                'raw_text': "Audio captured - MVP integration pending",
                'corrected_text': "Awaiting MVP engine processing",
                'duration': duration_str
            })
            st.session_state.history = st.session_state.history[:10]
            st.session_state.recording_start_time = None
            st.success(f"✅ Recording stopped - Duration: {duration_str}")
            st.rerun()

if st.session_state.recording:
    st.markdown("<p class='recording-indicator'>🔴 RECORDING IN PROGRESS... Click STOP when finished</p>", unsafe_allow_html=True)

# DISPLAY CURRENT RESULTS
col_a, col_b = st.columns(2)
with col_a:
    if st.session_state.history:
        raw_text = st.session_state.history[0]['raw_text']
    else:
        raw_text = "No recording yet"
    st.markdown(f"""
    <div class="status-box">
        <h4 style="color: #ff4b4b; margin: 0;">🔴 Raw ASR</h4>
        <p style="margin: 0; color: #aaa; font-size: 0.9rem;">{raw_text}</p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    if st.session_state.history:
        corrected_text = st.session_state.history[0]['corrected_text']
    else:
        corrected_text = "No recording yet"
    st.markdown(f"""
    <div class="status-box">
        <h4 style="color: #00ff88; margin: 0;">🟢 Corrected</h4>
        <p style="margin: 0; color: #aaa; font-size: 0.9rem;">{corrected_text}</p>
    </div>
    """, unsafe_allow_html=True)

# HISTORY SECTION
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
