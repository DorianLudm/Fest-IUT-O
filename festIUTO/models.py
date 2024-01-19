from flask_login import UserMixin
from .app import login_manager
from .connexionPythonSQL import *
import json
from .requette import get_creneaux



@login_manager.user_loader
def load_user(email):
    cnx = get_cnx()
    return get_nom_whith_email(cnx, email)

def get_articles():
    with open("./static/data/goodies.json") as file:
        data = json.load(file)
    return data


def get_planning():
    creneaux = get_creneaux()
    planning = dict()
    for c in creneaux:
        if (int(c[4].strftime("%H")), c[4].weekday()) in planning.keys():
            planning[int(c[4].strftime("%H")), c[4].weekday()].append((c[6], c[0]))
        else:
            planning[int(c[4].strftime("%H")), c[4].weekday()] = [(c[6], c[0])]
    return planning
