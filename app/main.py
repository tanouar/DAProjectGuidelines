import streamlit as st
from pages import home, resources, projects, about
from config import get_language

# Configuration de la page
st.set_page_config(page_title="Streamlit Resources", layout="wide")

# Sélection de la langue
language = get_language()

# Menu de navigation
menu = {
    "Accueil": home,
    "Ressources": resources,
    "Projets": projects,
    "À propos": about
}

# Affichage du menu
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Aller à", list(menu.keys()))

# Affichage de la page sélectionnée
menu[selection].show(language)
