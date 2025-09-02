#Import Library
import streamlit as st
import pandas as pd
import numpy as np
import joblib as jl


# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="📈 Youtube Analytics Tendency")


# ============= RESOURCE ==================

## ============= MODEL============
model = jl.load("models & Dataset\model.pkl")

## ========= CATEGORIESLABEL ===========
CategoriesLabel = ['Nonprofits & Activism', 'People & Blogs', 'Entertainment',
       'News & Politics', 'Science & Technology', 'Education', 'Music',
       'Travel & Events', 'Film & Animation', 'Sports', 'Gaming',
       'Comedy', 'Howto & Style']
#=========================================

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
        text-align: center;
    }

    label, .stTextInput label, .stNumberInput label, .stTextArea label {
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



# =========== หัวข้อ input ===========
# Title
videoTitle = st.text_input("🎬 Video Title 🎬")

# Description
videoDescription = st.text_area("🖊️ Description 🖊️")

# Category
videoCategoryLabel = st.selectbox(
    "📂 Category 📂",
    CategoriesLabel
)

# Duration (Seconds)
durationSec = st.number_input("⏱️ Duration (seconds) ⏱️", min_value=1, step=1)
# ===================================

# ===========ปุ่ม===========
button = st.button("Predict")

if button :
    # Convert to Dataframe
    # Feature : "videoTitle", "videoDescription", "videoCategoryLabel", "durationSec" 
    data = {
        "videoTitle": [videoTitle],
        "videoDescription": [videoDescription],
        "videoCategoryLabel": [videoCategoryLabel],
        "durationSec": [durationSec]
    }
    data = pd.DataFrame(data)

    #Predict
    predict_answer = model.predict(data)

    # Display Predict
    if predict_answer == 1 :
        st.success("Your video is trend 🔥")
    else :
        st.warning("Your video is not trend 😥")
# ========================

# =============== Dataset =====================
train_df = pd.read_excel('models & Dataset\Dataset.xlsx')
# Toggle switch
show_data = st.toggle("Show dataset")

# Condition
if show_data:
    set_index = st.checkbox("Set Index ?", value=False)

    if set_index :
        set_index_columns = st.selectbox(
        "How would you like to set index?",
        train_df.columns
        )
        # Multiselect for columns
        columns = st.multiselect(
                    "Select columns to display:",
                    options=train_df.columns.tolist(),
                    default=train_df.columns.tolist()[:4]  # default shows all columns
                )
        if columns  :
            st.dataframe(train_df[columns], use_container_width=True)
        else:
            st.warning("⚠ Please select at least one column!")
        
    else :
        st.dataframe(train_df, use_container_width=True)
# =============================================

