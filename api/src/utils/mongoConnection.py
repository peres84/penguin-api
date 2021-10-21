from pymongo import MongoClient 
from dotenv import load_dotenv 
import os

load_dotenv()
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
url_connection = f"mongodb+srv://{username}:{password}@dbpenguin.yrtiv.mongodb.net/test"
client = MongoClient(url_connection)
db = client.get_database("dbml-penguin")
penguin_details = db.penguin_details
distribution_details = db.distribution_details
penguin_breeding_signy = db.penguin_breeding_signy
check_messages = db.messages