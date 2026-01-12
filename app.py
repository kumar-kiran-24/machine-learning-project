import streamlit as st
import numpy as np
import pandas as pd

from src.pieline.predict_pipeline import CustomData, PredictPipeline
st.set_page_config(page_title="Student Marks Prediction", layout="centered")

st.title("Student Marks Prediction App")

st.write("Fill the form below to predict marks")


gender = st.selectbox(
    "Gender",
    ["male", "female"]
)

ethnicity = st.selectbox(
    "Race / Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ["standard", "free/reduced"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading_score = st.number_input(
    "Reading Score",
    min_value=0.0,
    max_value=100.0,
    step=1.0
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0.0,
    max_value=100.0,
    step=1.0
)



if st.button("Predict Marks"):

    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    pred_df = data.get_data_as_data_frame()
    
    st.write("### Input Data")
    st.dataframe(pred_df)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    st.success(f" Predicted Math Score: **{results[0]}**")

