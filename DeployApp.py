 

import pickle
import streamlit as st
import numpy as np

 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache(allow_output_mutation=True)

# defining the function which will make the prediction using the data which the user inputs 
def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    
    # preprocess user input
    if sex == 'Male':
        sex = 0
    else:
        sex = 1
        
    # making predictions of all the grouphs in the file
    predictions = classifier.predict(
        [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if (predictions[0] == 0):
        disease = "Nondefective heart"
    else:
        disease = "Defective Heart"
    return disease 
# main function defines our webpage
def main():
     # front end elements of the web page 
    html_temp ="""
    <div style ="background-color:red;background-image: linear-gradient(45deg, #f3ec78, #af4261);background-size: 100%;  background-repeat: repeat;;
    -webkit-background-clip: text;-webkit-text-fill-color: transparent; -moz-background-clip: text;
    -moz-text-fill-color: transparent;"> 
    <h1 style ="text-align: center;font-family: "Archivo Black", sans-serif;font-weight: normal;font-size: 6em; ">Heart Disease Deployment</h1> 
    </div> """
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    # allow user input 
    sex = st.selectbox('Sex',('Male','Female'))
    age  = st.slider('Age',min_value=1, max_value=100, value=10, step=1)
    cp  = st.slider('Constrictive pericarditis (CP): ',min_value=0, max_value=3, value=0, step=1)
    trestbps  = st.slider('Resting blood pressure (trestbps)',min_value=100, max_value=200, value=1, step=1)
    chol = st.slider('Cholesterol (chol)',min_value=100, max_value=400, value=1, step=1)
    fbs = st.slider('fasting blood sugar (fbs)',min_value=0, max_value=2, value=0, step=1)
    restecg = st.slider('Resting electrocardiographic Results:(0 = normal; 1 = having ST-T; 2 = hypertrophy) (restecg)',min_value=0, max_value=2, value=0, step=1)
    thalach  = st.slider('Maximum Heart Rate achieved (thalach)',min_value=50, max_value=200, value=0,step=1)
    exang  = st.slider('Exercise induced angina (exang)',min_value=0, max_value=2, value=0, step=1)
    oldpeak  = st.slider('Exercise relative to rest (oldpeak)',min_value=0.0, max_value=4.0, value=0.0, step=0.1)
    slope  = st.slider('ST/heart rate (Slope)',min_value=0, max_value=3, value=0, step=1)
    ca  = st.slider('Coronary calcium (CA)',min_value=0, max_value=5, value=0, step=1)
    thal  = st.slider('Thalassemia (thal)',min_value=0, max_value=4, value=0, step=1)

    # Make the prediction and store it when clicked
    if st.button("Predict"):
        result = prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        st.success(f'Health Status is {result}')
if __name__=='__main__': 
    main()
