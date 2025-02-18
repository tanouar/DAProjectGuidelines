import streamlit as st
import json
import requests

def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Erreur lors du chargement de {file_path} : {e}")
        return {}

def extract_links(data):
    links = []
    if isinstance(data, dict):
        for value in data.values():
            links.extend(extract_links(value))
    elif isinstance(data, list):
        for item in data:
            links.extend(extract_links(item))
    elif isinstance(data, str) and data.startswith("http"):
        links.append(data)
    return links

def check_link(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    st.title("Vérificateur de liens")
    st.write("Ce script charge les liens des fichiers JSON et vérifie leur validité.")
    
    resources = load_json("data/resources.json")
    projects = load_json("data/projects.json")

    
    all_links = list(set(extract_links(resources) + extract_links(projects)))
    
    if not all_links:
        st.warning("Aucun lien trouvé dans les fichiers JSON.")
        return
    
    st.write(f"**{len(all_links)} liens trouvés**")
    results = {url: check_link(url) for url in all_links}
    
    for url, status in results.items():
        st.write(f"{'✅' if status else '❌'} {url}")
    
if __name__ == "__main__":
    main()
