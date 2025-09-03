#Import Library
from sklearn.metrics import r2_score
import streamlit as st
import pandas as pd
import numpy as np
import joblib as jl
from sklearn.metrics import accuracy_score


# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="📈 Youtube Analytics Tendency")


# ============= RESOURCE ==================

## ============= MODEL============
model = jl.load("modelsAndDataset\model.pkl")

## ========= CATEGORIESLABEL ===========
CategoriesLabel = ['People & Blogs', 'Entertainment', 'Science & Technology',
       'Howto & Style', 'Education', 'Pets & Animals', 'Gaming', 'Sports',
       'News & Politics', 'Music', 'Film & Animation']

## ============== DATASET ================
train_df = pd.read_excel('modelsAndDataset\Dataset.xlsx')
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
        color : white;
    }

    label, .stTextInput label, .stNumberInput label, .stTextArea label {
        text-align: left; 
        display: block; 
    }
            
    .stExpander{
        background-color : #cc0000 ;
        color : white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        border-radius: 12px;
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





isUploadFile = st.toggle("Upload File ?" )

if isUploadFile:
    #Example Data
    with st.expander("Example of Dataset"):
        example_df = pd.read_excel('modelsAndDataset\Example.xlsx')
        st.dataframe(example_df)

    # Upload file
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt"])
else :
    uploaded_file = None
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
    if uploaded_file is not None:
        st.write("✅ File uploaded:", uploaded_file.name)

        # If CSV
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        # If Excel
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        df['Predict'] = model.predict(df)

        st.dataframe(df)

    else :
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
# ====================================

# =============== Dataset =====================
# Toggle switch
show_data = st.toggle("Show training dataset")

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

