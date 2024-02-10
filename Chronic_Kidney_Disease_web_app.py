# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:56:24 2023

@author: vinay
"""

import numpy as np
import pickle
import streamlit as st

# Load the saved model
model_file_path = 'trained_model.sav'

try:
    with open(model_file_path, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
except FileNotFoundError:
    print(f"Model file '{model_file_path}' not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    
#loaded_model = pickle.load(open('C:/Users/vinay/OneDrive/Desktop/ML Project/ML web/trained_model.sav', 'rb'))

# Create a function for prediction
def kidney_prediction(new_data):
   input_data_as_numpy_array = np.asarray(new_data, dtype=float)  # Convert to float
   input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
   predictions = loaded_model.predict(input_data_reshaped)
   if predictions[0] == 0:
       return "No Kidney Disease"
   else:
       return "Seems like Kidney Disease. Please Contact Doctor!"

def main():
    st.title('Chronic Kidney Disease Prediction Web App')
    st.write("yes:1, No:0")

    # Get input data from the user
    col1,col2,col3=st.columns(3)
    
    with col1:
        age = st.text_input('Age',)
        st.caption("Age: 1-100")
    with col2:
        blood_pressure = st.text_input('Blood Pressure',)
        st.caption("Normal: 120/80")
    
    with col3:
        specific_gravity = st.text_input('Specific Gravity', )
        st.caption("Normal: 1.005 - 1.030")
        
    with col1:
        red_blood_cells_options = ["1", "0"]
        red_blood_cells = st.selectbox('Red Blood Cells', red_blood_cells_options)
        st.caption("Normal: 1")
        st.caption("Abnormal: 0")
        #red_blood_cells = st.text_input('Red Blood Cells (1 or 0)', value=0)
        #st.caption("Normal: 1")
        #st.caption("Abnormal: 0")
    with col2:
        pus_cells_options=["1", "0"]
        pus_cell = st.selectbox('Pus Cells',pus_cells_options)
        st.caption("Normal: 1")
        st.caption("Abnormal: 0")
    with col3:
        pus_cells_clumps_options=["1", "0"]
        pus_cell_clumps = st.selectbox('Pus Cell Clumps',pus_cells_clumps_options)
        st.caption("Present: 1")
        st.caption("Not Present: 0")
    with col1:
        bacteria_options=["1", "0"]
        bacteria = st.selectbox('Bacteria', bacteria_options)
        st.caption("Present: 1")
        st.caption("Not Present: 0")
    with col2:
        blood_glucose_random = st.text_input('Blood Glucose')
        st.caption("Normal: <140")
    with col3:
        blood_urea = st.text_input('Blood Urea')
        st.caption("Normal: 6-20 mg")
    with col1:
        serum_creatinine = st.text_input('Serum Creatinine')
        st.caption("Normal: 0.6-1.2")
    with col2:
        sodium = st.text_input('Sodium')
        st.caption("Normal: 135-145")
    with col3:
        potassium = st.text_input('Potassium')
        st.caption("Normal: 3.5-5.0")
    with col1:
        haemoglobin = st.text_input('Haemoglobin')
        st.caption("Male: 13.8-17.2")
        st.caption("Female: 12.1-15.1")
    with col2:
        hypertension_options=["1", "0"]
        hypertension = st.selectbox('Hypertension',hypertension_options)
        st.caption("Present: 1")
        st.caption("Not Present: 0")
    with col3:
        appetite_values=["1", "0"]
        appetite = st.selectbox('Appetite',appetite_values)
        st.caption("Good: 1")
        st.caption("Poor: 0")
    with col1:
        peda_edema_options=["1", "0"]
        peda_edema = st.selectbox('Peda Edema (1 or 0)', peda_edema_options)
        st.caption("Yes: 1")
        st.caption("No: 0")
    with col2:
        anemia_options=["1", "0"]
        anemia = st.selectbox('Anemia', anemia_options)
        st.caption("Yes: 1")
        st.caption("No: 0")
    diagnosis = ''

    # Create a button for prediction
    if st.button('Test Result'):
        try:
            # Convert user input to float and pass it to the prediction function
            input_data = [
                float(age), float(blood_pressure), float(specific_gravity),
                float(red_blood_cells), float(pus_cell), float(pus_cell_clumps),
                float(bacteria), float(blood_glucose_random), float(blood_urea),
                float(serum_creatinine), float(sodium), float(potassium),
                float(haemoglobin), float(hypertension), float(appetite),
                float(peda_edema), float(anemia)
            ]
            diagnosis = kidney_prediction(input_data)
        except ValueError:
            diagnosis = "Invalid input. Please enter numeric values."

    st.success(diagnosis)

if __name__ == '__main__':
    main()
