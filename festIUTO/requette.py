from sqlalchemy import text
from .connexionPythonSQL import *
from hashlib import sha256
from .models import *


cnx = ouvrir_connexion()

def get_cnx():
    return cnx

def get_nom_and_email(cnx, email):
    try :
        res = cnx.execute(text("SELECT nom, prenom, mailAcheteur, idRoleAcheteur FROM ACHETEUR WHERE mailAcheteur = '"+email+"';"))
        for row in res:
            return row[0], row[1], row[2], row[3]
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
        print("get_all_groupe")
        res = cnx.execute(text("SELECT idGroupe, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe, nomImage FROM GROUPE NATURAL JOIN PHOTOGROUPE"))
        for row in res:
            print(row)
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_groupe")
        return []

def get_all_nom_groupe():
    try:
        liste = []
        res = cnx.execute(text("SELECT nomGroupe FROM GROUPE;"))
        for row in res:
            liste.append(row[0])
        return liste
    except:
        print("Erreur lors de la requête get_all_nom_groupe")
        return []

def get_all_artiste():
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM ARTISTE NATURAL JOIN GROUPEARTISTE NATURAL JOIN GROUPE;"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_artiste")
        return []

def ajouter_artiste(cnx, nomArtiste, prenomArtiste, idGroupe):
    try:
        nbPersn = get_groupe_with_idGroupe(cnx, idGroupe)[0]
        nbArtisteActuel = get_nombre_artiste_in_groupe(cnx, idGroupe)
        if int(nbPersn) > int(nbArtisteActuel):  
            cnx.execute(text("INSERT INTO ARTISTE (nomArtiste, prenomArtiste) VALUES ('"+nomArtiste+"', '"+prenomArtiste+"');"))
            cnx.execute(text("INSERT INTO GROUPEARTISTE (idArtiste, idGroupe) VALUES ((SELECT MAX(idArtiste) FROM ARTISTE), "+str(idGroupe)+");"))
            cnx.commit()
            print("Ajout réussi")
        print("Ajout échouer trop d'artiste dans le groupe")
    except:
        print("Erreur lors de la requête ajouter_artiste")

def supprimer_artiste(cnx, idArtiste):
    try:
        idGroupe = get_groupe_artiste(cnx, idArtiste)[0]
        cnx.execute(text("DELETE FROM GROUPEARTISTE WHERE idArtiste = "+str(idArtiste)+";"))
        cnx.execute(text("DELETE FROM ARTISTE WHERE idArtiste = "+str(idArtiste)+";"))
        cnx.commit()
        print("Suppression réussie")
    except:
        print("Erreur lors de la requête supprimer_artiste")

def get_profil_artiste(idArtiste):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM ARTISTE WHERE idArtiste = "+str(idArtiste)+";"))
        for row in res:
            liste.append(row)
        return liste[0]
    except:
        print("Erreur lors de la requête get_profil_artiste")
        return []

def set_profil_artiste(cnx, idArtiste, nomArtiste, prenomArtiste, idGroupe):
    try:
        nbPersn = get_groupe_with_idGroupe(cnx, idGroupe)[0]
        print(nbPersn)
        nbArtisteActuel = get_nombre_artiste_in_groupe(cnx, idGroupe)
        if int(nbPersn) > int(nbArtisteActuel):  
            cnx.execute(text("UPDATE GROUPEARTISTE SET idGroupe = "+str(idGroupe)+" WHERE idArtiste = "+str(idArtiste)+";"))
            cnx.execute(text("UPDATE ARTISTE SET nomArtiste = '"+nomArtiste+"', prenomArtiste = '"+prenomArtiste+"' WHERE idArtiste = "+str(idArtiste)+";"))
            cnx.commit()
            print("Modification réussie")
        print("Modification échouer trop d'artiste dans le groupe")
    except:
        print("Erreur lors de la requête set_profil_artiste")

def get_groupe_with_idGroupe(cnx, idGroupe):
    try:
        liste = []
        res = cnx.execute(text("SELECT nbPersn FROM GROUPE NATURAL JOIN PHOTOGROUPE WHERE idGroupe = "+str(idGroupe)+";"))
        for row in res:
            liste.append(row)
        return liste[0]
    except:
        print("Erreur lors de la requête get_groupe_with_idGroupe")
        return []


def get_nombre_artiste_in_groupe(cnx, idGroupe):
    try:
        liste = []
        res = cnx.execute(text("SELECT COUNT(idArtiste) FROM GROUPEARTISTE WHERE idGroupe = "+str(idGroupe)+";"))
        for row in res:
            liste.append(row)
        print(liste[0][0])
        return liste[0][0]
    except:
        print("Erreur lors de la requête get_nombre_artiste_in_groupe")
        return []

