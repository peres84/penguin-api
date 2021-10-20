import streamlit as st
from pages.home import home_page
from pages.data import data_page
from pages.analysis import analysis_page
from pages.check_page import main_dashboard


st.set_page_config(
    page_title="Palmer Archipelago App",
    initial_sidebar_state="collapsed"
)

add_selectbox = st.sidebar.radio(
    "Welcome to dataInfo",
    ("Home", "Analysis", "Download DataFrames", "Update Data")
)

if add_selectbox == "Analysis":
    analysis_page()
elif add_selectbox == "Download DataFrames":
    data_page()
elif add_selectbox == "Update Data":
    main_dashboard()
else:
    home_page()









