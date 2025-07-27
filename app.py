# app.py
import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("cancer_model.pkl")
diagnosis_labels = {0: "Healthy", 1: "Leukemia", 2: "Lymphoma"}

st.set_page_config(page_title="Cancer Prediction", layout="centered")
st.title("🧬 Blood Test Cancer Predictor")
st.markdown("Predicts possible cancer type based on simulated blood test values.\n\n"
            "⚠️ *This is not a diagnostic tool. For educational purposes only.*")

# Sliders for inputs
WBC = st.slider("White Blood Cells (x10^9/L)", 2.0, 15.0, 7.0, 0.1)
RBC = st.slider("Red Blood Cells (x10^12/L)", 3.5, 6.5, 5.0, 0.1)
Hemoglobin = st.slider("Hemoglobin (g/dL)", 8.0, 18.0, 14.0, 0.1)
Platelets = st.slider("Platelets (x10^9/L)", 100.0, 500.0, 250.0, 1.0)
MCV = st.slider("MCV (fL)", 75.0, 105.0, 90.0, 0.5)
Lymphocytes = st.slider("Lymphocytes (%)", 10.0, 50.0, 30.0, 0.5)
Neutrophils = st.slider("Neutrophils (%)", 30.0, 80.0, 60.0, 0.5)

# Prediction
sample = np.array([[WBC, RBC, Hemoglobin, Platelets, MCV, Lymphocytes, Neutrophils]])
if st.button("🔍 Predict"):
    pred = model.predict(sample)[0]
    prob = model.predict_proba(sample).max()
    st.success(f"**Prediction: {diagnosis_labels[pred]}**")
    st.info(f"Confidence: {prob:.2%}")

st.markdown("---")
st.caption("Built with ❤️ using synthetic data and Streamlit.")