from src.app import app

@app.route("/penguin/welcome")
def welcome():
    return {
        "welcome" : "penguin Api"
    }