import streamlit as st
import os
from utils import load_json

def show(language):
    st.title("Projets")
    content_path = f"content/{language}/projects.md"
    if os.path.exists(content_path):
        with open(content_path, "r", encoding="utf-8") as file:
            content = file.read()
            st.markdown(content)

    # projects = load_json("data/projects.json")
    # st.write("### Liste des projets")
    # for project in projects:
    #     st.write(f"- [{project['name']}]({project['link']})")
