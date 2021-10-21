# Palmer Archipelago (Antarctica)

![](streamlit/pages/img/penguin.png)

## About 
The objective of this project is to have a better understanding of the penguins in the palmer archipelago, to achieve this, we are going to describe 6 basic objective:

Objectives:
- Know the average weight of penguins according to their species
- Number of penguins per island, and total
- Distribution of penguin species by island
- Average spawning of penguins according to their type on Signy Island
- Predominant species, and endangered species
- Number of penguins according to their sex, by island and total



## Installation

Before start We need to install the dependencies requeriments.txt and environment.yml, 

Some basic Git commands are:

```

#create new directory
mkdir <folder name>

#clone the repository 
$ git init
$ git clone https://github.com/peres84/BootCampProject_1.git

#setup your environment as 'streamlit' 
$ conda create -f environment.yml

#adding dependencies 
$ pip install -r requirements.txt 

```

## API Rest 

### Enpoints 

1. /penguin/welcome - check if all is ok

2. /penguin/especies/list - GET
    - **Params**
        - island  --> Select the island to search ['dream', 'torgersen', 'biscoe'] 
        - limit  -->  Set the max items to show (int value) 

3. /penguin/especies/<specie> - GET
    - **Params**
        - specie --> Select the name of your specie ['Adelie Penguin', 'Gentoo penguin', 'Chinstrap penguin']
        - island  --> Select the island to search ['dream', 'torgersen', 'biscoe'] 
        - sex - Select the sex of your specie ['male', 'female']
        - limit  -->  Set the max items to show (int value) 

4. /penguin/especies/weight - GET 
    - **Params**
        - specie --> Select the name of your specie ['all', 'Adelie Penguin', 'Gentoo penguin', 'Chinstrap penguin']
        - max --> Set the maximun value of your weight  (int value)
        - min --> Set the manimun value of your weight  (int value)
        - limit  -->  Set the max items to show (int value) 

5. /penguin/breeding/year/all - GET
    - **Params**
        - limit  -->  Set the max items to show (int value) 

6. /penguin/breeding/year
    - **Params**
        - max --> Set the maximun value of your year  (int value)
        - min --> Set the manimun value of your year  (int value)
        - limit  -->  Set the max items to show (int value) 

7. /penguin/especies/distribution - GET
    - **No Params** 

8. /messages/add - POST 
    - **Params**
        - penguin --> Set the name of the penguin 
        - weight --> Set the weight of the penguin   
        - sex --> Set the sex of the penguin 
        - location --> Set the location of the penguin 
        - username --> Set your username (Contact suport to get your credentials)
        - password --> Set your password (Contact suport to get your credentials)

9. /messages/update - POST 
    - **Params**
        - id --> Choose the id of your penguin document, you want to update 
        - penguin --> Set the name of the penguin 
        - weight --> Set the weight of the penguin   
        - sex --> Set the sex of the penguin 
        - location --> Set the location of the penguin 
        - username --> Set your username (Contact suport to get your credentials)
        - password --> Set your password (Contact suport to get your credentials)

You may read this [Database Structure](api/dataBase_estructure.md)

## Streamlit Description

### Pages

    - Home
    - Analysis 
    - Download DataFrames
    - Update Data

### Description 

    - Home: Presentation of the project 
    - Analysis: Here you can interactive with the data, each point will represent a previous objective. 
    - Download DataFrames: Download the dataframes using in Analysis page.
    - Update Data: Once you got your credentials, you will able to colaborate with our data, you can send information about this penguin and update the previus ones 

## Support

email: peresrjavier@gmail.com

## Resources 

- Data Penguins From [Palmer Archipelago](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data)
- Data Breeding From [Population Size](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5082682/#pone.0164025.ref029) 

## License
[All Right Reserve PJ](https://github.com/peres84)


