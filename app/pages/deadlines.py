import streamlit as st
from datetime import timedelta
import pandas as pd

st.set_page_config(layout="wide")

st.image("app/pages/files/light-time.gif")

col1, col2 = st.columns([1, 2])

# choix de la date 
with col1:
    base_date = st.date_input("Choisis la date de commencement", pd.to_datetime("2025-02-01"))

# choix de l'etape
with col2:
    selected_row = st.selectbox('Choisis l’étape', ['Étape 0 Cadrage (Notre première réunion)', 
                                                  'Étape 1 Découverte des données et du projet', 
                                                  'Étape 2 Exploration, Nettoyage et Pre-processing', 
                                                  'Étape 3 Création de Tableaux de Bord', 
                                                  'Étape 4 Rapport final + codes', 
                                                  'Étape 5 Soutenances'])

# Texte quand etape choisie

text_0 = """La réunion doit être réalisée le  Lundi ou Mardi après l’allocation. 
Le document [Projets_méthodologie_rapports](https://docs.google.com/document/d/1IDYR48eYHUfb6DfOAkdo1vN2ACvK2rPAZwssO_25Aeg/edit?tab=t.0) vous aiguillera dans la rédaction des différents rendus.
"""

text_1 = """ 
        Votre première tâche consistera à définir le contexte et le périmètre du projet : 
        - J’attends que vous preniez vraiment le temps de **bien comprendre** le projet et de vous renseigner 
        au mieux sur les notions que celui-ci va introduire. 
        - Il faudra ensuite prendre en main et découvrir votre jeu de données et faire une **analyse** presque 
        exhaustive de celui-ci afin de mettre en lumière la **structure**, les difficultés et éventuels biais du dataset.
        - Vous pourrez utiliser ce **template** : [Rapport exploration des données](https://docs.google.com/spreadsheets/d/1JldHaFs8Pwk4SyRQDie7m_DyhGs6UbJtM5ZbGtzAnYs/edit?gid=0#gid=0).
    """
text_2 ="""
        Au moins 5 représentations graphiques construites à partir de votre jeu de données, visuelles 
        et surtout pertinentes. Pour chaque visualisation, j’attends un commentaire précis, qui analyse la figure 
        et apporte un avis “métier”. 
        Suite aux constats établis lors des étapes précédentes, vous devrez nettoyer votre jeu de données, et 
        si besoin le transformer et l’enrichir. L'objectif de cette étape est de préparer un ensemble de données 
        adapté à une analyse approfondie, ainsi qu'à la création de visualisations et de tableaux de bord pour 
        communiquer efficacement vos résultats.
        Rendu 1 : rapport d’exploration, de data visualisation et de pre-processing des données.
    """
text_3 = """
Step 1 :
Créez des visualisations de données interactives qui vont au-delà des graphiques statiques. 
Assurez-vous que les visualisations communiquent efficacement les principaux résultats. 
Adaptez les visualisations au public cible que vous envisagez pour votre projet. 
Step 2 :
Construisez un tableau de bord dynamique qui intègre les visualisations avancées dans une interface cohérente et interactive. 
Assurez-vous que le tableau de bord raconte une histoire, met en évidence des tendances, et permet aux utilisateurs d'explorer les données grâce à des filtres interactifs et des fonctionnalités de "drill-down". 
Rendu 2 : rapport de visualisation avancée des données."""
text_4 = """
Vous rendrez le rapport final : constitué des deux premiers rendus, il concrétise votre vision et votre travail face à votre projet en intégrant une conclusion et une ouverture.
Vous rendez également votre code propre et commenté."""
text_5= """
Le document Soutenance Méthodologie résume l’organisation de la soutenance.
La soutenance se déroule de la manière suivante :
20 minutes de présentation
10 minutes de questions de la part des membres du jury
Vous avez la possibilité de réaliser soit :
une présentation Powerpoint + démo Streamlit et/ou PowerBI
toute la présentation avec votre application Streamlit et/ou PowerBI
Il faudra que votre application soit :
esthétique, en particulier qu’elle contienne plusieurs onglets.
fonctionne sans bugs."""

steps = [
    {"Etape": "Étape 0 Cadrage (Notre première réunion)", "days_offset": 7, "texte": text_0},
    {"Etape": "Étape 1 Découverte des données et du projet", "days_offset": 14, "texte":text_1},
    {"Etape": "Étape 2 Exploration, Nettoyage et Pre-processing", "days_offset": 21, "texte": text_2 },
    {"Etape": "Étape 3 Création de Tableaux de Bord", "days_offset": 28, "texte": text_3},
    {"Etape": "Étape 4 Rapport final + codes", "days_offset": 35, "texte": text_4},
    {"Etape": "Étape 5 Soutenances", "days_offset": 42, "texte": text_5}
]

# Calcul des deadlines 
for step in steps:
    step['Deadline'] = base_date + timedelta(days=step['days_offset'])

df = pd.DataFrame(steps)
step_details = df[df['Etape'] == selected_row].iloc[0]
deadline = step_details['Deadline']
text = step_details['texte']

st.write(f"**Deadline pour l'étape sélectionnée** : {deadline.strftime('%Y-%m-%d')}")
st.write(f"{text}")
