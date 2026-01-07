import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns(3)
with col1:
    exp_ID = st.text_input("experiment ID", placeholder="Enter experiment ID")
with col2:
    startTime = st.datetime_input("start time")
with col3:
    endTime = st.datetime_input("end time")
sensor_types = pd.read_csv("sensorTypes.csv")

col_sensor_type, col_distribution = st.columns([2, 1])

with col_sensor_type:
    sensor_type = st.selectbox(
        "sensor type",
        sensor_types.iloc[0:],
        index=None,
        placeholder="Select sensor",
    )

with col_distribution:
    distribution = st.selectbox(
        "Distribution",
        ("Hourly", "Daily", "Weekly", "Monthly", "Yearly"),
        index=None,
        placeholder="Select Distribution",
    )


st.button("Graph")
