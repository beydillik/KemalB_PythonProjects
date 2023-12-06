import streamlit as st
import sklearn
import numpy as np
import pandas as pd
import joblib

def predict_rf(df):
    rf = joblib.load('RandForest_model.sav')
    return rf.predict(df)
def predict_dt(df):
    dt = joblib.load('DecisionTree_model.sav')
    return dt.predict(df)
def predict_svm(df):
    svm = joblib.load('SVM_model.sav')
    return svm.predict(df)

st.set_page_config(layout="wide")

st.image("images/mubea1.jpg")

st.title("Electricity Consumption Forecast with Machine Learning")
content1 = """
Please fill the necessary information into input cells below in order to get electricity consumption forecast.
Machine Learning Algorithms will calculate expected consumption using historical information with regression analysis.
"""

st.info(content1)

col1, empty_col, col2 = st.columns([3.5, 0.5, 0.5])

production_pieces = st.number_input('Please write number of pieces to be produced:', format= '%i', value=10000, step=100)
average_weight = st.slider('Please write expected average weight of spring:', min_value=1.0, max_value=12.0, value=2.1, step=0.1)
cycle_time = st.slider('Please write expected cycle_time_(Pcs/min):', min_value=10.0, max_value=20.0, value=18.0, step=0.1)
stoppage_rate = st.slider('Please write expected stoppage rate percentage :', min_value=0, max_value=100, value=25, step=1)
scrap_rate = st.slider('Please write expected scrap rate percentage:', min_value=0.00, max_value=20.0, value=0.2, step=0.01)
algorithm = st.radio(
    "Select algorithm to  run",
    ["Random Forest Regressor (recommended)", "Decision Tree Regressor", "Support Vector Machine (SVM)"],
    captions = ["", "", ""])
st.write("Selected Algorithm: "+ algorithm)

if st.button('Estimate Electricity Consumption'):
    if algorithm == "Random Forest Regressor (recommended)":
        electricity_consumption = predict_rf(np.array([[production_pieces,average_weight, cycle_time, stoppage_rate, scrap_rate]]))
        st.write("Consumption Estimate is: " , ("%.2f" % electricity_consumption[0]) , "kwh")
    elif algorithm == "Decision Tree Regressor":
        electricity_consumption = predict_dt(np.array([[production_pieces,average_weight, cycle_time, stoppage_rate, scrap_rate]]))
        st.write("Consumption Estimate is: " , ("%.2f" % electricity_consumption[0]) , "kwh")
    elif algorithm == "Support Vector Machine (SVM)":
        electricity_consumption = predict_svm(np.array([[production_pieces,average_weight, cycle_time, stoppage_rate, scrap_rate]]))
        st.write("Consumption Estimate is: " , ("%.2f" % electricity_consumption[0]) , "kwh")
    else:
        st.write("Please select Algorithm first")

    st.snow()

"""
  
  
"""
#st.image("images/mubea2.jpg")