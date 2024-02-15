import pandas as pd
import streamlit as st
import requests

conn = requests.get("http://104.248.109.197:8383/v1/predictions")
bets = pd.DataFrame.from_dict(conn.json())
colname = ["home_team", "home", "draw", "away", "away_team", "round", "date", "league"]
new_names = ["Local", "Gana local", "Empate", "Gana visita", "Visita", "Jornada", "Fecha", "Liga"]
to_rename = {k: v for (k, v) in zip(colname, new_names)}
# ----------------- game start --------
to_show = bets[colname].sort_values(by=["date", "league"])
st.write(
  """
  En la figura de abajo podemos ver un ejemplo de las predicciones hechas por el modelo de [nies](https://www.nies.futbol/).

En las columnas 1 y 2 tenemos el nombre de los equipos.
En la columna 1 tenemos a los equipos locales y en la columna dos tenemos a los equipos visitantes.
En las columnas 3 tenemos las probabilidades de que gane el local, el empate o la visita.
  """
)
st.dataframe(to_show.rename(columns=to_rename), hide_index=True)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
