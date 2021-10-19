import requests
import numpy as np


def get_penguin_details(endpoint):
    url = "http://127.0.0.1:5000/penguin/especies/" + endpoint
    data = requests.get(url).json()
    return data


def distribution_details():
    url = "http://127.0.0.1:5000/penguin/especies/distribution"
    distribution = requests.get(url).json()[0]
    return distribution

def all_details_penguin():
    url = "http://127.0.0.1:5000//penguin/especies/list"
    all_distribution = requests.get(url).json()[0]
    return all_distribution

def breeding_preguin():
    url = "http://127.0.0.1:5000/penguin/breeding/year/all?limit=50"
    population = requests.get(url).json()
    return population

