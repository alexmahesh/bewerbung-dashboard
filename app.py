import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


@st.cache_data
def get_data():
    # Connect to Google Sheet
    con = st.connection('gsheets', type=GSheetsConnection)
    # Read Data and return Pandas Dataframe
    return con.read(worksheet='Bewerbungen', usecols=list(range(8)), ttl=5)
    

st.title('Bewerbungs-Dashboard')
st.markdown('Statistik meiner Bewerbungen als Data Analyst')

# Read and Clean Data
data = get_data()
data.dropna(how='all', inplace=True) #Leerzeilen löschen
data['Datum'] = pd.to_datetime(data['Datum'], format='%d.%m.%Y') #Datumstyp setzen

# Calculate Statistics for Dashboard
anz_abs = data['Datum'].count() #Absolute Bewerbungen
anz_offen = data[data['Resultat']=='Offen']['Resultat'].count() #Offene Bewerbungen
anz_absagen = data[data['Resultat']=='Absage']['Resultat'].count() #Absagen

# Output
st.dataframe(data)
st.write(f'Anzahl Bewerbungen abs: {anz_abs}') 
st.write(f'Anzahl Bewerbungen offen: {anz_offen}') 
st.write(f'Anzahl Bewerbungen absagen: {anz_absagen}') 

# Anzahl durchschnittlich pro ?
# Anzahl pro Tag
# Anzahl pro Woche
# Anzahl pro Monat
# Anzahl offen
# Anzahl Gespräche
# Anzahl Bewerbungen Plattformen
# Anzahl Bewerbungen Initiativ
# Anzahl Bewerbungen Dienstleister
