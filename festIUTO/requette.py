import pyotp
from sqlalchemy import text
from .connexionPythonSQL import *
from hashlib import sha256
from .models import *


cnx = ouvrir_connexion()

def get_cnx():
    return cnx

def get_nom_and_email(cnx, email):
    try :
        res = cnx.execute(text("SELECT nom, prenom, mailAcheteur FROM ACHETEUR WHERE mailAcheteur = '"+email+"';"))
        for row in res:
            return row[0], row[1], row[2]
    except:
        print("Erreur lors de la requête get_nom_and_email")

def get_password_with_email(cnx, email):
    try :
        res = cnx.execute(text("SELECT mdp FROM ACHETEUR WHERE mailAcheteur = '"+email+"';"))
        for row in res:
            return row[0]
    except: 
        print("Erreur lors de la requête get_password_with_email")

# marche pas
def get_groupe_non_favoris(mail):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM GROUPE WHERE idGroupe not IN (SELECT idGroupe FROM FAVORIS NATURAL JOIN GROUPE WHERE mailAcheteur = '"+mail+"');"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_groupe")
        return []

# marche pas
def get_groupe_favoris(mail):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM FAVORIS NATURAL JOIN GROUPE WHERE mailAcheteur = '"+mail+"';"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_groupe")
        return []
