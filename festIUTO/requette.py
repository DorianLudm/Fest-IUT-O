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

def inscription_acheteur(cnx, email, mdp, nom, prenom):
    try:
        cnx.execute(text("INSERT INTO ACHETEUR (mailAcheteur, mdp, nom, prenom) VALUES ('"+email+"', '"+mdp+"', '"+nom+"', '"+prenom+"');"))
        cnx.commit()
        print("Inscription réussie")
    except:
        print("Erreur lors de la requête inscription_acheteur")

def get_all_groupe():
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM GROUPE;"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_groupe")
        return []

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


def add_groupe_favoris(mail, idGroupe):
    try:
        cnx.execute(text("INSERT INTO FAVORIS (mailAcheteur, idGroupe) VALUES ('"+mail+"', "+str(idGroupe)+");"))
        cnx.commit()
        print("Ajout réussi")
    except:
        print("Erreur lors de la requête add_groupe_favoris")

def delete_groupe_favoris(mail, idGroupe):
    try:
        cnx.execute(text("DELETE FROM FAVORIS WHERE mailAcheteur = '"+mail+"' AND idGroupe = "+str(idGroupe)+";"))
        cnx.commit()
        print("Suppression réussie")
    except:
        print("Erreur lors de la requête del_groupe_favoris")