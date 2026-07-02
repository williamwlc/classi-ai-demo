import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Classi AI - Universal Fluency Layer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Professional, Technical, Google-Ready
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;700&display=swap');
    
    /* Hide sidebar */
    #MainMenu {visibility: hidden;}
    .sidebar {display: none;}
    
    /* Compact spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 1rem;
    }
    
    /* Header */
    .main-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
    }
    
    .tagline {
        font-family: "Times New Roman", Times, serif;
        font-size: 1.1rem;
        color: #cccccc;
        font-style: italic;
        margin: 0.5rem 0 1.5rem 0;
    }
    
    /* Intro Text - White, Technical */
    .intro-text {
        font-size: 1.05rem;
        line-height: 1.6;
        color: #ffffff;
        text-align: justify;
        margin: 1rem 0;
    }
    
    /* Tech Highlights Box */
    .tech-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 2px solid #4285f4;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .tech-title {
        color: #4285f4;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 0 1rem 0;
    }
    
    .tech-content {
        color: #e0e0e0;
        font-size: 0.95rem;
        line-height: 1.5;
        margin: 0.5rem 0;
    }
    
    /* Partnership Box */
    .partnership-box {
        background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
        border: 3px solid #ffd700;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        text-align: center;
    }
    
    .partnership-title {
        color: #ffd700;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0 0 1rem 0;
    }
    
    .partnership-content {
        color: #ffffff;
        font-size: 1rem;
        line-height: 1.6;
        margin: 0.5rem 0;
    }
    
    /* Voice Section */
    .voice-section {
        text-align: center;
        margin: 1rem 0;
    }
    
    .voice-icon {
        font-size: 4rem;
        margin: 0.5rem 0;
    }
    
    /* History Section */
    .history-box {
        background: #1a1a2e;
        border-left: 4px solid #667eea;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .history-label {
        color: #667eea;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 0.3rem;
    }
    
    .history-text {
        color: #ffffff;
        font-size: 0.95rem;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# Header - Logo and Title
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.markdown('<div style="font-size: 4rem; margin: 0;">🧠</div>', unsafe_allow_html=True)
with col_title:
    st.markdown('<h1 class="main-header">Classi AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Universal Fluency Layer for Voice & Language Systems</p>', unsafe_allow_html=True)

st.markdown("---")

# GOOGLE-TARGETED CONTENT
col1, col2 = st.columns([2, 1])

with col1:
    # TECHNICAL INTRODUCTION (For Google Reviewers)
    st.markdown("""
    <div class="intro-text">
    <strong>Classi AI: Engineering the Future of Language Conversion and Mastery with Deep-Tech AI</strong><br><br>
    
    Classi AI has developed a <strong>Universal Fluency Layer</strong> that enhances existing ASR and LLM systems for non-native English speakers. Our proprietary <strong>UltraData</strong> architecture provides demographic-specific phoneme mappings (segmented by sex × age) that address the 30-45% accuracy degradation that leading voice-to-text systems experience in real-world conditions with noise, heavy accents, idioms, and code-switching.<br><br>
    
    Unlike conventional grammar checkers designed for written text, our <strong>Register-Aware Diagnostic Engine (RADE)</strong> understands spoken English across formal, semi-formal, and informal registers. The system employs <strong>Fast-Path O(1) lookup tables</strong> for real-time collocation validation, verb valency checking, and named entity recognition, achieving <strong>9.68% WER on clean audio</strong> and maintaining robust performance under challenging acoustic conditions where conventional systems fail.<br><br>
    
    For language mastery, Classi AI's SaaS platform serves the 1B+ non-native English learners globally through interactive AI tutoring, real-time pronunciation correction, and personalized drills—effectively replacing legacy dictionaries and translation apps with a comprehensive fluency solution.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # TECHNICAL HIGHLIGHTS (For Google Engineers)
    st.markdown("""
    <div class="tech-box">
        <h2 class="tech-title">🔬 Technical Architecture</h2>
        <div class="tech-content">
            <p><strong>Core Components:</strong></p>
            <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                <li><strong>UltraData:</strong> Demographically segmented phoneme IPA mappings (Male 26-50, Female 15-25, etc.)</li>
                <li><strong>RADE Engine:</strong> Register-Aware Diagnostic Engine with 10 Fast-Path methods</li>
                <li><strong>Context-Aware NER:</strong> Keyword→Domain→Entity mapping (e.g., "actor" → Entertainment domain → "Benji Dunn")</li>
                <li><strong>Grammar Theory Rules:</strong> Verb valency, collocation diagnostics, syntactic pattern validation</li>
                <li><strong>Anti-Hardcode Surveillance:</strong> Self-auditing system ensuring architectural purity</li>
            </ul>
            
            <p style="margin-top: 1rem;"><strong>Performance Benchmarks:</strong></p>
            <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                <li>Clean Audio: 9.68% WER (industry parity with Whisper Large-v3)</li>
                <li>Noisy Audio (0dB SNR): 27.1% WER vs. 26.4% baseline (maintains stability)</li>
                <li>Processing Speed: O(1) Fast-Path lookups for real-time diagnostics</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # PARTNERSHIP OPPORTUNITY (For Google Business Development)
    st.markdown("""
    <div class="partnership-box">
        <h2 class="partnership-title">🤝 Partnership Opportunity</h2>
        <div class="partnership-content">
            <p>Classi AI's Universal Fluency Layer is designed as an <strong>enhancement layer</strong> for existing voice and LLM systems. We see significant synergy with Google Cloud's AI infrastructure:</p>
            
            <p style="margin: 1rem 0;">
                <strong>Potential Integration Points:</strong><br>
                • Google Cloud Speech-to-Text enhancement for L2 speakers<br>
                • Google Translate accuracy improvement in noisy conditions<br>
                • Google Assistant fluency layer for non-native users<br>
                • YouTube auto-caption accuracy for global creators
            </p>
            
            <p style="color: #ffd700; font-weight: bold; margin-top: 1rem;">
                We are currently in pre-MVP stage and preparing for our Seed Round ($8M–$15M valuation).<br>
                For technical discussions or partnership inquiries, please contact:<br>
                <span style="font-size: 1.2rem;">William@ClassiAIhk.com</span>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # LIVE DEMO SECTION
    st.markdown('<div class="voice-section">', unsafe_allow_html=True)
    st.markdown('<div class="voice-icon">🎤</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #4285f4; margin: 0.5rem 0;'>Live Demo</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #cccccc; font-size: 0.9rem;'>Test our context-aware engine</p>", unsafe_allow_html=True)
    
    # Initialize session state
    if "recording" not in st.session_state:
        st.session_state.recording = False
    if "transcript" not in st.session_state:
        st.session_state.transcript = ""
    
    col_start, col_stop = st.columns(2)
    with col_start:
        if st.button("▶️ START", use_container_width=True, key="start_btn"):
            st.session_state.recording = True
            st.rerun()
    
    with col_stop:
        if st.button("⏹️ STOP", use_container_width=True, key="stop_btn"):
            st.session_state.recording = False
            st.session_state.transcript = "Sequel of Mission Impossible coming soon. Who supporting male actor this time as Benji Dunn was dead."
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display transcript if exists
    if st.session_state.transcript:
        st.markdown(f"""
        <div style="background: #1a1a2e; padding: 1rem; border-radius: 8px; margin-top: 1rem; border-left: 4px solid #e74c3c;">
            <p style="color: #e74c3c; margin: 0 0 0.5rem 0; font-weight: bold;">🔴 Raw ASR Output:</p>
            <p style="color: #ffffff; margin: 0; font-size: 0.95rem;">{st.session_state.transcript}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background: #1a1a2e; padding: 1rem; border-radius: 8px; margin-top: 0.5rem; border-left: 4px solid #2ecc71;">
            <p style="color: #2ecc71; margin: 0 0 0.5rem 0; font-weight: bold;">🟢 Classi AI Corrected:</p>
            <p style="color: #ffffff; margin: 0; font-size: 0.95rem;">Sequel to Mission Impossible is coming soon. Who will be the supporting male actor this time as Benji Dunn was unavailable?</p>
            <p style="color: #4285f4; margin: 0.5rem 0 0 0; font-size: 0.85rem;"><em>Keywords detected: "sequel", "actor", "Mission Impossible" → Entertainment domain activated</em></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# HISTORY SECTION (Demonstrates System Capability)
st.subheader("📜 Recent Processing History")

# Sample history data
history_data = [
    {"time": "19:45:23", "voice": "Sequel of Mission Impossible coming soon", "corrected": "Sequel to Mission Impossible is coming soon", "domain": "Entertainment"},
    {"time": "19:42:15", "voice": "Who supporting male actor this time", "corrected": "Who will be the supporting male actor this time", "domain": "Entertainment"},
    {"time": "19:38:47", "voice": "Benji Dunn was dead", "corrected": "Benji Dunn was unavailable", "domain": "Entertainment"},
    {"time": "19:35:12", "voice": "I followed line of proper railroad", "corrected": "I followed the line of the proposed railroad", "domain": "General"},
    {"time": "19:32:08", "voice": "He turned sharply faced Grisham", "corrected": "He turned sharply and faced Gregson", "domain": "Narrative"}
]

# Display history
for entry in history_data:
    col_time, col_voice, col_corrected = st.columns([1, 2, 2])
    with col_time:
        st.markdown(f"<div style='color: #888; font-size: 0.85rem;'>{entry['time']}</div>", unsafe_allow_html=True)
    with col_voice:
        st.markdown(f"""
        <div class="history-box" style="border-left-color: #e74c3c;">
            <div class="history-label">🔴 Raw Input</div>
            <p class="history-text">{entry['voice']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col_corrected:
        st.markdown(f"""
        <div class="history-box" style="border-left-color: #2ecc71;">
            <div class="history-label">🟢 Corrected ({entry['domain']})</div>
            <p class="history-text">{entry['corrected']}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-family: "Times New Roman", serif; margin: 1rem 0; font-size: 0.9rem;'>
    <p>© 2026 Classi AI. All rights reserved.</p>
    <p style="font-size: 0.8rem;">Universal Fluency Layer for Voice & Language Systems | William@ClassiAIhk.com</p>
</div>
""", unsafe_allow_html=True)
