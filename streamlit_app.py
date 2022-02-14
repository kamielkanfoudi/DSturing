import streamlit as st
import pandas as pd 



st.title('An Overview of the Sicilian Defense.')


st.text(" “Those who say they understand chess, understand nothing.” – Robert Hübner")

st.text("One thing we can learn to understand, though, is data. And, with data, I want to explore one of chess’s most famed names: The Sicilian defense!") 

trackingdata = pd.read_csv('trackingmoves1.csv')

st.line_chart(trackingdata)

