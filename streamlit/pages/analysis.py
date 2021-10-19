import streamlit as st
from support.apiConnection import distribution_details, breeding_preguin, all_details_penguin
import pandas as pd
import plotly.express as px
from PIL import Image
from streamlit_folium import folium_static
import folium


#@st.cache(allow_output_mutation=True, max_entries=1)
def island_module(island):
    
    data_island = distribution_details()
    st.subheader(f'Distribution in {island.capitalize()}')
    dfa = data_island['total_penguins_by_sex']['by_island'][island]['famele']
    dm = data_island['total_penguins_by_sex']['by_island'][island]['male']
    df = pd.DataFrame({'Famele': [dfa], 'Male':[dm], 'Total': dfa+dm})
    st.write(df)

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
  
def island_signy(island):
    st.subheader('Average born by Specie from 1978 to 2015 Signy Island')

    data = breeding_preguin()
    data_years = [int(row['year']) for row in data]
    data_average_born = [row['average_born_by_species']  for row in data]

    gento_y = []
    chinstrap_y = []
    adelie_y = []

    for value in data_average_born:
        gento_y.append(value['gentoo'])
        chinstrap_y.append(value['chinstrap'])
        adelie_y.append(value['adelie'])
    
    #st.write(data_years)
    #st.write(data_average_born)
    #st.write(gento_y, chinstrap_y, adelie_y)

    lst = [data_years, gento_y, chinstrap_y, adelie_y]
    df = pd.DataFrame(lst).T
    df = df.rename(columns={0: 'year', 1: 'Gento', 2: 'Chinstrap', 3: 'Adelie'})
    df = df.set_index('year')
    st.write(df)
    st.download_button(
        label="Download visible data as CSV",
        data = df.to_csv().encode('utf-8'),
        file_name='Average born by Specie from 1978 to 2015.csv',
        mime='text/csv')
    fig = px.line(df)
    st.plotly_chart(fig, use_container_width=True, title = "Breeding by year of each Specie")

    st.subheader('Map Location')
    location = [-60.6769774, -45.8848705]
    tooltip = 'Palmer Archipelago'
    m = folium.Map(location, zoom_start=9, width="100%", height="%100")
    folium.Marker(location, popup=f"{island}", tooltip=tooltip).add_to(m)
    folium_static(m)



def analysis_page():

    image = Image.open('pages/img/penguin.png')
    st.image(image)
    st.title(" Analysis of Palmer Archipelago (Antarctica)")
    st.write('here, you can see the average weight of penguins according to their species')
    data = distribution_details()['average_weight']
    df = pd.DataFrame(dict(Species=data.keys(), Weight=data.values()))
    #st.write(df)
    
    fig = px.bar(df, x=df.Species, y=df.Weight, color=["red", "goldenrod", "#00D"], color_discrete_map="identity")
    st.plotly_chart(fig, use_container_width=True)


    st.write('In this section you will have full details about penguins on each island, you can know: \
        Number of penguins per island, and total, Distribution of penguin species by island, \
        Number of penguins according to their sex, by island and total')

    island_options = st.selectbox('Select the Island', ['Dream', 'Torgersen', 'Biscoe']).lower()
    island_module(island_options)


    st.write('Another usefull information about this penguins species is their reproducion from 1978 to 2015 \
        in the Signy Island')

    island_signy('Signy Island')
    
