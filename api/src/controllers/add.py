from src.app import app
from flask import request
from src.utils.json_resp import serialize
from src.utils.error import errorHandling, MissingArgumentError
from src.utils.mongoConnection import messages


@app.route("/messages/add", methods=["POST"])
@errorHandling
@serialize
def add_message():
    message = request.args.get("message")
    if request.method == "GET":
        return not_allow_to_send()
    elif request.method == "POST":
        return insert_message(message)

def not_allow_to_send():
    return {
        "Error":"Not Allowed",
        "Message":"If you wish to contribute, please contact the develop team"
    }

def insert_message(message = None):
   
    if message == None:
        raise MissingArgumentError("message")
    print("gaew")
    send_message = messages.insert_one({"message":message})

    messages.update_one({"message":"hola"}, {'$set': {'message':'1234test_update', "test":500}})

    print("no tengo permisos")
    return {
        "status":"OK. Message added successfully.",
        "message_id": send_message.inserted_id
    }