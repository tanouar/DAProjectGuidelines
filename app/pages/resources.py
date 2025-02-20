import streamlit as st
import os
from utils import load_json

def show(language):
    st.title("Ressources")
    content_path = f"content/{language}/resources.md"
    if os.path.exists(content_path):
        with open(content_path, "r", encoding="utf-8") as file:
            content = file.read()
            st.markdown(content)

    resources_data = load_json("data/resources.json")

    # Vérification du type de resources_data
    if isinstance(resources_data, dict):
        resources = resources_data.get("resources", {})
        st.write("### Liste des ressources")
        for category, items in resources.items():
            st.write(f"#### {category.capitalize()}")
            for item in items:
                if isinstance(item, dict):
                    st.write(f"- [{item.get('name', 'Nom inconnu')}]({item.get('url', '#')}) - {item.get('description', 'Pas de description')}")
                else:
                    st.error("Un élément n'est pas au bon format.")
    else:
        st.error("Les ressources ne sont pas au bon format. Un dictionnaire avec des catégories est attendu.")
