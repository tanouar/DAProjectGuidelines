import streamlit as st


st.title('Prise de rendez-vous')
st.write("En cas de besoin ou de blocage dans l'avancée du projet, vous pouvez prendre rendez-vous pour une assistance via les calendriers suivants :")

# Lien Calendly pour chaque personne
calendly_urls = {
    "Alia": "https://calendly.com/alia-boudehane-dehanalyst/30min",
    "Tarik": "https://calendly.com/anouar-tarik/1-1-teaching-assistant",   # Mettre à jour le calendly de Tarik
    "Sans préférence": "https://calendly.com/d/cnj9-9bw-k58/da-teaching-assistant-session" 
}


left, middle, right = st.columns(3)


button_alia = left.button("Alia", use_container_width=True)
button_tarik = middle.button("Tarik", use_container_width=True)
button_sans_preference = right.button("Sans préférence", use_container_width=True)

# Affichage du calendrier en fonction du bouton cliqué
if button_alia:
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <iframe src="{calendly_urls['Alia']}" width="100%" height="800" frameborder="0"></iframe>
        </div>
    """, unsafe_allow_html=True)

elif button_tarik:
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <iframe src="{calendly_urls['Tarik']}" width="100%" height="800" frameborder="0"></iframe>
        </div>
    """, unsafe_allow_html=True)

elif button_sans_preference:
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <iframe src="{calendly_urls['Sans préférence']}" width="100%" height="800" frameborder="0"></iframe>
        </div>
    """, unsafe_allow_html=True)
