import pickle
import streamlit as st
from streamlit_option_menu import option_menu
lung_model= pickle.load(open('lung_model.sav', 'rb'))
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Lung Cancer Prediction'],
                          icons=['apple'],
                          default_index=0)
if(selected == "Lung Cancer Prediction"):
    
    #page title
    st.title("Lung Cancer Prediction using Machine Learning")



# getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        GENDER = st.number_input("GENDER")
        
    with col2:
        AGE = st.number_input("AGE")
    
    with col3:
        SMOKING = st.number_input("SMOKING")
    
    with col4:
        YELLOW_FINGERS = st.number_input("YELLOW_FINGERS")
    
    with col1:
        ANXIETY = st.number_input("ANXIETY")
    
    with col2:
        PEER_PRESSURE = st.number_input("PEER_PRESSURE")
    
    with col3:
        CHRONIC_DISEASE = st.number_input("CHRONIC DISEASE")
    
    with col4:
        FATIGUE = st.number_input("FATIGUE")
    
    with col1:
        ALLERGY = st.number_input("ALLERGY")
    
    with col2:
        WHEEZING = st.number_input("WHEEZING")
    
    with col3:
        ALCOHOL_CONSUMING = st.number_input("ALCOHOL CONSUMING")
    
    with col4:
        COUGHING = st.number_input("COUGHING")
    
    with col1:
        SHORTNESS_OF_BREATH = st.number_input("SHORTNESS OF BREATH")
    
    with col2:
        SWALLOWING_DIFFICULTY = st.number_input("SWALLOWING DIFFICULTY")
    
    with col3:
        CHEST_PAIN = st.number_input("CHEST PAIN")
    


# code for Prediction
    lung_cancer_result = " "
    
    # creating a button for Prediction
    
    if st.button("Lung Cancer Test Result"):
        lung_cancer_report = lung_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        
        if (lung_cancer_report[0] == 1):
          lung_cancer_result = "Sorry! You have Lung Cancer."
        else:
          lung_cancer_result = "Hurrah! You have no Lung Cancer."
        
    st.success(lung_cancer_result)
    