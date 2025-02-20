import streamlit as st

def get_language():
    return st.sidebar.selectbox("Langue", ["FR", "EN"], index=0)
