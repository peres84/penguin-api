from src.app import app
from flask import request

@app.route("/penguin/welcome")
def welcome():
    return {
        "welcome" : "penguin Api"
    }