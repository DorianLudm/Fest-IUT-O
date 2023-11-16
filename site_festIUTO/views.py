from .app import app 
from flask import render_template, url_for, redirect, request, session, jsonify, send_file
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Optional
from wtforms import PasswordField
from hashlib import sha256
from .models import *
import time
import datetime
from .requette import *

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    next = HiddenField()

    def get_authenticated_user(self):
        print(self.email.data)
        print(self.password.data)

        user = get_nom_and_email(cnx, self.email.data)
        mdp = get_password_with_email(cnx, self.email.data)
        passwd = self.password.data
        print(user)
        return user if passwd == mdp else None


        # mdp = get_password_with_email(cnx, self.email.data)
        # if user is None:
        #     return None
        # passwd = hasher_mdp(self.password.data)
        # print(str(mdp)+" == "+str(passwd))
        # return user if passwd == mdp else None

class InscriptionForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    next = HiddenField()

    def get_inscription_user(self):
        email = self.email.data
        mdp = self.password.data
        nom = self.nom.data
        prenom = self.prenom.data
        # passwd = self.password.data
        return (email, mdp, nom, prenom)




@app.route('/')
def index():
    # cursor = DATABASE.cursor()

    # if 'user_id' in session:
    #     user_id = session['user_id'][0]['idAcheteur']
    #     cursor_username = DATABASE.cursor(dictionary=True)
    #     cursor_username.execute("SELECT NOM FROM ACHETEUR WHERE idAcheteur = "+str(user_id))
    #     username_id = cursor_username.fetchall()
    #     username = username_id[0]['NOM']
        
    #     cursor_concert = DATABASE.cursor(dictionary=True)
    #     # Exécutez une requête SQL pour récupérer des données de la table
    #     cursor_concert.execute("SELECT * FROM CONCERT")
    #     # Récupérez toutes les lignes de résultats dans une liste
    #     concert = cursor_concert.fetchall()
    #     # Fermez le curseur et la connexion à la base de données
    #     cursor.close()
    #     return render_template(
    #         "home.html",
    #         title="Festiut'O | Accueil",
    #         concert=concert,  # Passez les données récupérées à votre modèle HTML
    #         username=username
    #     )
    # else:
    #     cursor_concert = DATABASE.cursor(dictionary=True)
    #     # Exécutez une requête SQL pour récupérer des données de la table
    #     cursor_concert.execute("SELECT * FROM CONCERT")
    #     # Récupérez toutes les lignes de résultats dans une liste
    #     concert = cursor_concert.fetchall()
    #     # Fermez le curseur et la connexion à la base de données
    #     cursor.close()
        return render_template(
            "home.html",
            title="Festiut'O | Accueil",
        )


@app.route('/programmation')
def programmation():
    if 'utilisateur' in session:
        artiste_fav=get_groupe_favoris(session['utilisateur'][2])
        yaFavoris=False
        if len(artiste_fav) > 0:
            yaFavoris=True
        return render_template(
            "programmation.html", 
            title="Festiut'O | Programmation", 
            artiste=get_groupe_non_favoris(session['utilisateur'][2]),
            artiste_fav=artiste_fav,
            yaFavoris=yaFavoris
        )  
    else:
        return render_template(
            "programmation.html",
            title="Festiut'O | Programmation",
            artiste=get_all_groupe(),
        )  
    

@app.route('/condition-de-service')
def conditionDeService():
    return render_template("cds.html",
                           title="Festiut'O | Condition de service"
                           )

@app.route('/politique-de-confidentialite')
def politiqueDeConfidentialite():
    return render_template("pdc.html",
                           title="Festiut'O | Politique de confidentialité"
                           )

@app.route('/politique-de-remboursement')
def politiqueDeRemboursement():
    return render_template("pdr.html",
                           title="Festiut'O | Politique de remboursement"
                           )

@app.route('/compte', methods=("GET","POST",))
def compte():
    f = LoginForm()
    f2 = InscriptionForm()
    # inscription
    if f2.validate_on_submit():
        acheteur = f2.get_inscription_user()
        inscription_acheteur(cnx, acheteur[0], acheteur[1], acheteur[2], acheteur[3])
        return redirect(url_for('compte'))
    # connexion
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user != None:
            #login_user(user)
            session['utilisateur'] = user
            print("login : "+str(session['utilisateur']))
            return redirect(url_for('index'))
    return render_template(
        "compte.html",
        title="Festiut'O | Compte",
        formConnexion=f,
        formInscription=f2
        )

    

@app.route('/contact')
def contact():
    return render_template("contact.html",
                           title="Festiut'O | Contact"
                           )

@app.route('/profilArtiste/<string:id>', methods=("GET",))
def profilArtiste(id):
    # cursor = DATABASE.cursor()

    # cursor_Groupe = DATABASE.cursor(dictionary=True)
    # cursor_Groupe.execute("SELECT * FROM ARTISTE natural join STYLEMUSICAL WHERE idArtiste = "+str(id))
    # Groupe = cursor_Groupe.fetchall()

    # idGroupe = Groupe[0]['idArtiste']
    # nomGroupe = Groupe[0]['nomGroupe']
    # descArtiste = Groupe[0]['descArtiste']
    
    # cursor_styleMusical = DATABASE.cursor(dictionary=True)
    # cursor_styleMusical.execute("SELECT * FROM STYLEMUSICAL WHERE idStyle = "+str(Groupe[0]['idStyle']))
    # styleMusical = cursor_styleMusical.fetchall()

    # nomStyle = styleMusical[0]['nom']

    # cursor.close()
    return render_template(
        "profilArtiste.html",
        title="Festiut'O | profilArtiste",
        # Groupe=Groupe,
        # nomGroupe=nomGroupe,
        # idGroupe=idGroupe,
        # descArtiste=descArtiste,
        # nomStyle=nomStyle
    )

@app.route('/ajouter_donnees', methods=['POST'])
def ajouter_donnees():
    # cursor = DATABASE.cursor()

    # username = request.form["username"]
    # nom = request.form["nom"]
    # prenom = request.form["prenom"]
    # mdp = request.form["password"]

    # cursor_max = DATABASE.cursor(dictionary=True)
    # cursor_max.execute("SELECT max(idAcheteur) FROM ACHETEUR")
    # id_max = cursor_max.fetchall()

    # id_maximum = int(id_max[0]['max(idAcheteur)'])+1

    # # Exemple de requête d'insertion
    # query = "INSERT INTO ACHETEUR (idAcheteur, nom, prenom, mdp) VALUES (%s, %s, %s, %s)"

    # # Exécutez la requête avec les données fournies
    # cursor.execute(query, (str(id_maximum), nom, prenom, mdp))

    # # Committez les changements dans la base de données
    # DATABASE.commit()

    # cursor.close()

    return redirect('/')




@app.route("/logout/")
def logout():
    # print(session['utilisateur'])
    session.pop('utilisateur', None)
    return redirect(url_for('compte'))