# Palmer Archipelago (Antarctica)

![](streamlit\pages\img\penguin.png)

##About 
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
mkdir penguin-project

#clone the repository 
git init
git clone https://github.com/peres84/BootCampProject_1.git

#setup your environment as 'streamlit' 
conda create -f environment.yml

#adding dependencies 
pip install -r requirements.txt 

```

## Api Rest 

###Controllers 

#### Enpoints 

1. /penguin/welcome - check if all is ok, you will receive "welcome" : "penguin Api"
2. /penguin/especies/list - GET
    - **Params**
    > island  - ['dream', 'torgersen', 'biscoe'] Select the island to search 
    > limit  -  Ex. limit=10 set the max items to show 
    


## License
[PJ](https://github.com/peres84)


