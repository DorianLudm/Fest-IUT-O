from flask_login import UserMixin
from .app import login_manager
from .connexionPythonSQL import *
import json



@login_manager.user_loader
def load_user(email):
    cnx = get_cnx()
    return get_nom_whith_email(cnx, email)

def get_articles():
    with open("./static/data/goodies.json") as file:
        data = json.load(file)
    return data
