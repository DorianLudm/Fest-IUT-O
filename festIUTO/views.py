from .app import app, csrf
from flask import render_template, url_for, redirect, request, session, jsonify, send_file
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField, IntegerField, BooleanField, RadioField
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
    nom = StringField('nom')
    prenom = StringField('prenom')
    email = StringField('email')
    adresse = StringField('adresse')
    codePostal = StringField('codePostal')
    ville = StringField('ville')
    pays = StringField('pays')
    tel = StringField('téléphone')
    numeroCarte = StringField('numéro de carte')
    dateCarte = DateField('date de validité')
    codeCarte = StringField('code de sécurité')
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
        return (nom, prenom, mail, mdp, confirmerMdp) # comment faire que sur un formulaire flaskForm seulement un booleanField soit cliquer a la fois

class SelectJourForm(FlaskForm):
    lundi = BooleanField('Lundi 17 mai', validators=[Optional()])
    mardi = BooleanField('Mardi 18 mai', validators=[Optional()])
    mercredi = BooleanField('Mercredi 19 mai', validators=[Optional()])
    jeudi = BooleanField('Jeudi 20 mai', validators=[Optional()])
    vendredi = BooleanField('Vendredi 21 mai', validators=[Optional()])
    samedi = BooleanField('Samedi 22 mai', validators=[Optional()])
    nombreBillet = IntegerField('Quantité de billets', validators=[DataRequired()])
    submit = SubmitField('Participer')

    def get_jour(self):
        return [self.lundi.data, self.mardi.data, self.mercredi.data, self.jeudi.data, self.vendredi.data, self.samedi.data, self.nombreBillet.data]

class RechercheForm(FlaskForm):
    recherche = StringField('recherche', validators=[DataRequired()])
    submit = SubmitField('Rechercher')

    def get_recherche(self):
        return self.recherche.data


def les_jours_sont_valide(liste_jours):
    if liste_jours.count(True) != 1:
        return False
    return True

def les_jours_sont_valide_2jours(liste_jours):
    if liste_jours.count(True) != 2:
        return False
    return True


@app.route('/')
def index():
        return render_template(
            "home.html",
            title="Festiut'O | Accueil",
        )

@app.route('/search', methods=("GET","POST",))
def search():
    f = RechercheForm()
    if f.validate_on_submit():
        recherche = f.get_recherche()
        contenu = recherche_groupe(cnx, recherche)
        contenu = contenu + recherche_creneau(cnx, recherche)
        contenu = contenu + [("3", "Billet", "lundi"), ("3", "Billet", "mardi"), ("3", "Billet", "mercredi"), ("3", "Billet", "jeudi"), ("3", "Billet", "vendredi"), ("3", "Billet", "samedi")]
        print(contenu)
        return render_template(
            "search.html",
            title="Festiut'O | Recherche",
            form=f,
            recherche=contenu
        )
    return render_template(
        "search.html",
        title="Festiut'O | Recherche",
        form=f,
    )

@app.route('/pass-1-jour', methods=("GET","POST",))
@csrf.exempt
def pass1jour():
    check = request.args.get('check')
    idBillet = request.args.get('idBillet')
    if idBillet != None:
        billet = get_billet(cnx, idBillet)
        print(billet)
    f = SelectJourForm()
    erreur = ""

    if idBillet != None:
        if billet[3] == datetime.date(2024, 5, 17):
            f.lundi.data = True
        elif billet[3] == datetime.date(2024, 5, 18):
            f.mardi.data = True
        elif billet[3] == datetime.date(2024, 5, 19):
            f.mercredi.data = True
        elif billet[3] == datetime.date(2024, 5, 20):
            f.jeudi.data = True
        elif billet[3] == datetime.date(2024, 5, 21):
            f.vendredi.data = True
        elif billet[3] == datetime.date(2024, 5, 22):
            f.samedi.data = True
    
    if check != None:
        if check == "lundi":
            f.lundi.data = True
        elif check == "mardi":
            f.mardi.data = True
        elif check == "mercredi":
            f.mercredi.data = True
        elif check == "jeudi":
            f.jeudi.data = True
        elif check == "vendredi":
            f.vendredi.data = True
        elif check == "samedi":
            f.samedi.data = True
        
    if f.validate_on_submit():
        jours = f.get_jour()
        nombreJour = jours[6]
        jours = jours[:5]
        if les_jours_sont_valide(jours) == True:
            print("test2")
            jour = f.get_jour()
            jourChoisit = ""
            if jour[0]:
                jourChoisit = "lundi"
            elif jour[1]:
                jourChoisit = "mardi"
            elif jour[2]:
                jourChoisit = "mercredi"
            elif jour[3]:
                jourChoisit = "jeudi"
            elif jour[4]:
                jourChoisit = "vendredi"
            elif jour[5]:
                jourChoisit = "samedi"
            return redirect("/payement?pass=1jour&jour="+jourChoisit+"&nbJour="+str(jour[6])+"")
        else:
            print("erreur")
            erreur = "Veuillez choisir seulement un jour"
    return render_template(
        "pass1jour.html",
        title="Festiut'O | Pass",
        form=f,
        erreur=erreur,
        idBillet=idBillet
    )

