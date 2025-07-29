import streamlit as st
import pickle  # or joblib
import numpy as np

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("My ML Model App")

# User input
input_value = st.number_input("Enter a value:")

# Prediction
if st.button("Predict"):
    prediction = model.predict(np.array([[input_value]]))
    st.write("Prediction:", prediction[0])