def get_groupe_non_favoris(mail):
    try:
        liste = []
        res = cnx.execute(text("SELECT idGroupe, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe, nomImage FROM GROUPE NATURAL JOIN PHOTOGROUPE WHERE idGroupe not IN (SELECT idGroupe FROM FAVORIS NATURAL JOIN GROUPE WHERE mailAcheteur = '"+mail+"');"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_groupe_non_favoris")
        return []

def get_groupe_favoris(mail):
    try:
        liste = []
       # res = cnx.execute(text("SELECT idGroupe, mailAcheteur, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe, nomImage FROM GROUPE NATURAL JOIN FAVORIS NATURAL JOIN PHOTOGROUPE WHERE mailAcheteur = '"+mail+"';"))
        print(text("SELECT idGroupe, mailAcheteur, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe, nomImage FROM PHOTOGROUPE NATURAL JOIN GROUPE NATURAL JOIN FAVORIS NATURAL JOIN GROUPE WHERE mailAcheteur = '"+mail+"';"))
        res = cnx.execute(text("SELECT idGroupe, mailAcheteur, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe, nomImage FROM PHOTOGROUPE NATURAL JOIN FAVORIS NATURAL JOIN GROUPE WHERE mailAcheteur = '"+mail+"';"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_groupe_favoris")
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


def get_creneaux():
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM CRENEAU order by heureDebut;"))
        print(res)
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_creneau")

    
def get_image_groupe(idGroupe):
    try :
        liste = []
        res = cnx.execute(text("SELECT nomImage FROM PHOTOGROUPE NATURAL JOIN GROUPE WHERE idGroupe = "+str(idGroupe)+";"))
        print(res)
        for row in res:
            liste.append(row)
        return liste[0]
    except:
        print("Erreur lors de la requête get_image_groupe")
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

def get_billet(cnx, idBillet):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM BILLET WHERE idBillet = '"+idBillet+"';"))
        for row in res:
            liste.append(row)
        return liste[0]
    except:
        print("Erreur lors de la requête get_billet")
        return None

def set_billet(cnx, idBillet, jour, jourDeux=None):
    try:
        if jourDeux == None:
            print("UPDATE BILLET SET jourDebut = '"+jour+"' WHERE idBillet = '"+str(idBillet)+"';")
            cnx.execute(text("UPDATE BILLET SET jourDebut = '"+jour+"' WHERE idBillet = '"+str(idBillet)+"';"))
        else:
            print("UPDATE BILLET SET jourDebut = '"+jour+"', jourDeux = '"+jourDeux+"' WHERE idBillet = '"+str(idBillet)+"';")
            cnx.execute(text("UPDATE BILLET SET jourDebut = '"+jour+"', jourDeux = '"+jourDeux+"' WHERE idBillet = '"+str(idBillet)+"';"))
        cnx.commit()
        print("Modification réussie")
    except:
        print("Erreur lors de la requête set_billet")

def delete_billet(cnx, idBillet):
    try:
        cnx.execute(text("DELETE FROM BILLET WHERE idBillet = "+str(idBillet)+";"))
        cnx.commit()
        print("Suppression réussie")
    except:
        print("Erreur lors de la requête delete_billet")

def supprimer_all_billet_acheteur(cnx, mail):
    try:
        cnx.execute(text("DELETE FROM BILLET WHERE mailAcheteur = '"+mail+"';"))
        cnx.commit()
        print("Suppression réussie")
    except:
        print("Erreur lors de la requête supprimer_billet_acheteur")

def get_max_idBillet(cnx):
    try:
        res = cnx.execute(text("SELECT MAX(idBillet) FROM BILLET;"))
        for row in res:
            return row[0]
    except:
        print("Erreur lors de la requête get_max_idBillet")

def create_billet(cnx, mail, jour, idType, jourDeux=None):
    try:
        idBillet = get_max_idBillet(cnx) + 1
        print(idBillet)
        if idType == 2:
            cnx.execute(text("INSERT INTO BILLET (idBillet, mailAcheteur, idFestival, jourdebut, jourDeux, idType) VALUES ('"+str(idBillet)+"', '"+mail+"', 1, '"+jour+"', '"+jourDeux+"', '"+str(idType)+"');"))
        else:
            cnx.execute(text("INSERT INTO BILLET (idBillet, mailAcheteur, idFestival, jourdebut, idType) VALUES ('"+str(idBillet)+"', '"+mail+"', 1, '"+jour+"', '"+str(idType)+"');"))
        cnx.commit()
        print("Ajout réussi")
    except:
        print("Erreur lors de la requête create_billet")

def recherche_groupe(cnx, recherche):
    liste = []
    res = cnx.execute(text("SELECT * FROM GROUPE WHERE nomGroupe LIKE '%"+recherche+"%';"))
    for row in res:
        # Convertir l'objet Row en tuple
        row_tuple = tuple(row)  
        # Ajouter une nouvelle ID à l'indice 0 de chaque ligne
        row_with_id = ("1",) + row_tuple
        liste.append(row_with_id)
    return liste
  
def recherche_creneau(cnx, recherche):
    liste = []
    res = cnx.execute(text("SELECT * FROM CRENEAU WHERE descriptionEvenement LIKE '%"+recherche+"%';"))
    for row in res:
        # Convertir l'objet Row en tuple
        row_tuple = tuple(row)  
        # Ajouter une nouvelle ID à l'indice 0 de chaque ligne
        row_with_id = ("2",) + row_tuple
        liste.append(row_with_id)
    return liste

def get_artistes_avec_meme_style(cnx, idGroupe):
    try:
        liste = []
        res = cnx.execute(text("SELECT idGroupe, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe, nomImage FROM GROUPE NATURAL JOIN PHOTOGROUPE WHERE idStyle = (SELECT idStyle FROM GROUPE WHERE idGroupe = "+str(idGroupe)+") and idGroupe != "+str(idGroupe)+";"))
        for row in res:
            print(row)
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_artistes_avec_meme_style")
        return []

def artiste_favoris_acheteur(cnx, mail, idGroupe):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM FAVORIS WHERE mailAcheteur = '"+mail+"' AND idGroupe = "+str(idGroupe)+";"))
        for row in res:
            liste.append(row)
        if len(liste) == 0:
            return False
        else:
            return True
    except:
        print("Erreur lors de la requête artiste_favoris_acheteur")
        return []
   
def get_all_spectateur():
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM ACHETEUR;"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_spectateur")
        return []

def get_all_spectateur_with_search(cnx, recherche):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM ACHETEUR WHERE nom LIKE '%"+recherche+"%' OR prenom LIKE '%"+recherche+"%' OR mailAcheteur LIKE '%"+recherche+"%';"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_spectateur_with_search")
        return []

def get_all_artistes_with_search(cnx, recherche):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM ARTISTE NATURAL JOIN GROUPEARTISTE NATURAL JOIN GROUPE WHERE nomArtiste LIKE '%"+recherche+"%' OR prenomArtiste LIKE '%"+recherche+"%';"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_artistes_with_search")
        return []

def get_profil_spectateur(cnx, mail):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM ACHETEUR WHERE mailAcheteur = '"+mail+"';"))
        for row in res:
            liste.append(row)
        return liste[0]
    except:
        print("Erreur lors de la requête get_profils_spectateur")

def ajouter_spectateur(cnx, nom, prenom, email, mdp, idRole):
    try:
        cnx.execute(text("INSERT INTO ACHETEUR (mailAcheteur, mdp, nom, prenom, idRoleAcheteur) VALUES ('"+email+"', '"+mdp+"', '"+nom+"', '"+prenom+"', '"+str(idRole)+"');"))
        cnx.commit()
        print("Ajout réussi")
    except:
        print("Erreur lors de la requête ajouter_spectateur")

def supprimer_spectateur(cnx, email):
    try:
        cnx.execute(text("DELETE FROM ACHETEUR WHERE mailAcheteur = '"+email+"';"))
        cnx.commit()
        print("Suppression réussie")
    except:
        print("Erreur lors de la requête supprimer_spectateur")

def modifier_spectateur(cnx, nom, prenom, email, mdp, idRole):
    try:
        cnx.execute(text("UPDATE ACHETEUR SET nom = '"+nom+"', prenom = '"+prenom+"', mdp = '"+mdp+"', idRoleAcheteur = '"+str(idRole)+"' WHERE mailAcheteur = '"+email+"';"))
        cnx.commit()
        print("Modification réussie")
    except:
        print("Erreur lors de la requête modifier_spectateur")

def get_groupe_artiste(cnx, idArtiste):
    try:
        liste = []
        res = cnx.execute(text("SELECT * FROM GROUPEARTISTE natural join GROUPE WHERE idArtiste = "+str(idArtiste)+";"))
        for row in res:
            liste.append(row)
        return liste[0]
    except:
        print("Erreur lors de la requête get_groupe_artiste")
        return []

def get_id_groupe(cnx, nomGroupe):
    try:
        liste = []
        res = cnx.execute(text("SELECT idGroupe FROM GROUPE WHERE nomGroupe = '"+nomGroupe+"';"))
        for row in res:
            liste.append(row)
        return liste[0][0]
    except:
        print("Erreur lors de la requête get_id_groupe")
        return []

def get_all_nom_style_musical(cnx):
    try:
        liste = []
        res = cnx.execute(text("SELECT nom FROM STYLEMUSICAL;"))
        for row in res:
            liste.append(row[0])
        return liste
    except:
        print("Erreur lors de la requête get_all_nom_style_musical")
        return []

def get_all_groupe_with_search(cnx, recherche):
    try:
        liste = []
        res = cnx.execute(text("SELECT idGroupe, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe, nomImage FROM GROUPE NATURAL JOIN PHOTOGROUPE WHERE nomGroupe LIKE '%"+recherche+"%' OR descGroupe LIKE '%"+recherche+"%';"))
        for row in res:
            liste.append(row)
        return liste
    except:
        print("Erreur lors de la requête get_all_groupe_with_search")
        return []

def modifier_groupe(cnx, nomGroupe, nbPersn, nomStyle, descGroupe, idGroupe):
    try:
        idStyle = get_id_style_musical(cnx, nomStyle)[0]
        print(idStyle)
        print(idGroupe)
        cnx.execute(text("UPDATE GROUPE SET nomGroupe = '"+nomGroupe+"', nbPersn = "+str(nbPersn)+", idStyle = "+str(idStyle)+", descGroupe = '"+descGroupe+"' WHERE idGroupe = "+str(idGroupe)+";"))
        print("Modification réussie")
    except:
        print("Erreur lors de la requête modifier_groupe")

def get_id_style_musical(cnx, nomStyle):
    try:
        liste = []
        res = cnx.execute(text("SELECT idStyle FROM STYLEMUSICAL WHERE nom = '"+nomStyle+"';"))
        for row in res:
            liste.append(row)
        return liste[0]
    except:
        print("Erreur lors de la requête get_id_style_musical")
        return []

def ajouter_groupe(cnx, nomGroupe, nbPersn, nomStyle, descGroupe):
    try:
        idStyle = get_id_style_musical(cnx, nomStyle)[0]
        cnx.execute(text("INSERT INTO GROUPE (nomGroupe, nbPersn, idStyle, descGroupe) VALUES ('"+nomGroupe+"', "+str(nbPersn)+", "+str(idStyle)+", '"+descGroupe+"');"))
        cnx.execute(text("INSERT INTO PHOTOGROUPE (idGroupe, nomImage) VALUES ((SELECT MAX(idGroupe) FROM GROUPE), 'default.jpg');"))
        cnx.commit()
        print("Ajout réussi")
    except:
        print("Erreur lors de la requête ajouter_groupe")

def delete_groupe(cnx, idGroupe):
    try:
        # cnx.execute(text("DELETE FROM ARTISTE WHERE idArtiste IN (SELECT idArtiste FROM GROUPEARTISTE WHERE idGroupe = "+str(idGroupe)+");"))
        cnx.execute(text("DELETE FROM PHOTOGROUPE WHERE idGroupe = "+str(idGroupe)+";"))
        print(text("DELETE FROM PHOTOGROUPE WHERE idGroupe = "+str(idGroupe)+";"))
        # cnx.execute(text("DELETE FROM FAVORIS WHERE idGroupe = "+str(idGroupe)+";"))
        # cnx.execute(text("DELETE FROM GROUPEARTISTE WHERE idGroupe = "+str(idGroupe)+";"))
        cnx.execute(text("DELETE FROM GROUPE WHERE idGroupe = "+str(idGroupe)+";"))
        print("DELETE FROM GROUPE WHERE idGroupe = "+str(idGroupe)+";")
        print("Suppression réussie")
    except:
        print("Erreur lors de la requête delete_groupe")

def get_all_name_hebergement(cnx):
    try:
        liste = []
        res = cnx.execute(text("SELECT nomHebergement FROM HEBERGEMENT;"))
        for row in res:
            liste.append(row[0])
        return liste
    except:
        print("Erreur lors de la requête get_all_name_hebergement")
        return []

def get_nbPlace_hebergement(cnx, nomHebergement):
    try:
        liste = []
        res = cnx.execute(text("SELECT nombreDePlaces FROM HEBERGEMENT WHERE nomHebergement = '"+nomHebergement+"';"))
        for row in res:
            liste.append(row)
        return liste[0][0]
    except:
        print("Erreur lors de la requête get_nbPlace_hebergement")
        return []

def insert_groupe_hebergement(cnx, idGroupe, idFestival, idHebergement, dateArrivee, dateDepart, tempsMontage, tempsDemontage):
    try:
        cnx.execute(text("INSERT INTO ORGANISATIONGROUPE (idGroupe, idFestival, idHebergement, dateArrivee, dateDepart, tempsMontage, tempsDemontage) VALUES ("+str(idGroupe)+", "+str(idFestival)+", '"+str(idHebergement)+", "+dateArrivee+"', '"+dateDepart+"', '"+tempsMontage+"', '"+tempsDemontage+"');"))
        cnx.commit()
        print("Ajout réussi")
    except:
        print("Erreur lors de la requête insert_groupe_hebergement")