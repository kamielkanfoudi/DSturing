import streamlit as st
import pandas as pd 
import altair as alt



st.title('An Overview of the Sicilian Defense.')


st.text(" “Those who say they understand chess, understand nothing.” – Robert Hübner")

st.write("One thing we can learn to understand, though, is data. And, with data, I want to explore one of chess’s most famed names: The Sicilian defense! ") 

st.write("Firstly, we will look at a quick overview of two chess tournaments held on one of the most prominent chess platforms, lichess. We scraped data of two tournaments held in January 2022: one consisting of only titled players and one open to all players. With almost 2000 games to analyze, the first step is to start at the beginning. How do the players tend to start? Put simply, the foundational mechanism of any chess game is known as the opening. Opening theory intends to document most, if not all, possible sets of opening plays in the ECO (Encyclopedia of Chess Openings)")


df = pd.read_csv('trackingmoves1.csv')

st.header("A chart to show the amount of time a given opening was played, cumulatively, with each second of the tournament.")

st.line_chart(df)

st.caption('In the abouve ch')
