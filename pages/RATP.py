import streamlit as st
import pandas as pd
import plotly.express as px


# --- Titre principal en couleur ---
st.markdown(
    "<h1 style='color:#004fa3;'>🚇 Données RATP - Emplacement des gares en Ile de France</h1>",
    unsafe_allow_html=True
)
st.header(" Données RATP")
st.write("Aperçu des données d'Ile de France RATP: ")
st.image("logo ratp.png", width=500)
df = pd.read_csv("emplacement-des-gares-idf.csv",sep=";")  
st.write(df.head(5)) 

# Graphique sur le nombre de stations par ligne de métro 
stations_par_ligne = df['indice_lig'].value_counts().sort_index()
# Titre
st.title("Nombre de stations par ligne de métro")
# Création du graphique avec Plotly Express
fig = px.bar(
    x=stations_par_ligne.index,
    y=stations_par_ligne.values,
    labels={"x": "ligne de metro", "y": "Nombre de stations sur la ligne"},
    title="Stations par ligne de métro",
    color=stations_par_ligne.values,
    color_discrete_sequence=["#4bc0ad"]
)

# Forcer un pas de 1 sur l'axe X
fig.update_xaxes(dtick=1)

# Affichage dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Création du camembert
counts = df['idf'].value_counts()
fig = px.pie(
    values=counts.values,
    names=["Île-de-France", "Hors Île-de-France"],
    color=["Île-de-France", "Hors Île-de-France"],  # pour gérer les couleurs
    color_discrete_map={
        "Île-de-France": "#4bc0ad",      
        "Hors Île-de-France": "#ffffff"   
    }
)

# Options de mise en forme
fig.update_traces(
    textinfo='label+percent',
    textfont_size=12  # taille du texte
)

fig.update_layout(
    width=400,   # largeur du graphique
    height=400,  # hauteur du graphique
    margin=dict(t=20, b=20, l=20, r=20)
)

# Affichage dans Streamlit
st.plotly_chart(fig, use_container_width=True)


# Comptage du nombre de stations par exploitant
stations_par_exploitant = df['exploitant'].value_counts()

# Titre
st.title("Répartition des stations par exploitant")

# Création du camembert avec Plotly Express
fig = px.pie(
    names=stations_par_exploitant.index,
    values=stations_par_exploitant.values,
    title="Répartition des lignes ferroviaire en Ile de France",
    color_discrete_sequence=px.colors.qualitative.Set3  # palette sympa
)

# Affichage dans Streamlit

st.plotly_chart(fig, use_container_width=True)
