import streamlit as st
from support.apiConnection import distribution_details, breeding_preguin
import pandas as pd
import plotly.express as px
from PIL import Image
from streamlit_folium import folium_static
import folium




#@st.cache(allow_output_mutation=True, max_entries=1)
def island_module(island):
    
    data_island = distribution_details()
    #col1, col2 = st.columns([2, 1])
    #with col1:
    st.subheader(f'{island.capitalize()} Details')
    st.text(f"penguin in {island}: {data_island['penguins_by_island'][island]}")
    st.text(f"Total Male Penguin in {island}: {data_island['total_penguins_by_sex']['by_island'][island]['male']}")
    st.text(f"Total Females Penguin in {island}: {data_island['total_penguins_by_sex']['by_island'][island]['famele']}")
    #with col2: 
    if  island == 'dream':
        location= [-64.7333316, -64.2508425]
    elif island == 'torgersen':
        location= [-64.7666354, -64.0896808]
    else:
        location= [-64.8038213, -63.8501337]
    #st.markdown(f"<div style='background-color: #FF0000'>Hello</div>", unsafe_allow_html=True)
    m = folium.Map(location, zoom_start=12, width="100%", height="%100")
    # add marker for Liberty Bell
    tooltip = 'Palmer Archipelago'
    folium.Marker(location, popup=f"{island}", tooltip=tooltip).add_to(m)
    st.subheader('Map')
    folium_static(m)
  
def island_Signy(island):
    st.subheader('Map Location')
    location = [-60.6769774, -45.8848705]
    tooltip = 'Palmer Archipelago'
    m = folium.Map(location, zoom_start=12, width="100%", height="%100")
    folium.Marker(location, popup=f"{island}", tooltip=tooltip).add_to(m)
    folium_static(m)

    st.subheader('Average born by Specie from 1978 to 2015 Signy Island')

    data_years = breeding_preguin()['year']
    data_average_born = breeding_preguin()['average_born_by_species']

    st.write(data_years)
    st.write(data_average_born)
    #df = pd.DataFrame(dict(Species=data.keys(), Weight=data.values()))
    #st.write(df)
    #fig = px.bar(df, x=df.Species, y=df.Weight, color=["red", "goldenrod", "#00D"], color_discrete_map="identity")
    #st.plotly_chart(fig, use_container_width=True)





def analysis_page():

    image = Image.open('pages/img/penguin.png')
    st.image(image)
    st.title(" Analysis of Palmer Archipelago (Antarctica)")
    st.subheader('1.- Know the average weight of penguins according to their species')
    data = distribution_details()['average_weight']
    df = pd.DataFrame(dict(Species=data.keys(), Weight=data.values()))
    #st.write(df)
    fig = px.bar(df, x=df.Species, y=df.Weight, color=["red", "goldenrod", "#00D"], color_discrete_map="identity")
    st.plotly_chart(fig, use_container_width=True)


    st.write('Here you wil have full details about penguins on each island, you can know: \
        Number of penguins per island, and total, Distribution of penguin species by island, \
        Number of penguins according to their sex, by island and total')

    island_options = st.selectbox('Select the Island', ['Dream', 'Torgersen', 'Biscoe']).lower()
    island_module(island_options)


    st.write('Another usefull information about this penguins species is their reproducion from 1978 to 2015 \
        in the Signy Island')

    island_Signy('Signy Island')
    
