import pandas as pd
import streamlit as st



premier_league = pd.read_csv("static/predictions_39_2023_0.csv.csv")
serie_a = pd.read_csv("static/predictions_135_2023_0.csv.csv")
bets = pd.concat([premier_league, serie_a], ignore_index=True).sort_values(by=['date'])
# ----------------- game start --------
st.dataframe(bets.style.highlight_max(axis=0))

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