@app.route('/pass-2-jours', methods=("GET","POST",))
@csrf.exempt
def pass2jours():
    nbJour = request.args.get('nbJour')
    idBillet = request.args.get('idBillet')
    if idBillet != None:
        billet = get_billet(cnx, idBillet)
        print(billet)
    f = SelectJourForm()
    erreur = ""

    if idBillet != None:
        if billet[3] == datetime.date(2024, 5, 17) or billet[4] == datetime.date(2024, 5, 17):
            f.lundi.data = True
        elif billet[3] == datetime.date(2024, 5, 18) or billet[4] == datetime.date(2024, 5, 18):
            f.mardi.data = True
        elif billet[3] == datetime.date(2024, 5, 19) or billet[4] == datetime.date(2024, 5, 19):
            f.mercredi.data = True
        elif billet[3] == datetime.date(2024, 5, 20) or billet[4] == datetime.date(2024, 5, 20):
            f.jeudi.data = True
        elif billet[3] == datetime.date(2024, 5, 21) or billet[4] == datetime.date(2024, 5, 21):
            f.vendredi.data = True
        elif billet[3] == datetime.date(2024, 5, 22) or billet[4] == datetime.date(2024, 5, 22):
            f.samedi.data = True

    if f.validate_on_submit():
        jours = f.get_jour()
        nombreJour = jours[6]
        jours = jours[:6]
        if les_jours_sont_valide_2jours(jours) == True:
            jourChoisit = []
            if jours[0]:
                jourChoisit.append("lundi")
            if jours[1]:
                jourChoisit.append("mardi")
            if jours[2]:
                jourChoisit.append("mercredi")
            if jours[3]:
                jourChoisit.append("jeudi")
            if jours[4]:
                jourChoisit.append("vendredi")
            if jours[5]:
                jourChoisit.append("samedi")
            return redirect("/payement?pass=2jours&jour1="+jourChoisit[0]+"&jour2="+jourChoisit[1]+"&nbJour="+str(nombreJour)+"")
        else:
            print("erreur")
            erreur = "Veuillez choisir deux jours"
    
    if idBillet == None:
        idBillet = True
    else:
        idBillet = False
    return render_template(
        "pass2jours.html",
        title="Festiut'O | Pass",
        form=f,
        erreur=erreur,
        idBillet=idBillet
    )

@app.route('/pass-semaine', methods=("GET","POST",))
@csrf.exempt
def passSemaine():
    form = SelectJourForm()
    if form.validate_on_submit():
        jours = form.get_jour()
        return redirect("/payement?pass=semaine&nbJour="+str(jours[6])+"")
    return render_template(
        "passsemaine.html",
        title="Festiut'O | Pass",
        form=form
    )

@app.route('/pass-semaine-valid', methods=("GET","POST",))
@csrf.exempt
def passSemaineValid():
    create_billet(cnx, session['utilisateur'][2], "semaine", 3)
    return redirect(url_for('compte'))


@app.route('/artistes')
def artistes():
    if 'utilisateur' in session:
        artiste=get_groupe_non_favoris(session['utilisateur'][2])
        artiste_fav=get_groupe_favoris(session['utilisateur'][2])

        artistes_images={}
        for a in artiste:
            artistes_images[a[0]]="../static/img/" + a[6]

        artistes_images_fav={}
        for a in artiste_fav:
            artistes_images_fav[a[0]]="../static/img/" + a[7]
        
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
            yaQueDesFavoris=yaQueDesFavoris,
            artiste_images=artistes_images,
            artiste_images_favs = artistes_images_fav
        )  
    else:
        artiste=get_all_groupe()
        
        artistes_images={}
        for a in artiste:
            artistes_images[a[0]]="../static/img/" + a[6]

        return render_template(
            "artistes.html",
            title="Festiut'O | Artistes",
            artiste=get_all_groupe(),
            artiste_images=artistes_images
        )  
    
