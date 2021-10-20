import streamlit as st
from support.apiConnection import check_list_message, add_data, update_data
import pandas as pd
from PIL import Image




def user_add_data():
    st.write('In order to add you data sucesfully please put the values for each box:')

    col1, col2 = st.columns(2)

    with col1:
        penguin = st.selectbox('Choose your Specie', ('None', 'Adelie Penguin', 'Chinstrap penguin', 'Gentoo penguin'))
        #st.write('The current specie is: ', penguin)
        weight = st.number_input('Penguin weight')
        weight = int(weight)
        #st.write('The current weight is: ', weight)

    with col2:
        location = st.selectbox('Choose your Location', ('None', 'Dream', 'Torgersen', 'Biscoe'))
        #st.write('location:', location)
        sex = st.selectbox('Choose your sex', ('None', 'Female', 'Male'))
        #st.write('The current sex is: ', sex)

    if penguin != None and weight > 0 and location != 'None' and sex != 'None':

        if st.button('Send Data'):
            add_data(penguin, weight, sex, location)
            color = '#00FF00'
            st.markdown(f"<div style='background-color: {color}'>**Added Successfully**</div>", unsafe_allow_html=True)

    else:
        color = '#FF0000'
        st.markdown(f"<div style='background-color: {color}'>**PLEASE FILL ALL THE FORM**</div>", unsafe_allow_html=True)
      
def update_exist_data():

    st.write('In order to add update your data sucesfully please put the values for each box:')
    col1, col2 = st.columns(2)

    with col1:
        penguin = st.selectbox('Choose your Specie', ('None', 'Adelie Penguin', 'Chinstrap penguin', 'Gentoo penguin'))
        #st.write('The current specie is: ', penguin)
        weight = st.number_input('Penguin weight')
        weight = int(weight)
        #st.write('The current weight is: ', weight)
        id = st.number_input('Penguin n_id')
        id = int(id)
        st.write(id)
        #st.write('The current weight is: ', weight)

    with col2:
        location = st.selectbox('Choose your Location', ('None', 'Dream', 'Torgersen', 'Biscoe'))
        #st.write('location:', location)
        sex = st.selectbox('Choose your sex', ('None', 'Female', 'Male'))
        #st.write('The current sex is: ', sex)

    if penguin != None and weight > 0 and location != 'None' and sex != 'None' and id > 0:

        if st.button('Update Data'):
            update_data(penguin, weight, sex, location, id)
            color = '#00FF00'
            st.markdown(f"<div style='background-color: {color}'>**Added Successfully**</div>", unsafe_allow_html=True)

    else:
        color = '#FF0000'
        st.markdown(f"<div style='background-color: {color}'>**PLEASE FILL ALL THE FORM**</div>", unsafe_allow_html=True)


def main_dashboard():
    st.header("If you want to contrubute with our data, feel free to send your query")
    image = Image.open('pages/img/penguin.png')
    st.image(image)

    option = st.selectbox('Choose your query', ('None', 'Add Data', 'Update Data', 'Check Data'))

    if option == 'Add Data':
        user_add_data()
    elif option == 'Check Data':
        data = check_list_message()
        df = pd.DataFrame(data)
        st.write(df)
    elif option == 'Update Data':
        #something
        update_exist_data()
    else:
        st.write('select an option')







