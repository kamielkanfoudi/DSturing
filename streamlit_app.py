import streamlit as st
import pandas as pd 
import altair as alt



st.title('An Overview of the Sicilian Defense.')


st.text(" “Those who say they understand chess, understand nothing.” – Robert Hübner")

st.write("One thing we can learn to understand, though, is data. And, with data, I want to explore one of chess’s most famed names: The Sicilian defense! ") 

st.write("Our data is derived from two chess tournaments held on one of the most prominent chess platforms, lichess. Utilizing thier API, we scraped data of two tournaments held in January 2022: one consisting of only titled players and one open to all players. With almost 2000 games to analyze, the first step is to start at the beginning. How do the players tend to start? Put simply, the foundational mechanism of any chess game is known as the opening. Opening theory intends to document most, if not all, possible sets of opening plays in the ECO (Encyclopedia of Chess Openings)")


df = pd.read_csv('trackingmoves1.csv')

st.markdown("**__A chart to show the amount of time a given opening was played, cumulatively, with each second of the tournament.__**")

st.line_chart(df)

st.header('Insight into varations of the Sicilian Defense')

st.write("As displayed by the above line chart, we plotted the top 5 most common moves against time. We saw that the Sicilian defense was played significantly more times than any other opening move and wanted to investigate and understand more about this play.")

st.image('SDIM.png')

st.write("With an infinite possibility of moves within a game, it is intuitive that with each movement we diverge into further tertiary and quaternary plays. The basis of the Sicilian defense consists of two moves (e4 d5), shown in the image above. Yet, as the game continues, we break away into a multitude of variations of the standard Sicilian Defense.")


st.write("We can get insights into what variations are played when we separate the data by untitled and titled tournament.")

option = st.selectbox(
     'Select Which Grouping To View',
     ('Total', 'Untitled', 'Titled'))

if option == 'Total':
      st.image("pietotal.png")
      
if option == 'Untitled':
  st.image ("pieuntitled.png")
if option =='Titled':
  st.image("pietitled.png")

st.write('You selected:', option)

st.header("Variations Analysis")

st.write("We were also able to derive some basic data that will allow us to look into how the variations actually differ within a game. Select the sidebar checkboxes to view!")

rates_data = pd.read_csv("rates_data_total1.csv")

un_rates = pd.read_csv("rates_data_untitled1.csv")

titled_rates = pd.read_csv("rates_data_titled3.csv")

show_df = st.sidebar.checkbox("Show Grouped Rates Data")

show_un = st.sidebar.checkbox("Show Untitled Rates Data")

show_ti = st.sidebar.checkbox("Show Titled Rates Data")

if show_df:
  st.dataframe(rates_data)
  
if show_un:
  st.dataframe(un_rates)

if show_ti:
  st.dataframe(titled_rates)
  
st.write("In the below barchart, we displayed some of this data from the 7 most common Sicilian Defense openings. Thus, showing how certain variations (such as Sicilian Defense: Nyezhmetdinov-Rossolimo Attack) statistically present an advantage in terms of win rates for white. From the data, we also calculated the average amount of blunders for the white player as observed across all the relevant games with a given opening. A blunder is the most dire classification of error in chess, therefore a higher average blunder count implies an opening that sets up for a more complex game for that player.")

st.image("whiteblunders.png")

st.write("Interestingly, the Moscow Variation has a slightly lower win rate than the Chekhover Variation. However, as the contrasting tones suggest,  the Moscow Variation has an average blunder for white of 0 and the Chekhover Variation has that of 3. Noting this, it would be interesting to use the data to paint a picture of the inside of the game.")

st.header("Evaluation Plotting")

st.write("Lichess utilizes stockfish, a chess rating engine, to provide evaluations as a rating system after a move is played. Stockfish uses factors such as piece placement, material and price classifications in order to calculate an in-game performance rating which gives an indication of the player's relative advantage. A negative eval score indicates a preferable standing for black, and a positive score a preferable standing for white. Higher absolute ratings propose a heavier advantage for the relevant player. Through the lichess API, we were able to collect dictionaries of the eval scores for each move, within each game. For these two variations, we were able to calculate and plot the average eval volatility to get a static look at thier subsequent game dynamics."

st.image("check.png")
         
st.image("russia.png")