@app.route('/planning')
def planning():
    concertChoisit = request.args.get('concert')
    if concertChoisit != None:
        return render_template(
        "planning.html",
        title="Festiut'O | Planning",
        creneaux = get_creneaux(),
        pla = get_planning(),
        concertChoisit=concertChoisit
        )
    return render_template(
        "planning.html",
        title="Festiut'O | Planning",
        creneaux = get_creneaux(),
        pla = get_planning(),
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
        print("modif : "+str(session['utilisateur']))
        # modifForm.nom.data = session['utilisateur'][0]
        # modifForm.prenom.data = session['utilisateur'][1]
        # modifForm.mail.data = session['utilisateur'][2]
        # modifForm.mdp.data = get_password_with_email(cnx, session['utilisateur'][2])
        billets = get_billet_acheteur(cnx, session['utilisateur'][2])
        yaDesBillets = False
        if len(billets) > 0:
            yaDesBillets = True
        print(yaDesBillets)
        return render_template(
            "compte.html",
            title="Festiut'O | Compte",
            formConnexion=f,
            formModif = modifForm,
            formInscription=f2,
            billets = billets,
            yaDesBillets = yaDesBillets,
            ILundi = datetime.date(2024, 5, 17),
            IMardi = datetime.date(2024, 5, 18),
            IMercredi = datetime.date(2024, 5, 19),
            IJeudi = datetime.date(2024, 5, 20),
            IVendredi = datetime.date(2024, 5, 21),
            ISamedi = datetime.date(2024, 5, 22)
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
        formInscription=f2,
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
        Image="../static/img/" + get_image_groupe(id)[0],
        suggestions=get_artistes_avec_meme_style(cnx, id),
        favoris=artiste_favoris_acheteur(cnx, session['utilisateur'][2], id)
    )

@app.route("/ajouter-fav/<int:id>", methods=("GET",))
def ajouterFav(id):
    add_groupe_favoris(session['utilisateur'][2], id)
    return redirect(url_for('artistes'))

@app.route("/supprimer-fav/<int:id>", methods=("GET",))
def supprimerFav(id):
    delete_groupe_favoris(session['utilisateur'][2], id)
    return redirect(url_for('artistes'))

@app.route("/ajouter-favoris/<int:id>", methods=("GET",))
def ajouterFavoris(id):
    add_groupe_favoris(session['utilisateur'][2], id)
    return redirect(url_for('profilGroupe', id=id))

@app.route("/supprimer-favoris/<int:id>", methods=("GET",))
def supprimerFavoris(id):
    delete_groupe_favoris(session['utilisateur'][2], id)
    return redirect(url_for('profilGroupe', id=id))

@app.route("/logout/")
def logout():
    session.pop('utilisateur', None)
    return redirect(url_for('compte'))

@app.route('/payement', methods=("GET", "POST",))
@csrf.exempt
def payement():
    passe = request.args.get('pass')
    nbJour = request.args.get('nbJour')
    f = PayementForm()
   # if f.validate_on_submit():
    if passe == "1jour":
        jour = request.args.get('jour')
        match jour:
            case "lundi":
                jour = "2024-05-17"
            case "mardi":
                jour = "2024-05-18"
            case "mercredi":
                jour = "2024-05-19"
            case "jeudi":
                jour = "2024-05-20"
            case "vendredi":
                jour = "2024-05-21"
            case "samedi":
                jour = "2024-05-22"
        print(jour)
        for i in range(int(nbJour)):
            create_billet(cnx, session['utilisateur'][2], jour, 1)
    elif passe == "2jours":
        jour1 = request.args.get('jour1')
        jour2 = request.args.get('jour2')
        print(jour1)
        print(jour2)
        match jour1:
            case "lundi":
                jour1 = "2024-05-17"
            case "mardi":
                jour1 = "2024-05-18"
            case "mercredi":
                jour1 = "2024-05-19"
            case "jeudi":
                jour1 = "2024-05-20"
            case "vendredi":
                jour1 = "2024-05-21"
            case "samedi":
                jour1 = "2024-05-22"
        match jour2:
            case "lundi":
                jour2 = "2024-05-17"
            case "mardi":
                jour2 = "2024-05-18"
            case "mercredi":
                jour2 = "2024-05-19"
            case "jeudi":
                jour2 = "2024-05-20"
            case "vendredi":
                jour2 = "2024-05-21"
            case "samedi":
                jour2 = "2024-05-22"
        print(jour1)
        print(jour2)
        for i in range(int(nbJour)):
            create_billet(cnx, session['utilisateur'][2], jour1, 2, jour2)
    elif passe == "semaine":
        for i in range(int(nbJour)):
            create_billet(cnx, session['utilisateur'][2], "2024-05-17", 3)

    return redirect(url_for('compte'))
    
    return render_template(
            "payement.html",
            title="Festiut'O | Payement",
            passe=passe,
            formPayement=f
        )

@app.route("/delete-billet/<int:id>", methods=("GET",))
def deleteBillet(id):
    delete_billet(cnx, id)
    return redirect(url_for('compte'))