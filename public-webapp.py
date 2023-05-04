# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:37:57 2023

@author: Manju
"""
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

loaded_model = pickle.load(open("best_model.sav", "rb"))

def predictfor(input_data):
    prediction = loaded_model.predict(input_data)
    if prediction==1:
        return ("Yes, default")
    else:
        return ("No")
    
    
with st.sidebar:
    selected = option_menu("Multiple default prediction",
                           ["Loan_Prediction"], icons = ["Activity"], default_index=0)

if selected=="Loan_Prediction":
    st.title("Loan_Prediction using credit score")
    col1, col2 = st.columns(2)
    with col1:
        Credit_History = st.text_input("Credit_history")
    with col2:
         Property_Area = st.text_input("Area of the property")
