import pandas as pd
import streamlit as st
import requests

conn = requests.get("http://104.248.109.197:8383/v1/predictions")
bets = pd.DataFrame.from_dict(conn.json())
colname = ['home_team', 'home', 'draw', 'away', 'away_team', 'round', 'date', 'league']
# ----------------- game start --------
st.dataframe(bets[colname], hide_index=True)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
