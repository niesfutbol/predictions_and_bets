import pandas as pd
import streamlit as st
import requests

conn = requests.get("http://104.248.109.197:8383/v1/predictions")
bets = pd.DataFrame.from_dict(conn.json()).sort_values(by=['date'])

# ----------------- game start --------
st.dataframe(bets.style.highlight_max(axis=0))

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
