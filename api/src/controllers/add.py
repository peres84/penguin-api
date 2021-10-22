from src.app import app
from flask import request
from src.utils.json_resp import serialize
from src.utils.error import errorHandling, MissingArgumentError
from src.utils.mongoConnection import check_messages
from numpy import random
from dotenv import load_dotenv 
import os
from pymongo import MongoClient 



@app.route("/messages/add", methods=["POST"])
@errorHandling
@serialize
def message_login():
    penguin = request.args.get("penguin")
    weight = int(request.args.get("weight"))
    sex = request.args.get("sex")
    location = request.args.get("location")
    username = request.args.get("username")
    password = request.args.get("password")
    if request.method == "GET":
        return not_allow_to_send()
    elif request.method == "POST":
        return insert_message(penguin, weight, sex, location, username, password)

def not_allow_to_send():
    return {
        "Error":"Not Allowed",
        "Message":"If you wish to contribute, please contact the develop team"
    }

def insert_message(penguin = None, weight = None, sex = None, location = None, username = None, password = None ):
    
    load_dotenv()
    user_check = os.getenv("MONGO_USER")
    pass_check = os.getenv("MONGO_PASS")
    #escribir funcion check = None
    if penguin == None:
        raise MissingArgumentError(penguin)
    elif weight == None:
        raise MissingArgumentError(weight)
    elif sex == None:
        raise MissingArgumentError(sex)
    elif location == None:
        raise MissingArgumentError(location)
    elif username != user_check or password != pass_check:
        raise MissingArgumentError("user name or password incorrect")
    #print("gaew")
    url_connection = f"mongodb+srv://{username}:{password}@dbpenguin.yrtiv.mongodb.net/test"
    client = MongoClient(url_connection)
    db = client.get_database("dbml-penguin")
    messages = db.messages
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
    username = request.args.get("username")
    password = request.args.get("password")
    if request.method == "GET":
        return not_allow_to_send()
    elif request.method == "POST":
        return update_message(penguin, weight, sex, location, id, username, password)

def update_message(penguin = None, weight = None, sex = None, location = None, id = None, username = None, password = None):
    
    load_dotenv()
    user_check = os.getenv("MONGO_USER")
    pass_check = os.getenv("MONGO_PASS")
    if penguin == None:
        raise MissingArgumentError(penguin)
    elif weight == None:
        raise MissingArgumentError(weight)
    elif sex == None:
        raise MissingArgumentError(sex)
    elif location == None:
        raise MissingArgumentError(location)
    elif id == None:
        raise MissingArgumentError(id)
    elif username != user_check or password != pass_check:
        raise MissingArgumentError("user name or password incorrect")
 
    #print("gaew")
    url_connection = f"mongodb+srv://{username}:{password}@dbpenguin.yrtiv.mongodb.net/test"
    client = MongoClient(url_connection)
    db = client.get_database("dbml-penguin")
    messages = db.messages
    messages.update_one({"n_id":id}, {'$set': { "specie":penguin, 
                                        "weight":weight, 
                                        "sex":sex,
                                        "location":location}})
    #print("no tengo permisos")
    return {
        "status":"OK. Updated successfully.",
        "penguin_id": id
    }



@app.route("/messages/list")
@errorHandling
@serialize
def check_list():
    check_list = check_messages.find({})
    return check_list
    