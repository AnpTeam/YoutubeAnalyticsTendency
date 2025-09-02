#Import Library
import streamlit as st
import pandas as pd
import numpy as np
import joblib as jl


# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="📈 Youtube Analytics Tendency")

# ============================
# CSS สำหรับ Card
st.markdown("""
    <style>
    .card {
        background-color: #cc0000;
        padding: 5px;
        border-radius: 30px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        margin-bottom: 20px;
        color: white;
        text-align: center;
    }

    label, .stTextInput label, .stNumberInput label, .stTextArea label {
        color: #ffffff !important; 
        text-align: left; 
        display: block; 
    }
    </style>
""", unsafe_allow_html=True)
# ============================

#============ TITLE =========
st.markdown('</div>', unsafe_allow_html=True)
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg",
    use_container_width=True
)
st.markdown('<div class="card"><h3>📊 Analytics Tendency', unsafe_allow_html=True)
st.title("📝 Enter video details to predict popularity")
# ============================

CategoriesLabel = ['Nonprofits & Activism', 'People & Blogs', 'Entertainment',
       'News & Politics', 'Science & Technology', 'Education', 'Music',
       'Travel & Events', 'Film & Animation', 'Sports', 'Gaming',
       'Comedy', 'Howto & Style']


# =========== หัวข้อ input ===========
videoTitle = st.text_input("🎬 Video Title 🎬")
videoDescription = st.text_area("🖊️ Description 🖊️")
videoCategoryLabel = st.selectbox(
    "📂 Category 📂",
    CategoriesLabel
)
durationSec = st.number_input("⏱️ Duration (seconds) ⏱️", min_value=1, step=1)
# ===================================

# ===========ปุ่ม===========
button = st.button("Predict")
# ========================