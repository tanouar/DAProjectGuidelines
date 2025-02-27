import streamlit as st
import streamlit_antd_components as sac

sidebar_title = '<p style="color:Black; font-size: 26px;">Navigation</p>'
st.sidebar.markdown(sidebar_title, unsafe_allow_html=True)

with st.sidebar:
    menu = sac.menu([
    sac.MenuItem('main', icon='house'),
    sac.MenuItem('about', icon='info-square'),
    sac.MenuItem('appointment', icon='calendar-event'),
    sac.MenuItem('deadlines', icon='clock-history'),
    sac.MenuItem('home', icon='house-fill'),
    sac.MenuItem('projects', icon='folder2-open', children=[
        sac.MenuItem('project 1', icon='file-earmark-bar-graph', description='description'),
        sac.MenuItem('project 2', icon='file-earmark-bar-graph', description='description' )]),
    sac.MenuItem(type='divider'),
    sac.MenuItem('Git Hub', type='group', children=[
        sac.MenuItem('Alia', icon='git', href='https://ant.design/components/menu#menu'),
        sac.MenuItem('Tarik', icon='git', href='https://icons.getbootstrap.com/'),
    ]),
], format_func='title', size='sm', color='blue', indent=10, open_all=True)





