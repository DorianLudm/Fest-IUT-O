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

def modifier_acheteur(cnx, nom, prenom, email, mdp):
    try:
        cnx.execute(text("UPDATE ACHETEUR SET nom = '"+nom+"', prenom = '"+prenom+"', mdp = '"+mdp+"' WHERE mailAcheteur = '"+email+"';"))
        print(text("UPDATE ACHETEUR SET nom = '"+nom+"', prenom = '"+prenom+"', mdp = '"+mdp+"' WHERE mailAcheteur = '"+email+"';"))
        cnx.commit()
        print("Modification réussie")
    except:
        print("Erreur lors de la requête modifier_acheteur")

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

def get_profil_groupe(idGroupe):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM GROUPE NATURAL JOIN STYLEMUSICAL WHERE idGroupe = "+str(idGroupe)))
        print(res)
        for row in res:
            liste.append(row)
        return liste[0]
    except:
        print("Erreur lors de la requête get_profil_groupe")
        return []

def get_billet_acheteur(cnx, mail):
    try:
        liste = []
        # res = cnx.execute(text("SELECT * FROM BILLET NATURAL JOIN ACHETEUR;"))
        res = cnx.execute(text("SELECT * FROM BILLET NATURAL JOIN ACHETEUR WHERE mailAcheteur = '"+mail+"';"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_billet_acheteur")
        return []

def delete_billet(cnx, idBillet):
    try:
        cnx.execute(text("DELETE FROM BILLET WHERE idBillet = "+str(idBillet)+";"))
        cnx.commit()
        print("Suppression réussie")
    except:
        print("Erreur lors de la requête delete_billet")

def get_max_idBillet(cnx):
    try:
        res = cnx.execute(text("SELECT MAX(idBillet) FROM BILLET;"))
        for row in res:
            return row[0]
    except:
        print("Erreur lors de la requête get_max_idBillet")

def create_billet(cnx, mail, jour):
    try:
        idBillet = get_max_idBillet(cnx) + 1
        print(idBillet)
        cnx.execute(text("INSERT INTO BILLET (idBillet, mailAcheteur, idFestival, jourdebut, idType) VALUES ('"+str(idBillet)+"', '"+mail+"', 1, 2024-01-09, 1);"))
        cnx.commit()
        print("Ajout réussi")
    except:
        print("Erreur lors de la requête create_billet")