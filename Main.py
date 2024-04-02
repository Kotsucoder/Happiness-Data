import streamlit as st
import plotly.express as px
import pandas as pd

happy = pd.read_csv("happy.csv")
categories = ["GDP", "Happiness", "Generosity"]

st.title("In Search of Happiness")
x_axis = st.selectbox("Select the data for the X-axis", categories)
y_axis = st.selectbox("Select the data for the Y-axis", categories)

st.header(f"{x_axis} and {y_axis}")
labels = {"x": x_axis, "y": y_axis}
chart = px.scatter(x=happy[x_axis.lower()], y=happy[y_axis.lower()], 
                   labels=labels)
st.plotly_chart(chart)