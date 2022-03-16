# Palmer Archipelago (Antarctica)

![](streamlit/pages/img/penguin.png)

## About 
The goal of this project is to have a better understanding of the penguins in the palmer archipelago, to achieve this, we are going to describe 6 basic objective:

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
        - island  --> Select the island to search ['dream', 'torgersen', 'biscoe'] *(Optional)
        - limit  -->  Set the max items to show (int value) *(Optional)

    Description: Search penguin details by island - collection(penguin_details) 

3. /penguin/especies/<specie> - GET
    - **Params**
        - specie --> Select the name of your specie ['Adelie Penguin', 'Gentoo penguin', 'Chinstrap penguin'] *(Required)
        - island  --> Select the island to search ['dream', 'torgersen', 'biscoe'] *(Optional)
        - sex - Select the sex of your specie ['male', 'female'] *(Optional)
        - limit  -->  Set the max items to show (int value) *(Optional)

    Description: Search penguin details by species, island or sex - collection(penguin_details) 

4. /penguin/especies/weight - GET 
    - **Params**
        - specie --> Select the name of your specie ['all', 'Adelie Penguin', 'Gentoo penguin', 'Chinstrap penguin'] *(Required)
        - max --> Set the maximun value of your weight  (int value) *(Required)
        - min --> Set the manimun value of your weight  (int value) *(Required)
        - limit  -->  Set the max items to show (int value) *(Optional)
    
    Description: Search penguin details by species, and weight - collection(penguin_details)

5. /penguin/breeding/year/all - GET
    - **Params**
        - limit  -->  Set the max items to show (int value) *(Optional)
    
    Description: Search penguin details by all years in signy island - collection(penguin_breeding)

6. /penguin/breeding/year
    - **Params**
        - max --> Set the maximun value of your year  (int value) *(Required)
        - min --> Set the manimun value of your year  (int value) *(Required)
        - limit  -->  Set the max items to show (int value) *(Optional)

    Description: Search penguin details by range years in signy island - collection(penguin_breeding)

7. /penguin/especies/distribution - GET
    - **No Params** 

    Description: Search penguin distribution details - collection(distribution_details)

8. /messages/add - POST 
    - **Params**
        - penguin --> Set the name of the penguin *(Required) 
        - weight --> Set the weight of the penguin *(Required)  
        - sex --> Set the sex of the penguin *(Required) 
        - location --> Set the location of the penguin *(Required) 
        - username --> Set your username (Contact suport to get your credentials) *(Required)
        - password --> Set your password (Contact suport to get your credentials) *(Required)
 
    Description: Add details of penguin  - collection(messages)

9. /messages/update - POST 
    - **Params**
        - id --> Choose the id of your penguin document, you want to update *(Required) 
        - penguin --> Set the name of the penguin *(Required)
        - weight --> Set the weight of the penguin *(Required)   
        - sex --> Set the sex of the penguin *(Required) 
        - location --> Set the location of the penguin *(Required) 
        - username --> Set your username (Contact suport to get your credentials) *(Required)
        - password --> Set your password (Contact suport to get your credentials) *(Required)

    Description: Update details of (ID) penguin  - collection(messages)

10. /messages/list - GET
    - **No Params**
    
    Description: Check the list you added 

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


