import streamlit as st
from pages.home import home_page
from pages.data import data_page
from pages.analysis import analysis_page

st.set_page_config(
    page_title="Palmer Archipelago App",
    initial_sidebar_state="collapsed"
)

add_selectbox = st.sidebar.radio(
    "Welcome to dataInfo",
    ("Home", "DataFrames", "Analysis")
)

if add_selectbox == "DataFrames":
    data_page()
elif add_selectbox == "Analysis":
    analysis_page()
else:
    home_page()









