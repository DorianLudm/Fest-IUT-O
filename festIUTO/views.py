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

    # def get_authenticated_user(self):
    #     user = get_nom_and_email(cnx, self.email.data)
    #     print(user)
    #     mdp = get_password_with_email(cnx, self.email.data)
    #     if user is None:
    #         return None
    #     passwd = hasher_mdp(self.password.data)
    #     print(str(mdp)+" == "+str(passwd))
    #     return user if passwd == mdp else None


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


@app.route("/login/", methods=("GET","POST",))
def login():
    f = LoginForm ()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user != None:
            #login_user(user)
            session['utilisateur'] = user
            print("login : "+str(session['utilisateur']))
            next = f.next.data or url_for("base")
            return redirect(next)
    return render_template(
        "login.html",
        title="Profil",
        form=f,
        )


@app.route("/logout/")
def logout():
    session.pop('utilisateur', None)
    return redirect(url_for('base'))



@app.route('/programmation')
def programmation():
    # cursor = DATABASE.cursor()

    # if 'user_id' in session:
    #     user_id = session['user_id'][0]['idAcheteur']
    #     cursor_username = DATABASE.cursor(dictionary=True)
    #     cursor_username.execute("SELECT NOM FROM ACHETEUR WHERE idAcheteur = "+str(user_id))
    #     username_id = cursor_username.fetchall()
    #     username = username_id[0]['NOM']
        
    #     curso_artiste_fav = DATABASE.cursor(dictionary=True)
    #     curso_artiste_fav.execute("SELECT * FROM FAVORIS NATURAL JOIN ARTISTE WHERE idAcheteur="+str(session['user_id'][0]['idAcheteur']))
    #     artiste_fav = curso_artiste_fav.fetchall()

    #     curso_artiste = DATABASE.cursor(dictionary=True)
    #     curso_artiste.execute("SELECT * FROM ARTISTE WHERE idArtiste not IN (SELECT idArtiste FROM FAVORIS NATURAL JOIN ARTISTE WHERE idAcheteur = "+str(session['user_id'][0]['idAcheteur'])+");")
    #     artiste = curso_artiste.fetchall()

    #     cursor.close()

    #     return render_template(
    #         "programmation.html", 
    #         title="Festiut'O | Programmation", 
    #         artiste=artiste,
    #         artiste_fav=artiste_fav,
    #         username=username
    #     )
    # else:
    #     # Gérez le cas où l'ID de l'utilisateur n'est pas présent dans la session
    #     curso_artiste_fav = DATABASE.cursor(dictionary=True)
    #     curso_artiste_fav.execute("SELECT * FROM FAVORIS NATURAL JOIN ARTISTE WHERE idAcheteur="+str(idAcheteur))
    #     artiste_fav = curso_artiste_fav.fetchall()

    #     curso_artiste = DATABASE.cursor(dictionary=True)
    #     curso_artiste.execute("SELECT * FROM ARTISTE WHERE idArtiste not IN (SELECT idArtiste FROM FAVORIS NATURAL JOIN ARTISTE WHERE idAcheteur = "+str(idAcheteur)+");")
    #     artiste = curso_artiste.fetchall()

    #     cursor.close()
        mail = 'dup@gmail.com'
        return render_template(
            "programmation.html", 
            title="Festiut'O | Programmation", 
            artiste=get_groupe_non_favoris(mail),
            artiste_fav=get_groupe_favoris(mail)
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

@app.route('/compte')
def compte():

    # if 'user_id' in session:
    #     user_id = session['user_id'][0]['idAcheteur']
    #     cursor_username = DATABASE.cursor(dictionary=True)
    #     cursor_username.execute("SELECT NOM FROM ACHETEUR WHERE idAcheteur = "+str(user_id))
    #     username_id = cursor_username.fetchall()
    #     username = username_id[0]['NOM']
        
    #     return render_template(
    #         "compte.html",
    #         title="Festiut'O | Compte",
    #         username=username,
    #         user_id=user_id
    #     )
    # else:
        # Gérez le cas où l'ID de l'utilisateur n'est pas présent dans la session
        return render_template(
            "compte.html",
            title="Festiut'O | Compte",
        )

    

@app.route('/contact')
def contact():
    return render_template("contact.html",
                           title="Festiut'O | Contact"
                           )

@app.route('/profilArtiste/<string:id>', methods=['GET'])
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

@app.route('/connexion', methods=["GET", "POST"])
def connexion():
    # cursor = DATABASE.cursor()

    # if request.method == "POST":
    #     try:
    #         # Récupérez les données du formulaire
    #         username = request.form["username"]
    #         password = "'"+request.form["password"]+"'"

    #         cursor_mdp = DATABASE.cursor(dictionary=True)
    #         cursor_mdp.execute("SELECT mdp FROM ACHETEUR where nom = "+"'"+username+"'")
    #         mdp = cursor_mdp.fetchall()

    #         cursor_id = DATABASE.cursor(dictionary=True)
    #         cursor_id.execute("SELECT idAcheteur FROM ACHETEUR where nom = "+"'"+username+"'")
    #         id_acheteur = cursor_id.fetchall()
    #         print(id_acheteur)

    #         # Vérifiez les informations d'authentification
    #         if "'"+mdp[0]['mdp']+"'" == password:
    #             # Authentification réussie
    #             # Après avoir vérifié les informations d'identification de l'utilisateur avec la base de données
    #             session['user_id'] = id_acheteur  # Stockez l'ID de l'utilisateur dans la session
    #             print("Authentification réussie. Vous êtes connecté.")
    #             return redirect('compte')
    #         else:
    #             # Authentification échouée
    #             print("'"+mdp[0]['mdp']+"'"+"  !=  "+password)
    #             print("Nom d'utilisateur ou mot de passe incorrect.")
    #     except:
    #         print("erreur")
    
    # cursor.close()
    pass

@app.route('/deconnexion')
def deconnexion():
    # session.pop('user_id', None)
    return redirect('compte')