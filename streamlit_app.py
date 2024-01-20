import pandas as pd
import streamlit as st
import requests

conn = requests.get("http://104.248.109.197:8383/v1/predictions")
all_bets = pd.DataFrame.from_dict(conn.json()).sort_values(by=['date'])
bets = all_bets.loc[(all_bets["home"] > 0.55) | (all_bets["away"] > 0.55) | (all_bets["draw"] > 0.55)]
colname = ['home_team', 'home', 'draw', 'away', 'away_team', 'round', 'date', 'league']
# ----------------- game start --------
st.dataframe(bets[colname])

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
