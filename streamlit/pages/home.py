import streamlit as st
from pages.analysis import analysis_page

def home_page(add_selectbox = "home"):
    st.title("Palmer Archipelago (Antarctica)")
    st.write("Welcome to dataInfo, the objective of this blog is to know how are the penguins in the palmer archipelago, to achieve this, we are going to describe 6 basic objective:")
    st.subheader('Objectives')
    st.write('1. Know the average weight of penguins according to their species')
    st.write('2. Number of penguins per island, and total')
    st.write('3. Distribution of penguin species by island')
    st.write('4. Average spawning of penguins according to their type on Signy Island')
    st.write('5. Predominant species, and endangered species')
    st.write('2. Number of penguins according to their sex, by island and total')

    if st.button('Learn More'):
        analysis_page()