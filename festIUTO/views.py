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

class PayementForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    adresse = StringField('adresse', validators=[DataRequired()])
    codePostal = StringField('codePostal', validators=[DataRequired()])
    ville = StringField('ville', validators=[DataRequired()])
    pays = StringField('pays', validators=[DataRequired()])
    tel = StringField('téléphone', validators=[DataRequired()])
    numeroCarte = StringField('numéro de carte', validators=[DataRequired()])
    dateCarte = DateField('date de validité', validators=[DataRequired()])
    codeCarte = StringField('code de sécurité', validators=[DataRequired()])
    next = HiddenField()

    def get_payement_user(self):
        email = self.email.data
        nom = self.nom.data
        prenom = self.prenom.data
        adresse = self.adresse.data
        codePostal = self.codePostal.data
        ville = self.ville.data
        pays = self.pays.data
        tel = self.tel.data
        numeroCarte = self.numeroCarte.data
        dateCarte = self.dateCarte.data
        codeCarte = self.codeCarte.data
        return (email, nom, prenom, adresse, codePostal, ville, pays, tel, numeroCarte, dateCarte, codeCarte)

class ModifierForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    mail = StringField('email', validators=[DataRequired()])
    mdp = PasswordField('Password', validators=[DataRequired()])
    confirmerMdp = PasswordField('Confirmer Password', validators=[DataRequired()])

    def get_modifier_user(self):
        nom = self.nom.data
        prenom = self.prenom.data
        mail = self.mail.data
        mdp = self.mdp.data
        confirmerMdp = self.confirmerMdp.data
        return (nom, prenom, mail, mdp, confirmerMdp)


@app.route('/')
def index():
        return render_template(
            "home.html",
            title="Festiut'O | Accueil",
        )

@app.route('/pass-1-jour')
def pass1jour():
    return render_template(
        "pass1jour.html",
        title="Festiut'O | Pass",
    )

@app.route('/pass-2-jours')
def pass2jours():
    return render_template(
        "pass2jours.html",
        title="Festiut'O | Pass",
    )

@app.route('/pass-semaine')
def passSemaine():
    return render_template(
        "passsemaine.html",
        title="Festiut'O | Pass",
    )


@app.route('/artistes')
def artistes():
    if 'utilisateur' in session:
        artiste=get_groupe_non_favoris(session['utilisateur'][2])
        artiste_fav=get_groupe_favoris(session['utilisateur'][2])
        yaQueDesFavoris=False
        yaFavoris=False
        if len(artiste_fav) > 0:
            yaFavoris=True
        if len(artiste) == 0:
            yaQueDesFavoris=True
        return render_template(
            "artistes.html", 
            title="Festiut'O | Artistes", 
            artiste=artiste,
            artiste_fav=artiste_fav,
            yaFavoris=yaFavoris,
            yaQueDesFavoris=yaQueDesFavoris
        )  
    else:
        return render_template(
            "artistes.html",
            title="Festiut'O | Artistes",
            artiste=get_all_groupe(),
        )  
    
@app.route('/planning')
def planning():
    return render_template(
        "planning.html",
        title="Festiut'O | Planning",
    )

@app.route('/billeterie')
def billeterie():
    return render_template(
        "billeterie.html",
        title="Festiut'O | Billeterie",
    )

@app.route('/boutique')
def boutique():
    return render_template(
        "boutique.html",
        title="Festiut'O | Boutique"
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
    modifForm = ModifierForm()
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
    if 'utilisateur' in session:
        # modifForm.nom.data = session['utilisateur'][0]
        # modifForm.prenom.data = session['utilisateur'][1]
        # modifForm.mail.data = session['utilisateur'][2]
        # modifForm.mdp.data = get_password_with_email(cnx, session['utilisateur'][2])
        render_template(
            "compte.html",
            title="Festiut'O | Compte",
            formConnexion=f,
            formModif = modifForm,
            formInscription=f2,
        )
    if modifForm.validate_on_submit():
        modif = modifForm.get_modifier_user()
        if modif[3] == modif[4]:
            print("modif : "+str(modif))
            modifier_acheteur(cnx, modif[0], modif[1], modif[2], modif[3])
            session.pop('utilisateur', None)
            session['utilisateur'] = get_nom_and_email(cnx, modif[2])
            return redirect(url_for('compte'))
        print("mdp non identique")
    return render_template(
        "compte.html",
        title="Festiut'O | Compte",
        formConnexion=f,
        formModif = modifForm,
        formInscription=f2
        )

    

@app.route('/contact')
def contact():
    return render_template("contact.html",
                           title="Festiut'O | Contact"
                           )

@app.route('/profilGroupe/<int:id>', methods=("GET",))
def profilGroupe(id):
    print(get_profil_groupe(id))
    return render_template(
        "profilGroupe.html",
        title="Festiut'O | profilGroupe",
        Groupe=get_profil_groupe(id),
        # nomGroupe=nomGroupe,
        # idGroupe=idGroupe,
        # descArtiste=descArtiste,
        # nomStyle=nomStyle
    )

@app.route("/ajouter-fav/<int:id>", methods=("GET",))
def ajouterFav(id):
    add_groupe_favoris(session['utilisateur'][2], id)
    return redirect(url_for('artistes'))

@app.route("/supprimer-fav/<int:id>", methods=("GET",))
def supprimerFav(id):
    delete_groupe_favoris(session['utilisateur'][2], id)
    return redirect(url_for('artistes'))

@app.route("/logout/")
def logout():
    session.pop('utilisateur', None)
    return redirect(url_for('compte'))

@app.route('/payement', methods=("GET", "POST",))
def payement():
    passe = request.args.get('pass')
    f = PayementForm()
    return render_template(
            "payement.html",
            title="Festiut'O | Payement",
            passe=passe,
            formPayement=f
        )