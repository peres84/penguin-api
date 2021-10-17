from src.app import app
from flask import request
from src.utils.json_resp import serialize
from src.utils.error import errorHandling, MissingArgumentError
from src.utils.mongoConnection import penguin_details

#http://127.0.0.1:5000/penguin/especies/list
#http://127.0.0.1:5000/penguin/especies/list?island=dream&limit=10
@app.route("/penguin/especies/list")
@errorHandling
@serialize
def list_species():
    island = request.args.get("island")
    limit = request.args.get("limit")
    limit = 5 if not limit else int(limit)
    if not island:
        all_species = penguin_details.find({}).distinct("specie")
    else:
        print(island)
        q = {"location.island":island.capitalize()}
        all_species = penguin_details.find(q).limit(limit)

    return all_species


#http://127.0.0.1:5000/penguin/especies/Chinstrap%20penguin?limit=10
#http://127.0.0.1:5000/penguin/especies/Chinstrap%20penguin?sex=female
#http://127.0.0.1:5000/penguin/especies/Adelie%20Penguin?sex=male
#http://127.0.0.1:5000/penguin/especies/Adelie%20Penguin?island=dream&sex=male
#http://127.0.0.1:5000/penguin/especies/Adelie%20Penguin?island=dream&limit=10
@app.route("/penguin/especies/<specie>")
@errorHandling
@serialize
def penguin_specie(specie):
    limit = request.args.get("limit")
    limit = 5 if not limit else int(limit)
    sex = request.args.get("sex")
    sex = 'none' if not sex else sex
    list_sex = ['female', 'male']
    island = request.args.get("island")
    island = 'none' if not island else island
    island_list  = ['dream', 'torgersen', 'biscoe']

    if sex in list_sex and island in island_list:
        q = { "specie":specie,
        "$and": [
                {"sex":sex.upper()},
                {"location.island":island.capitalize()}
            ]
        }
        penguin = penguin_details.find(q).limit(limit)
    elif sex in list_sex or island in island_list:
        q = { "specie":specie,
        "$or": [
                {"sex":sex.upper()},
                {"location.island":island.capitalize()}
            ]
        }
        penguin = penguin_details.find(q).limit(limit)
    else:
        q = {"specie":specie}
        penguin = penguin_details.find(q).limit(limit)

    return penguin


#http://127.0.0.1:5000/penguin/especies/weight?specie=all&min=3700&max=3750&limit=20
@app.route("/penguin/especies/weight")
@errorHandling
@serialize
def penguin_specie_by_weight():
    limit = request.args.get("limit")
    limit = 5 if not limit else int(limit)
    max_w = request.args.get("max")
    min_w = request.args.get("min")
    specie = request.args.get("specie")

    if not max_w or not min_w:
        raise MissingArgumentError("max_w - min_w")
    else: 
        max_w = int(max_w)
        min_w = int(min_w)

    if specie == "all":
        q = {"$and": [
                    {"weight": {"$gte" : min_w}},
                    {"weight": {"$lte" : max_w}}
                ]
            }
        penguin = penguin_details.find(q).limit(limit)

    else:
        q = {"specie":specie,
             "$and": [
                    {"weight": {"$gte" : min_w}},
                    {"weight": {"$lte" : max_w}}
                ]
            }
        penguin = penguin_details.find(q).sort("weight",-1).limit(limit)

    return penguin


