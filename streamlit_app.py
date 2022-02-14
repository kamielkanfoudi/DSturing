import streamlit as st
import pandas as pd 



st.title('An Overview of the Sicilian Defense.')


st.text(" “Those who say they understand chess, understand nothing.” – Robert Hübner")

st.text("One thing we can learn to understand, though, is data. And, with data, I want to explore one of chess’s most famed names: The Sicilian defense! ") 

st.text("Firstly, a quick overview of two chess tournaments held on one of the most prominent chess platforms, lichess. We scraped data of two tournaments held in January 2022: one consisting of only titled players and one open to all chess players. With almost 2000 games to analyze, our first step was to start at the beginning. How do the players tend to start? Put simply, the foundational mechanism of any chess game is known as the opening. Opening theory intends to document most, if not all, possible sets of opening plays in the ECO (encyclopedia of chess Openings)" 

trackingdata = pd.read_csv('trackingmoves1.csv')

st.line_chart(trackingdata)

st.caption('In the abou')
