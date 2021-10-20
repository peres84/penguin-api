from src.app import app
from flask import request
from src.utils.json_resp import serialize
from src.utils.error import errorHandling, MissingArgumentError
from src.utils.mongoConnection import messages
from numpy import random

@app.route("/messages/add", methods=["POST"])
@errorHandling
@serialize
def add_message():
    penguin = request.args.get("penguin")
    weight = int(request.args.get("weight"))
    sex = request.args.get("sex")
    location = request.args.get("location")
    if request.method == "GET":
        return not_allow_to_send()
    elif request.method == "POST":
        return insert_message(penguin, weight, sex, location)

def not_allow_to_send():
    return {
        "Error":"Not Allowed",
        "Message":"If you wish to contribute, please contact the develop team"
    }

def insert_message(penguin = None, weight = None, sex = None, location = None):
   
    if penguin == None:
        raise MissingArgumentError(penguin)
    elif weight == None:
        raise MissingArgumentError(weight)
    elif sex == None:
        raise MissingArgumentError(weight)
    elif location == None:
        raise MissingArgumentError(weight)
    elif id == None:
        raise MissingArgumentError(weight)
    #print("gaew")
    send_message = messages.insert_one({"n_id": random.randint(10000000),
                                        "specie":penguin, 
                                        "weight":weight, 
                                        "sex":sex,
                                        "location":location})

    #messages.update_one({"message":"hola"}, {'$set': {'message':message}})

    print("no tengo permisos")
    return {
        "status":"OK. Message added successfully.",
        "message_id": send_message.inserted_id
    }


@app.route("/messages/update", methods=["POST"])
@errorHandling
@serialize
def update_message():
    id = int(request.args.get("id"))
    penguin = request.args.get("penguin")
    weight = int(request.args.get("weight"))
    sex = request.args.get("sex")
    location = request.args.get("location")
    if request.method == "GET":
        return not_allow_to_send()
    elif request.method == "POST":
        return update_message(penguin, weight, sex, location, id)

def update_message(penguin = None, weight = None, sex = None, location = None, id = None):
   
    if penguin == None:
        raise MissingArgumentError(penguin)
    elif weight == None:
        raise MissingArgumentError(weight)
    elif sex == None:
        raise MissingArgumentError(weight)
    elif location == None:
        raise MissingArgumentError(weight)
    elif id == None:
        raise MissingArgumentError(weight)
 
    #print("gaew")
    messages.update_one({"n_id":id}, {'$set': { "specie":penguin, 
                                        "weight":weight, 
                                        "sex":sex,
                                        "location":location}})
    #print("no tengo permisos")
    return {
        "status":"OK. Updated successfully.",
        "penguin_id": id
    }



@app.route("/message/list")
@errorHandling
@serialize
def check_list():
    check_list = messages.find({})
    return check_list
    