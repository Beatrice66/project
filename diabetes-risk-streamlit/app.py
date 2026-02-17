
import streamlit as st
import pickle
import os

st.title("Diabetes Risk Prediction App")

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model.pkl")

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}. Please upload model.pkl")
    st.stop()

st.header("Enter patient details:")
age = st.number_input("Age", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)

if st.button("Predict Diabetes Risk"):
    input_data = [[age, bmi, glucose, blood_pressure]]
    prediction = model.predict(input_data)
    risk = "High Risk" if prediction[0] == 1 else "Low Risk"
    st.success(f"The predicted diabetes risk is: {risk}")
