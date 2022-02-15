import streamlit as st
import pandas as pd 
import altair as alt



st.title('An Overview of the Sicilian Defense.')


st.text(" “Those who say they understand chess, understand nothing.” – Robert Hübner")

st.write("I presume I evade a dark fate, because I sincerely cannot say I understand chess. Yet, chess is beautifully unique in the way that we have built mechanisms to quantify and analyze the game through complex statistical means. With this, we can gain a really interesting insight into all chess’s moving parts. And, even the layman (which I would believe myself to be) can grow to grasp the game! ")


st.write("Our data is derived from two chess tournaments held on one of the most prominent chess platforms, lichess. Utilizing thier API, we scraped data of two tournaments held simultaneously in January 2022: one consisting of only titled players and one open to all players. With almost 8000 games to analyze, the first step is to start at the beginning. How do the players tend to open? Put simply, the foundational mechanism of any chess game is known as the opening. Opening theory intends to document most, if not all, possible sets of opening plays in the ECO (Encyclopedia of Chess Openings)")


df = pd.read_csv('trackingmoves1.csv')

st.markdown("**__A chart to show the amount of time a given opening was played, cumulatively, with each second of the tournament.__**")

st.line_chart(df)

st.caption("On the x axis, we cataloged each second of the tournament. The y axis displays the total amount of times a given opening was used at that point in the tournament.")

st.header('Insight into varations of the Sicilian Defense')

st.write("As displayed by the above line chart, we plotted the top 5 most common moves against time. We saw that the Sicilian defense was played significantly more times than any other opening move and wanted to investigate and understand more about this play.")

st.image('SDIM.png')

st.write("With an infinite possibility of moves within a game, it is intuitive that with each pair of moves we diverge into further tertiary and quaternary plays. The basis of the Sicilian defense consists of two moves (e4 d5), shown in the image above. Yet, as the game continues, we break away into a multitude of variations of the standard Sicilian Defense.")


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

st.write("Interestingly, the Moscow Variation has a slightly lower win rate than the Chekhover Variation. However, as the contrasting tones suggest,  the Moscow Variation has an average blunder for white of 0 and the Chekhover Variation has that of 3. The Moscow varation is actually classified as a 'Anti-Sicilian', a play initiated by white to counter the Sicilian Defense. Noting this, it would be interesting to use the data to paint a picture of the inside of the game.")

st.header("Evaluation Plotting")

st.write("Lichess utilizes stockfish, a chess rating engine, to provide evaluations as a rating system after a move is played. Stockfish uses factors such as piece placement, material and price classifications in order to calculate an in-game performance rating which gives an indication of the player's relative advantage. A negative eval score indicates a preferable standing for black, and a positive score a preferable standing for white. Higher absolute ratings propose a heavier advantage for the relevant player. Through the lichess API, we were able to collect dictionaries of the eval scores for each move, within each game. For these two variations, we were able to calculate and plot the average eval volatility to get a static look at thier subsequent game dynamics.")

st.image("check.png")
         
st.image("russia.png")

st.write("The two variations have relatively tepid openings. Yet, we can see that the Checkov variation sets up for a slightly more hostile middle game than the Moscow variation. The Mosccow variation’s middle game tails closely behind its opening, encouraging a balanced game. The fact the evals deviate very little from move to move at this point explains the low blunder average, as the environment remains conservative. However, from the 100th move on we observe a strong black lead, followed by a strong white lead. The two seem fairly symmetrical about the x axis. Interestingly, however, the Checkov variation’s middle only slightly differs from that of Moscow. But from the 100th move onwards, the game skews extremely heavily in favor of black for a much larger period of the game, explaining why we see such a high relative average blunder rate for white!")
