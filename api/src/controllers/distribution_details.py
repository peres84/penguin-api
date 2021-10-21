from src.app import app
#from flask import request
from src.utils.json_resp import serialize
from src.utils.mongoConnection import distribution_details

#http://127.0.0.1:5000/penguin/especies/distribution
@app.route("/penguin/especies/distribution")
@serialize
def species_distribution():
    distribution = distribution_details.find({})
    return distribution