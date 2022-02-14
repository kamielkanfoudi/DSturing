import streamlit as st
import pandas as pd 
import altair as alt



st.title('An Overview of the Sicilian Defense.')


st.text(" “Those who say they understand chess, understand nothing.” – Robert Hübner")

st.write("One thing we can learn to understand, though, is data. And, with data, I want to explore one of chess’s most famed names: The Sicilian defense! ") 

st.write("Firstly, we will look at a quick overview of two chess tournaments held on one of the most prominent chess platforms, lichess. We scraped data of two tournaments held in January 2022: one consisting of only titled players and one open to all players. With almost 2000 games to analyze, the first step is to start at the beginning. How do the players tend to start? Put simply, the foundational mechanism of any chess game is known as the opening. Opening theory intends to document most, if not all, possible sets of opening plays in the ECO (Encyclopedia of Chess Openings)")


df = pd.read_csv('trackingmoves1.csv')

st.markdown("**__A chart to show the amount of time a given opening was played, cumulatively, with each second of the tournament.__**")

st.line_chart(df)

st.header('Insight into varations of the Sicilian Defense')

st.write("As displayed by the above line chart, we plotted the top 5 most common moves against time. We saw that the Sicilian defense was played significantly more times than any other opening move and wanted to investigate and understand more about this play.")

st.image('SDIM.png')

st.write("With an infinite possibility of moves within a game, it is intuitive that with each movement we diverge into further tertiary and quaternary plays. The basis of the Sicilian defense consists of two moves (e4 d5), shown in the image above. Yet, as the game continues, we break away into a multitude of variations of this play.")

## total pie chart 

st.write("We can also get insights into what variations are played when we separate the data by untitled and titled tournament.")

## untitled, titled pie chart 

st.header("Variations Analysis")

st.write("We were also able to derive some basic data that will allow us to look into how the variations actually differ within a game.")

rates_data = pd.read_csv("rates_data_total1.csv")

show_df = st.sidebar.checkbox("Show Grouped Rates Data")

if show_df:
  st.dataframe(rates_data)
