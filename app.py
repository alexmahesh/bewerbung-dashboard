import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title('Bewerbungs-Dashboard')
st.markdown('Statistik meiner Bewerbungen als Data Analyst')

# Verbindung zum Google Spreadsheet herstellen
con = st.connection('gsheets', type=GSheetsConnection)

# Daten lesen, worksheet=Name des Spreadsheet, usecols=Anzahl der zu verwendenden Spalten, 
# ttl=5 sekunden (wie oft die Daten aktualisiert werden, Standard ist 60 Min.)
# Gibt autom. Pandas Dataframe zurück
data = con.read(worksheet='Bewerbungen', usecols=list(range(8)), ttl=5)
data.dropna(how='all', inplace=True)

st.dataframe(data)