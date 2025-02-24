import streamlit as st
import pandas as pd
from datetime import timedelta
from streamlit_timeline import st_timeline

st.set_page_config(layout="wide")

# Demander à l'utilisateur d'entrer la Deadline de base
base_date = st.date_input("Choisir la date de départ ", pd.to_datetime("2025-02-01"))

# Créer les étapes du projet
steps = [
    {"Etape": "Étape 0 Cadrage (Notre première réunion)", "days_offset": 0},
    {"Etape": "Étape 1 Découverte des données et du projet", "days_offset": 9},
    {"Etape": "Étape 2 Exploration, Nettoyage et Pre-processing", "days_offset": 14},
    {"Etape": "Étape 3 Création de Tableaux de Bord", "days_offset": 19},
    {"Etape": "Étape 4 Rapport final + codes", "days_offset": 24},
    {"Etape": "Étape 5 Soutenances", "days_offset": 27}
]

# Calculer les dates pour chaque étape
for step in steps:
    step['Deadline'] = base_date + timedelta(days=step['days_offset'])

# Créer un DataFrame pour afficher les étapes
df = pd.DataFrame(steps)

# Afficher le tableau
st.write("Voici la timeline des étapes du projet à partir de la date de base choisie :")
st.dataframe(df[['Etape', 'Deadline']])

# Préparer les items pour la timeline avec les dates dynamiques et noms d'étape simplifiés
items = [
    {"id": idx + 1, "content": f"Étape {idx}", "start": step["Deadline"].strftime("%Y-%m-%d")} 
    for idx, step in enumerate(steps)
]

dictionnary = {"Étape 0": "Cadrage (Notre première réunion)",
               "Étape 1" :"Découverte des données et du projet",
               "Étape 2":"Exploration, Nettoyage et Pre-processing",
               "Étape 3":"Création de Tableaux de Bord",
               "Étape 4":"Rapport final + codes", 
               "Étape 5":"Soutenances"}

# Options pour rendre la timeline statique
options = {
    "scroll": False, 
    "zoomable": False,
}

# Afficher la timeline
st.subheader("Selectionne une étape pour en afficher les détails")
timeline = st_timeline(items, groups=[], options=options, height="300px")

st.write(timeline)


import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta

# Sélection de la date de départ
start_date = st.date_input("Choisir la date de départ")

# Si une date de départ est sélectionnée
if start_date:
    # Calcul des dates des étapes (avec un pas de 7 jours)
    dates = [start_date + timedelta(weeks=7*i) for i in range(4)]  # 4 étapes
    labels = [f"Etape {i}" for i in range(len(dates))]

    # Création de la figure
    fig, ax = plt.subplots(figsize=(10, 3))

    # Tracer les points de la timeline
    ax.plot(dates, [1] * len(dates), marker='o', color='dodgerblue', markersize=10, linestyle='', zorder=5)

    # Ajouter des annotations sous chaque point pour les labels
    for i, date in enumerate(dates):
        ax.annotate(labels[i], (date, 1), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=12, color='black')

    # Formater l'axe des x pour afficher les dates de manière lisible
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    plt.xticks(rotation=45)

    # Personnaliser l'axe pour enlever l'axe y et mieux centrer la timeline
    ax.get_yaxis().set_visible(False)
    ax.set_xlim(min(dates) - timedelta(days=5), max(dates) + timedelta(days=5))

    # Titre de la timeline
    ax.set_title('Timeline des étapes', fontsize=16, fontweight='bold')

    # Afficher le graphique
    st.pyplot(fig)

    # Afficher le texte en fonction de l'étape sélectionnée
    step = st.selectbox("Choisir une étape", labels)
    if step == "Etape 0":
        st.write("Description de l'étape 0 : Information sur cette première étape...")
    elif step == "Etape 1":
        st.write("Description de l'étape 1 : Détails concernant la deuxième étape...")
    elif step == "Etape 2":
        st.write("Description de l'étape 2 : Explication de la troisième étape...")
    elif step == "Etape 3":
        st.write("Description de l'étape 3 : Dernière étape du processus...")
