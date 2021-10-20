import requests

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
    all_distribution = requests.get(url).json()
    return all_distribution

def breeding_preguin():
    url = "http://127.0.0.1:5000/penguin/breeding/year/all?limit=50"
    population = requests.get(url).json()
    return population


def update_data(penguin, weight, sex, location, id):
    url = f"http://127.0.0.1:5000/messages/update?penguin={penguin}&weight={weight}&sex={sex}&location={location}&id={id}"
    check = requests.post(url)
    return check

def add_data(penguin = None, weight = None, sex = None, location = None):
    url = f"http://127.0.0.1:5000/messages/add?penguin={penguin}&weight={weight}&sex={sex}&location={location}"
    #url = "http://127.0.0.1:5000/messages/add?penguin=adelie30&weight=55550&sex=male&location=dream"
    add = requests.post(url)
    return add

def check_list_message():
    url = "http://127.0.0.1:5000//message/list"
    population = requests.get(url).json()
    return population
