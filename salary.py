import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Employee Salary Predictor",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS
# Custom CSS (Glassmorphism theme)
st.markdown("""
<style>
/* 🔳 Background + font settings */
html, body, .main, .block-container {
    background-color: #0b0f14 !important;
    color: #f1f5f9 !important;
    font-family: 'Segoe UI', sans-serif;
}

/* 💼 Header */
.header {
    font-size: 36px;
    font-weight: 800;
    text-align: center;
    color: #60a5fa;
    margin: 20px 0 10px;
}

/* ℹ️ Info Box + Form Panel */
.info-box, section[data-testid="stForm"] {
    background-color: #111827;
    border: 2px solid #000000;
    border-radius: 12px;
    padding: 20px;
    margin-top: 20px;
}

/* 📝 Subheader Text */
.subheader {
    font-size: 20px;
    color: #cbd5e1;
    font-weight: 600;
    margin-top: 30px;
    margin-bottom: 12px;
}

/* 🔢 Number Input Box */
.stNumberInput input {
    background-color: #1f2937 !important;
    color: #f1f5f9 !important;
    border: 2px solid #000000 !important;
    border-radius: 8px !important;
    padding: 10px !important;
}

/* 🔽 Dropdown (SelectBox) */
.stSelectbox div[data-baseweb="select"] {
    background-color: #1f2937 !important;
    border: 2px solid #000000 !important;
    border-radius: 8px !important;
    color: #f1f5f9 !important;
}
.stSelectbox div[data-baseweb="select"] * {
    color: #f1f5f9 !important;
    background-color: #1f2937 !important;
}

/* 📋 Dropdown Menu Options */
[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #111827 !important;
    color: #f1f5f9 !important;
    border: 1px solid #000000 !important;
}

/* 🖱 Center Button Container */
.center-button {
    display: flex;
    justify-content: center;
    margin-top: 25px;
}

/* ✅ Predict Salary Button — blue background */
.stButton > button {
    background-color: #1e40af !important;  /* 🔵 Blue background */
    color: #ffffff !important;
    padding: 12px 28px !important;
    border: 2px solid #000000 !important;
    border-radius: 10px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background-color: #3b82f6 !important;  /* 🔵 Lighter blue on hover */
    transform: scale(1.03);
    cursor: pointer;
}

/* 💰 Prediction Box */
.prediction-box {
    background-color: #1e40af !important;
    color: #ffffff !important;
    padding: 26px;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    border-radius: 16px;
    border: 2px solid #000000;
    margin-top: 35px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.6);
}
.prediction-box h6 {
    font-size: 13px;
    font-weight: 400;
    color:#f1f5f9;
    margin-top: 10px;
    line-height: 1.5;
}

/* 🏷 Label text like Age, Gender, etc. */
label, .stRadio > label, .stSelectbox label, .stNumberInput label, .stTextInput label {
    color: #ffffff !important;
    font-weight: 600;
}

/* 🖼 Image Caption */
img + div {
    color: #94a3b8;
    text-align: center;
    font-size: 14px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)


# Load model
model_data = joblib.load("salary_predictor.pkl")
model = model_data["model"]
label_encoders = model_data["label_encoders"]
scaler = model_data["scaler"]
feature_names = model_data["feature_names"]

# Load supporting assets
eval_plot = Image.open("plot.png")

# Header
st.markdown('<div class="header">💼 Employee Salary Predictor</div>', unsafe_allow_html=True)

# Info box
st.markdown(f"""
<div class="info-box">
    <b>📘 Algorithm Used:</b> XGBoost Regressor <br>
    <b>📈 Model R² Score:</b> 94.58% <br>
    <b>📊 Evaluation:</b> Compares predicted vs actual salaries.
</div>
""", unsafe_allow_html=True)

# Form title
st.markdown('<div class="subheader">📝 Enter Employee Details</div>', unsafe_allow_html=True)

# Input form
with st.form("salary_form"):
    age = st.number_input("Age", min_value=18, max_value=80, value=30)
    gender = st.selectbox("Gender", options=label_encoders["Gender"].classes_)
    education_level = st.selectbox("Education Level", options=label_encoders["Education Level"].classes_)
    job_title = st.selectbox("Job Title", options=label_encoders["Job Title"].classes_)
    years_of_experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=5)

    # Centered button
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    submit_button = st.form_submit_button("Predict Salary")
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction output
if submit_button:
    input_df = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Education Level": [education_level],
        "Job Title": [job_title],
        "Years of Experience": [years_of_experience]
    })

    for col in ["Gender", "Education Level", "Job Title"]:
        input_df[col] = label_encoders[col].transform(input_df[col])

    input_scaled = scaler.transform(input_df)
    predicted_salary = model.predict(input_scaled)[0]

    st.markdown(f"""
    <div class="prediction-box">
        💰 <b>Estimated Annual Salary:</b><br>
        USD ${predicted_salary:,.2f}<br>
        <h6>📌 This prediction is based on your provided inputs and the model's training data.<br>
        📈 Accuracy may vary depending on job type and experience levels. </h6>
    </div>
    """, unsafe_allow_html=True)

# Evaluation section
st.markdown('<div class="subheader">📉 Model Evaluation</div>', unsafe_allow_html=True)
st.image(eval_plot, caption="Actual vs Predicted Salary", use_container_width=True)
