import requests
from dotenv import load_dotenv 
import os
load_dotenv()
url_main = os.getenv("URL")

def get_penguin_details(endpoint):
    url = f"{url_main}/penguin/especies/" + endpoint
    data = requests.get(url).json()
    return data

def distribution_details():
    url = f"{url_main}/penguin/especies/distribution"
    distribution = requests.get(url).json()[0]
    return distribution

def all_details_penguin():
    url = f"{url_main}/penguin/especies/list"
    all_distribution = requests.get(url).json()
    return all_distribution

def breeding_preguin():
    url = f"{url_main}/penguin/breeding/year/all?limit=50"
    population = requests.get(url).json()
    return population


def update_data(penguin, weight, sex, location, id, username, password):
    url = f"{url_main}/messages/update?penguin={penguin}&weight={weight}&sex={sex}&location={location}&id={id}&username={username}&password={password}"
    check = requests.post(url)
    return check

def add_data(penguin = None, weight = None, sex = None, location = None, username = None, password = None):
    url = f"{url_main}/messages/add?penguin={penguin}&weight={weight}&sex={sex}&location={location}&username={username}&password={password}"
    #url = "http://127.0.0.1:5000/messages/add?penguin=adelie30&weight=55550&sex=male&location=dream"
    add = requests.post(url)
    return add

def check_list_message():
    url = f"{url_main}/messages/list"
    population = requests.get(url).json()
    return population
