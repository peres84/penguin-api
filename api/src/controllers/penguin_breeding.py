from src.app import app
from flask import request
from src.utils.json_resp import serialize
from src.utils.error import errorHandling, MissingArgumentError
from src.utils.mongoConnection import penguin_breeding_signy


#http://127.0.0.1:5000/penguin/breeding/year?max=2000&min=1990
@app.route("/penguin/breeding/year")
@errorHandling
@serialize
def breeding_year():
    limit = request.args.get("limit")
    limit = 5 if not limit else int(limit)
    max_y = request.args.get("max")
    min_y = request.args.get("min")

    if not max_y or not min_y:
        raise MissingArgumentError("max - min of year")
    else: 
        max_y = int(max_y)
        min_y = int(min_y)

    q = {"$and": [
                    {"year": {"$gte" : min_y}},
                    {"year": {"$lte" : max_y}}
                ]
            }
    breeding_year = penguin_breeding_signy.find(q).sort("year", 1).limit(limit)
    return breeding_year