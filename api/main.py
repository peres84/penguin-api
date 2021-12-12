#from src.controllers.welcome import app
from src.controllers.penguin_details import app
from src.controllers.distribution_details import app
from src.controllers.penguin_breeding import app
from src.controllers.welcome_test import app
from src.controllers.add import app
from dotenv import load_dotenv 
import os

load_dotenv()
port = os.getenv("PORT")
app.run('0.0.0.0',port, debug=True)

