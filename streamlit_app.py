import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import taosws
import taosrest

from datetime import datetime
"""
# Renewable Energy Example
"""
start_date = st.date_input("Enter the start date:", value="default_value_today")
start_time = st.time_input("Enter the start time:", value="now")
st.write("Start date:", start_date)
st.write("Start time:", start_time)
end_date = st.date_input("Enter the end date:", value="default_value_today")
end_time = st.time_input("Enter the end time:", value="now")
st.write("End date:", end_date)
st.write("End time:", end_time)

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
