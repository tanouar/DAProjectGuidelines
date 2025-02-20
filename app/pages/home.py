import streamlit as st
import os

def show(language):
    st.title("Accueil")
    content_path = f"content/{language}/index.md"
    if os.path.exists(content_path):
        with open(content_path, "r", encoding="utf-8") as file:
            content = file.read()
            st.markdown(content)
    else:
        st.error("Contenu non trouvé.")
