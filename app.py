import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Title of the web app
st.title("Diabetes Prediction System")

st.write("Enter the patient details below to predict whether the patient has diabetes or not.")

# User Inputs
preg = st.number_input("Number of Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin Level", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

# Predict Button
if st.button("Predict"):

    # Convert input into numpy array
    data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

    # Model prediction
    prediction = model.predict(data)

    # Show result
    if prediction[0] == 1:
        st.error("The patient is likely to have Diabetes.")
    else:
        st.success("The patient is unlikely to have Diabetes.")