import streamlit as st
import streamlit.components.v1 as components
import time

# ============================================================================
# PASSWORD PROTECTION
# ============================================================================
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.set_page_config(page_title="Classi AI - Login", layout="centered")
    st.title("🔒 Classi AI - Confidential Demo")
    password = st.text_input("Enter access code:", type="password", key="password_input")
    if st.button("Login"):
        if password == "classi2026invest":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Invalid access code")
    st.stop()

# ============================================================================
# MAIN APP
# ============================================================================
st.set_page_config(page_title="Classi AI", layout="wide", initial_sidebar_state="collapsed")

# Initialize history
if 'history' not in st.session_state:
    st.session_state.history = []

# Custom CSS
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stSidebar {display: none !important;}
    .stApp { background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%); color: white; }
    
    .header-container { display: flex; align-items: center; margin-bottom: 30px; }
    .logo-circle { width: 40px; height: 40px; background: linear-gradient(135deg, #00ffff 0%, #0099ff 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 0 15px rgba(0, 255, 255, 0.4); }
    .logo-text { color: white; font-size: 20px; font-weight: bold; }
    .company-name { font-size: 24px; font-weight: 800; color: #ffffff; letter-spacing: 1px; }
    
    .mi-box { background: rgba(20, 20, 30, 0.8); border: 2px solid #00ffff; border-radius: 12px; padding: 20px; max-width: 600px; margin: 0 auto 30px auto; text-align: center; box-shadow: 0 0 20px rgba(0, 255, 255, 0.2); }
    .mi-text { color: #e0e0e0; font-size: 1rem; line-height: 1.5; font-style: italic; }
    .countdown { color: #ff4444; font-weight: bold; font-size: 1.1rem; margin-top: 10px; }
    
    .mic-container { text-align: center; margin: 40px 0; }
    .mic-button { width: 120px; height: 120px; background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 0 30px rgba(155, 89, 182, 0.6); border: 4px solid #ffffff; transition: transform 0.2s; }
    .mic-button:hover { transform: scale(1.05); }
    .mic-icon { font-size: 60px; color: white; }
    
    .output-box { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 20px; margin: 10px 0; min-height: 100px; }
    .output-title { color: #00ffff; font-weight: bold; margin-bottom: 10px; }
    
    .history-item { background: rgba(255, 255, 255, 0.03); border-left: 3px solid #9b59b6; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .history-time { color: #888; font-size: 0.8rem; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

# 1. Header (Top Left)
st.markdown("""
<div class="header-container">
    <div class="logo-circle"><div class="logo-text">C</div></div>
    <div class="company-name">Classi AI</div>
</div>
""", unsafe_allow_html=True)

# 2. Mission Impossible Box (Center)
st.markdown("""
<div class="mi-box">
    <div class="mi-text">
        "If you choose to accept this VIP invitation to experience Classi's state-of-the-art 
        voice-to-text journey, you are free to speak in English using the Voice message icon below. 
        Your spoken words will be transcribed and displayed instantly."
    </div>
    <div class="countdown">
        ⚠️ This website will disintegrate in <span id="countdown">10</span> seconds...
    </div>
</div>
""", unsafe_allow_html=True)

# Countdown Timer
components.html("""
<script>
let seconds = 10;
const countdown = document.getElementById('countdown');
const interval = setInterval(() => {
    seconds--;
    if (countdown) countdown.textContent = seconds;
    if (seconds <= 0) {
        clearInterval(interval);
        document.querySelector('.mi-box').innerHTML = '<div style="color: #00ff00; font-size: 1.1rem; font-weight: bold;">✓ Access Granted. Welcome to the future of voice intelligence.</div>';
    }
}, 1000);
</script>
""", height=60)

# 3. Voice Message Icon (Purple Mic)
st.markdown("""
<div class="mic-container">
    <div class="mic-button" onclick="alert('Voice recording feature coming soon!')">
        <div class="mic-icon">🎙️</div>
    </div>
    <p style="color: #9b59b6; font-weight: bold; margin-top: 15px;">Voice Message Icon</p>
</div>
""", unsafe_allow_html=True)

# 4. Output Layout (Raw vs Corrected)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="output-box"><div class="output-title">🔴 Raw ASR (Stage 3)</div><p style="color: #aaa;">Waiting for voice input...</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="output-box"><div class="output-title">🟢 Corrected Output (Stage 5)</div><p style="color: #aaa;">Waiting for voice input...</p></div>', unsafe_allow_html=True)

# 5. Conversation History (Bottom)
st.markdown("---")
st.markdown("### 📜 Conversation History")

# Add a dummy history item for demo purposes
if len(st.session_state.history) == 0:
    st.session_state.history.append({
        'time': 'Just now',
        'raw': 'Hello, this is a test of the voice system.',
        'fixed': 'Hello, this is a test of the voice system.'
    })

for item in reversed(st.session_state.history):
    st.markdown(f"""
    <div class="history-item">
        <div class="history-time"> {item['time']}</div>
        <div style="color: #ff6b6b; font-size: 0.9rem;"><strong>Raw:</strong> {item['raw']}</div>
        <div style="color: #51cf66; font-size: 0.9rem; margin-top: 5px;"><strong>Corrected:</strong> {item['fixed']}</div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #555; font-size: 0.8rem;'>© 2026 Classi AI. Confidential & Proprietary.</div>", unsafe_allow_html=True)
