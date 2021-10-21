import streamlit as st
from support.apiConnection import distribution_details, breeding_preguin, get_penguin_details
import pandas as pd
import plotly.express as px
from PIL import Image
from streamlit_folium import folium_static
import folium


#@st.cache(allow_output_mutation=True, max_entries=1)
def island_module():


    island = st.selectbox('Select the Island', ['None','Dream', 'Torgersen', 'Biscoe']).lower()
    if island != 'none':
        species = st.multiselect('Choose the penguins to evalue the population', ['Adelie Penguin', 'Gentoo penguin', 'Chinstrap penguin'])
        #st.write(species)
        species_sex = []
        total = []
        #http://127.0.0.1:5000/penguin/especies/Adelie%20Penguin?island={island}&limit=100
        for item in species:
            data =  get_penguin_details(f"{item}?island={island}&limit=200")
            for row in data:
                species_sex.append(row['sex'] + ' ' + item)
                total.append(1)
                

        #st.write(length_all)
        #st.write(species_all)
        lst_sex = [species_sex, total]
        #st.write(lst)
        df_total = pd.DataFrame(lst_sex).T
        df_total = df_total.rename(columns={0:'Sex', 1:'Count'})
        col1, col2 = st.columns([1,2])
        with col2:
            #st.write(df_total)
            fig = px.pie(df_total, values='Count', names='Sex', title=f'Population by sex in {island}')
            st.plotly_chart(fig, use_container_width=True)

        with col1:

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

        m = folium.Map(location, zoom_start=12, width="100%", height="%100")
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
    
    st.write("Average breeding by specie all time")
    species = ['Adelie Penguin', 'Gentoo penguin', 'Chinstrap penguin']
    avg_breeding_total = [df['Adelie'].mean(), df['Gento'].mean(), df['Chinstrap'].mean()]
    df2 = pd.DataFrame(dict(Name=species, Total_avg = avg_breeding_total ))
    fig2 = px.bar(df2, x=df2.Name, y=df2.Total_avg, color=["red", "goldenrod", "#00D"], color_discrete_map="identity")
    st.plotly_chart(fig2, use_container_width=True)
    st.subheader('Map Location')
    location = [-60.737786, -45.6731513]
    tooltip = 'Palmer Archipelago'
    m = folium.Map(location, zoom_start=9, width="100%", height="%100")
    folium.Marker(location, popup=f"{island}", tooltip=tooltip).add_to(m)
    folium_static(m)


def bill_length():

    st.subheader('Culmen/lipper length distribution by species')
    species = st.multiselect('Choose the penguins to evalue the length', ['Adelie Penguin', 'Gentoo penguin', 'Chinstrap penguin'])
    st.subheader('Check the image to see the characteristics of the penguins body.')
    image = Image.open('pages/img/PenguinMeasurements.png')
    st.image(image)
    species_all = []
    culmen_all = []
    lipper_all = []
    for item in species:
        data =  get_penguin_details(f"{item}?limit=300")

        for row in data:
            species_all.append(item)
            culmen_all.append(row['body_features']['culmen_length_mm'])
            lipper_all.append(row['body_features']['lipper_length_mm'])

    #st.write(length_all)
    #st.write(species_all)

    lst_culmen = [species_all, culmen_all]
    #st.write(lst)
    df_culmen = pd.DataFrame(lst_culmen).T
    df_culmen = df_culmen.rename(columns={0:'Species', 1:'bill_length'})
    #st.write(df)
    fig1 = px.violin(df_culmen, x="Species", y="bill_length", color="Species", box=True, points="all", hover_data=df_culmen.columns)
    st.plotly_chart(fig1, use_container_width=True)

    lst_lipper = [species_all, lipper_all]
    #st.write(lst)
    df_lipper = pd.DataFrame(lst_lipper).T
    df_lipper = df_lipper.rename(columns={0:'Species', 1:'flipper_length'})
    #st.write(df)
    fig2 = px.violin(df_lipper, x="Species", y="flipper_length", color="Species", box=True, points="all", hover_data=df_lipper.columns)
    st.plotly_chart(fig2, use_container_width=True)





def analysis_page():

    image = Image.open('pages/img/penguin.png')
    st.image(image)
    st.title(" Analysis of Palmer Archipelago (Antarctica)")

    st.write('In this section you will have full details about penguins on each island, you can know: \
        Number of penguins per island, and total, Distribution of penguin species by island, \
        Number of penguins according to their sex, by island and total')
    island_module()

    st.write('here, you can see the average weight of penguins according to their species')
    data = distribution_details()['average_weight']
    df = pd.DataFrame(dict(Species=data.keys(), Weight=data.values()))
    #st.write(df)
    
    fig = px.bar(df, x=df.Species, y=df.Weight, color=["red", "goldenrod", "#00D"], color_discrete_map="identity")
    st.plotly_chart(fig, use_container_width=True)


    st.write('Another usefull information about this penguins species is their reproducion from 1978 to 2015 \
        in the Signy Island')

    island_signy('Signy Island')
    bill_length()
    
