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

class ModifierGroupeForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    style = SelectField('style', choices=get_all_nom_style_musical(cnx), validators=[DataRequired()])
    nbPersn = IntegerField('nombre de personne', validators=[DataRequired()])
    descGroupe = StringField('description', validators=[DataRequired()])
    hebergement = SelectField('hebergement', choices=get_all_name_hebergement(cnx), validators=[DataRequired()])
    dateArrivee = DateField("date d'arrivée", validators=[DataRequired()])
    dateDepart = DateField("date de départ", validators=[DataRequired()])
    tempsMontage = IntegerField('temps de montage', validators=[DataRequired()])
    tempsDemontage = IntegerField('temps de démontage', validators=[DataRequired()])
    photo = FileField('photo')
    submit = SubmitField('Modifier')

    def get_modifier_groupe(self):
        return (self.nom.data, self.style.data, self.nbPersn.data, self.descGroupe.data, self.hebergement.data, self.dateArrivee.data, self.dateDepart.data, self.tempsMontage.data, self.tempsDemontage.data, self.photo.data)

class AjouterGroupeForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    style = SelectField('style', choices=get_all_nom_style_musical(cnx), validators=[DataRequired()])
    nbPersn = IntegerField('nombre de personne', validators=[DataRequired()])
    descGroupe = StringField('description', validators=[DataRequired()])
    hebergement = SelectField('hebergement', choices=get_all_name_hebergement(cnx) , validators=[DataRequired()])
    dateArrivee = DateField("date d'arrivée", validators=[DataRequired()])
    dateDepart = DateField("date de départ", validators=[DataRequired()])
    tempsMontage = IntegerField('temps de montage', validators=[DataRequired()])
    tempsDemontage = IntegerField('temps de démontage', validators=[DataRequired()])
    photo = FileField('photo')
    submit = SubmitField('Ajouter')

    def get_ajouter_groupe(self):
        return (self.nom.data, self.style.data, self.nbPersn.data, self.descGroupe.data, self.hebergement.data, self.dateArrivee.data, self.dateDepart.data, self.tempsMontage.data, self.tempsDemontage.data, self.photo.data)

class ModifierArtisteForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    groupe = SelectField('groupe', choices=get_all_nom_groupe(), validators=[DataRequired()])
    submit = SubmitField('Modifier')

    def get_modifier_artiste(self):
        return (self.nom.data, self.prenom.data, self.groupe.data)

class AjouterArtisteForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    groupe = SelectField('groupe', choices=get_all_nom_groupe(), validators=[DataRequired()])
    submit = SubmitField('Ajouter')

    def get_ajouter_artiste(self):
        return (self.nom.data, self.prenom.data, self.groupe.data)

class ModifierSpectateurForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    mail = StringField('email', validators=[DataRequired()])
    mdp = PasswordField('Password', validators=[DataRequired()])
    confirmerMdp = PasswordField('Confirmer Password', validators=[DataRequired()])
    role = SelectField('role', choices=[("2", "Spectateur"), ("1", "Admin")], validators=[DataRequired()])
    submit = SubmitField('Modifier')

    def get_modifier_spectateur(self):
        return (self.nom.data, self.prenom.data, self.mail.data, self.mdp.data, self.confirmerMdp.data, self.role.data)

class AjouterSpectateurForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    mail = StringField('email', validators=[DataRequired()])
    mdp = PasswordField('Password', validators=[DataRequired()])
    confirmerMdp = PasswordField('Confirmer Password', validators=[DataRequired()])
    role = SelectField('role', choices=[("2", "Spectateur"), ("1", "Admin")], validators=[DataRequired()])
    submit = SubmitField('Ajouter')

    def get_ajouter_spectateur(self):
        return (self.nom.data, self.prenom.data, self.mail.data, self.mdp.data, self.confirmerMdp.data, self.role.data)

class ModifierHebergementForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    nbPlace = IntegerField('nombre de place', validators=[DataRequired()])
    submit = SubmitField('Modifier')

    def get_modifier_hebergement(self):
        return (self.nom.data, self.nbPlace.data)

class AjouterHebergementForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    nbPlace = IntegerField('nombre de place', validators=[DataRequired()])
    submit = SubmitField('Ajouter')

    def get_ajouter_hebergement(self):
        return (self.nom.data, self.nbPlace.data)

class ModifierEvenementForm(FlaskForm):
    lieu = SelectField('lieu', choices=get_all_nom_lieu(cnx), validators=[DataRequired()])
    groupe = SelectField('groupe', choices=get_all_nom_groupe(), validators=[DataRequired()])
    typeEvent = SelectField('typeEvent', choices=get_all_type_evenement(), validators=[DataRequired()])
    dateDebut = DateField("date de début", validators=[DataRequired()])
    duree = IntegerField('durée', validators=[DataRequired()])
    descEvenement = StringField('description', validators=[DataRequired()])
    gratuit = BooleanField('gratuit', validators=[Optional()])
    submit = SubmitField('Modifier')

    def get_modifier_evenement(self):
        return (self.lieu.data, self.groupe.data, self.typeEvent.data, self.dateDebut.data, self.duree.data, self.descEvenement.data, self.gratuit.data)

class AjouterEvenementForm(FlaskForm):
    lieu = SelectField('lieu', choices=get_all_nom_lieu(cnx), validators=[DataRequired()])
    groupe = SelectField('groupe', choices=get_all_nom_groupe(), validators=[DataRequired()])
    typeEvent = SelectField('typeEvent', choices=get_all_type_evenement(), validators=[DataRequired()])
    dateDebut = DateField("date de début", validators=[DataRequired()])
    duree = IntegerField('durée', validators=[DataRequired()])
    descEvenement = StringField('description', validators=[DataRequired()])
    gratuit = BooleanField('gratuit', validators=[Optional()])
    submit = SubmitField('Ajouter')

    def get_ajouter_evenement(self):
        return (self.lieu.data, self.groupe.data, self.typeEvent.data, self.dateDebut.data, self.duree.data, self.descEvenement.data, self.gratuit.data)

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
    idBilletReprog = request.args.get('idBilletReprog')
    erreurRequest = request.args.get('erreur')
    idBilletConst = idBillet
    if idBillet != None:
        billet = get_billet(cnx, idBillet)
        print(billet)
    f = SelectJourForm()

    erreur = ""
    if erreurRequest != None:
        erreur = erreurRequest

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

            if idBilletReprog != None:
                print("idBilletReprog != None")
                if jourChoisit == "lundi":
                    jourChoisit = "2024-05-17"
                elif jourChoisit == "mardi":
                    jourChoisit = "2024-05-18"
                elif jourChoisit == "mercredi":
                    jourChoisit = "2024-05-19"
                elif jourChoisit == "jeudi":
                    jourChoisit = "2024-05-20"
                elif jourChoisit == "vendredi":
                    jourChoisit = "2024-05-21"
                elif jourChoisit == "samedi":
                    jourChoisit = "2024-05-22"
                print(jourChoisit)
                
                set_billet(cnx, idBilletReprog, jourChoisit)
                return redirect(url_for('compte'))

            return redirect("/payement?pass=1jour&jour="+jourChoisit+"&nbJour="+str(jour[6])+"")
        else:
            print("erreur")
            erreur = "Veuillez choisir seulement un jour"
            if idBilletReprog != None:
                return redirect('/pass-1-jour?idBillet='+str(idBilletReprog)+"&erreur=Veuillez choisir seulement un jour")

    if idBillet == None:
        idBillet = True
    else:
        idBillet = False
    return render_template(
        "pass1jour.html",
        title="Festiut'O | Pass",
        form=f,
        erreur=erreur,
        idBillet=idBillet,
        idBilletConst=idBilletConst
    )

@app.route('/pass-2-jours', methods=("GET","POST",))
@csrf.exempt
def pass2jours():
    nbJour = request.args.get('nbJour')
    idBillet = request.args.get('idBillet')
    idBilletReprog = request.args.get('idBilletReprog')
    erreurRequest = request.args.get('erreur')
    idBilletConst = idBillet

    if idBillet != None:
        billet = get_billet(cnx, idBillet)
        print(billet)
    f = SelectJourForm()
    
    erreur = ""
    if erreurRequest != None:
        erreur = erreurRequest

    if idBillet != None:
        if billet[3] == datetime.date(2024, 5, 17) or billet[4] == datetime.date(2024, 5, 17):
            f.lundi.data = True
        if billet[3] == datetime.date(2024, 5, 18) or billet[4] == datetime.date(2024, 5, 18):
            f.mardi.data = True
        if billet[3] == datetime.date(2024, 5, 19) or billet[4] == datetime.date(2024, 5, 19):
            f.mercredi.data = True
        if billet[3] == datetime.date(2024, 5, 20) or billet[4] == datetime.date(2024, 5, 20):
            f.jeudi.data = True
        if billet[3] == datetime.date(2024, 5, 21) or billet[4] == datetime.date(2024, 5, 21):
            f.vendredi.data = True
        if billet[3] == datetime.date(2024, 5, 22) or billet[4] == datetime.date(2024, 5, 22):
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
            
            if idBilletReprog != None:
                jourChoisit1 = ""
                jourChoisit2 = ""
                print("idBilletReprog != None")
                if jourChoisit[0] == "lundi":
                    jourChoisit1 = "2024-05-17"
                elif jourChoisit[0] == "mardi":
                    jourChoisit1 = "2024-05-18"
                elif jourChoisit[0] == "mercredi":
                    jourChoisit1 = "2024-05-19"
                elif jourChoisit[0] == "jeudi":
                    jourChoisit1 = "2024-05-20"
                elif jourChoisit[0] == "vendredi":
                    jourChoisit1 = "2024-05-21"
                elif jourChoisit[0] == "samedi":
                    jourChoisit1 = "2024-05-22"
                
                if jourChoisit[1] == "lundi":
                    jourChoisit2 = "2024-05-17"
                elif jourChoisit[1] == "mardi":
                    jourChoisit2 = "2024-05-18"
                elif jourChoisit[1] == "mercredi":
                    jourChoisit2 = "2024-05-19"
                elif jourChoisit[1] == "jeudi":
                    jourChoisit2 = "2024-05-20"
                elif jourChoisit[1] == "vendredi":
                    jourChoisit2 = "2024-05-21"
                elif jourChoisit[1] == "samedi":
                    jourChoisit2 = "2024-05-22"
                
                set_billet(cnx, idBilletReprog, jourChoisit1, jourChoisit2)
                return redirect(url_for('compte'))

            return redirect("/payement?pass=2jours&jour1="+jourChoisit[0]+"&jour2="+jourChoisit[1]+"&nbJour="+str(nombreJour)+"")
        else:
            print("erreur")
            erreur = "Veuillez choisir deux jours"
            if idBilletReprog != None:
                return redirect('/pass-2-jours?idBillet='+str(idBilletReprog)+"&erreur=Veuillez choisir deux jours")
    
    if idBillet == None:
        idBillet = True
    else:
        idBillet = False
    return render_template(
        "pass2jours.html",
        title="Festiut'O | Pass",
        form=f,
        erreur=erreur,
        idBillet=idBillet,
        idBilletConst=idBilletConst
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
        title="Festiut'O | ",
        articles = get_articles()
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
    redirect_url = request.args.get('redirect')
    Mail = request.args.get('mail')
    print(Mail)
    delete_billet(cnx, id)
    if redirect_url == "admin":
        return redirect(url_for('modifierSpectateur', mail=Mail))
    return redirect(url_for('compte'))

@app.route("/concert/<int:id>", methods=("GET",))
def concert(id):
    concertChoisit = get_concert(id)
    dateConcert = concertChoisit[4].strftime("%D")
    heureDebut = concertChoisit[4].strftime("%H:%M")
    return render_template(
        "concert.html",
        title="jsp",
        concert = concertChoisit,
        dateConcert = dateConcert,
        heureDebut = heureDebut,
        Image="../static/img/" + concertChoisit[-1]
    )
    


@app.route("/admin")
def admin():
    return render_template(
        "admin.html",
        title="Festiut'O | Admin",
    )

@app.route("/groupes-management", methods=("GET", "POST",))
def groupeManagement():
    form = RechercheForm()
    if form.validate_on_submit():
        recherche = form.get_recherche()
        if recherche != None:
            return render_template(
                "groupeManagement.html",
                title="Festiut'O | Admin",
                groupes=get_all_groupe_with_search(cnx, recherche),
                form=form
            )
    return render_template(
        "groupeManagement.html",
        title="Festiut'O | Admin",
        groupes=get_all_groupe(),
        form=form
    )

@app.route("/modifier-groupe/<int:id>", methods=("GET", "POST",))
def modifierGroupe(id):
    form = ModifierGroupeForm()
    if form.validate_on_submit():
        groupe = form.get_modifier_groupe()
        print(groupe)
        modifier_groupe(cnx, groupe[0], groupe[2], groupe[1], groupe[3], id)
        return redirect(url_for('modifierGroupe', id=id))
    return render_template(
        "modifierGroupe.html",
        title="Festiut'O | Admin",
        groupes=get_profil_groupe(id),
        form=form
    )

@app.route('/ajouter-groupe', methods=("GET", "POST",))
def ajouterGroupe():
    form = AjouterGroupeForm()
    if form.validate_on_submit():
        groupe = form.get_ajouter_groupe()
        #print(groupe)
        # Check if groupe[5] and groupe[6] are strings before conversion
        if isinstance(groupe[5], str):
            groupe[5] = datetime.strptime(groupe[5], '%Y-%m-%d')
        if isinstance(groupe[6], str):
            groupe[6] = datetime.strptime(groupe[6], '%Y-%m-%d')
        ajouter_groupe(cnx, groupe[0], groupe[2], groupe[1], groupe[3], groupe[4], groupe[5], groupe[6], groupe[7], groupe[8])
        print("date")
        print(groupe[6])
        return redirect(url_for('groupeManagement'))
   
    return render_template(
        "ajouterGroupe.html",
        title="Festiut'O | Admin",
        form=form
    )

@app.route('/supprimer-groupe/<int:id>', methods=("GET",))
def supprimerGroupe(id):
    delete_groupe(cnx, id)
    return redirect(url_for('groupeManagement'))

@app.route('/artistes-management', methods=("GET", "POST",))
def artistesManagement():
    print(get_all_artiste())
    form = RechercheForm()
    if form.validate_on_submit():
        recherche = form.get_recherche()
        if recherche != None:
            return render_template(
                "artisteManagement.html",
                title="Festiut'O | Admin",
                artistes=get_all_artistes_with_search(cnx, recherche),
                form=form
            )
    return render_template(
        "artisteManagement.html",
        title="Festiut'O | Admin",
        artistes=get_all_artiste(),
        form=form
    )

@app.route('/modifier-artiste/<int:id>', methods=("GET", "POST",))
def modifierArtiste(id):
    form = ModifierArtisteForm()
    groupeAssocie = get_groupe_artiste(cnx, id)
    if form.validate_on_submit():
        artiste = form.get_modifier_artiste()
        idGroupe = get_id_groupe(cnx, artiste[2])
        print(idGroupe)
        set_profil_artiste(cnx, id, artiste[0], artiste[1], idGroupe)
        return redirect(url_for('modifierArtiste', id=id))
    return render_template(
        "modifierArtiste.html",
        title="Festiut'O | Admin",
        artiste=get_profil_artiste(id),
        form=form,
        groupeAssocie=groupeAssocie
    )

@app.route('/ajouter-artiste', methods=("GET", "POST",))
def ajouterArtiste():
    form = AjouterArtisteForm()
    if form.validate_on_submit():
        artiste = form.get_ajouter_artiste()
        idGroupe = get_id_groupe(cnx, artiste[2])
        print(idGroupe)
        ajouter_artiste(cnx, artiste[0], artiste[1], idGroupe)
        return redirect(url_for('artistesManagement'))
   
    return render_template(
        "ajouterArtiste.html",
        title="Festiut'O | Admin",
        form=form
    )

@app.route('/supprimer-artiste/<int:id>', methods=("GET",))
def supprimerArtiste(id):
    supprimer_artiste(cnx, id)
    return redirect(url_for('artistesManagement'))

@app.route('/spectateurs-management', methods=("GET", "POST",))
def spectateurManagement():
    form = RechercheForm()
    if form.validate_on_submit():
        recherche = form.get_recherche()
        if recherche != None:
            return render_template(
                "spectateurManagement.html",
                title="Festiut'O | Admin",
                spectateurs=get_all_spectateur_with_search(cnx, recherche),
                form=form
            )
    return render_template(
        "spectateurManagement.html",
        title="Festiut'O | Admin",
        spectateurs=get_all_spectateur(),
        form=form
    )

@app.route('/modifier-spectateur/<string:mail>', methods=("GET", "POST",))
def modifierSpectateur(mail):
    form = ModifierSpectateurForm()
    billets = get_billet_acheteur(cnx, mail)
    yaDesBillets = False
    if billets != []:
        yaDesBillets = True
    print(yaDesBillets)
    print(billets)
    if form.validate_on_submit():
        spectateur = form.get_modifier_spectateur()
        print(spectateur)
        modifier_spectateur(cnx, spectateur[0], spectateur[1], spectateur[2], spectateur[3], spectateur[5])
        return redirect(url_for('modifierSpectateur', mail=mail))
    return render_template(
        "modifierSpectateur.html",
        title="Festiut'O | Admin",
        spectateur=get_profil_spectateur(cnx, mail),
        form=form,
        billets=billets,
        yaDesBillets=yaDesBillets
    )

@app.route('/supprimer-tous-les-billets/<string:mail>', methods=("GET",))
def supprimerTousLesBillets(mail):
    supprimer_all_billet_acheteur(cnx, mail)
    return redirect(url_for('modifierSpectateur', mail=mail))

@app.route('/ajouter-spectateur', methods=("GET", "POST",))
def ajouterSpectateur():
    form = AjouterSpectateurForm()
    if form.validate_on_submit():
        spectateur = form.get_ajouter_spectateur()
        if spectateur[3] == spectateur[4]:
            ajouter_spectateur(cnx, spectateur[0], spectateur[1], spectateur[2], spectateur[3], spectateur[5])
            return redirect(url_for('spectateurManagement'))
    return render_template(
        "ajouterSpectateur.html",
        title="Festiut'O | Admin",
        form=form
    )

@app.route('/supprimer-spectateur/<string:mail>', methods=("GET",))
def supprimerSpectateur(mail):
    supprimer_spectateur(cnx, mail)
    return redirect(url_for('spectateurManagement'))


@app.route('/hebergement-management', methods=("GET", "POST",))
def hebergementManagement():
    form = RechercheForm()
    if form.validate_on_submit():
        recherche = form.get_recherche()
        if recherche != None:
            return render_template(
                "hebergementManagement.html",
                title="Festiut'O | Admin",
                hebergements=get_all_hebergement_with_search(cnx, recherche),
                form=form
            )
    return render_template(
        "hebergementManagement.html",
        title="Festiut'O | Admin",
        hebergements=get_all_hebergement(),
        form=form
    )

@app.route('/modifier-hebergement/<int:id>', methods=("GET", "POST",))
def modifierHebergement(id):
    form = ModifierHebergementForm()
    if form.validate_on_submit():
        hebergement = form.get_modifier_hebergement()
        print(hebergement)
        modifier_hebergement(cnx, hebergement[0], hebergement[1], id)
        return redirect(url_for('modifierHebergement', id=id))
    return render_template(
        "modifierHebergement.html",
        title="Festiut'O | Admin",
        hebergement=get_profil_hebergement(id),
        form=form
    )

@app.route('/ajouter-hebergement', methods=("GET", "POST",))
def ajouterHebergement():
    form = AjouterHebergementForm()
    if form.validate_on_submit():
        hebergement = form.get_ajouter_hebergement()
        ajouter_hebergement(cnx, hebergement[0], hebergement[1])
        return redirect(url_for('hebergementManagement'))
    return render_template(
        "ajouterHebergement.html",
        title="Festiut'O | Admin",
        form=form
    )

@app.route('/supprimer-hebergement/<int:id>', methods=("GET",))
def supprimerHebergement(id):
    supprimer_hebergement(cnx, id)
    return redirect(url_for('hebergementManagement'))


# gerer les evenements
@app.route('/evenement-management', methods=("GET", "POST",))
def evenementManagement():
    form = RechercheForm()
    if form.validate_on_submit():
        recherche = form.get_recherche()
        if recherche != None:
            return render_template(
                "evenementManagement.html",
                title="Festiut'O | Admin",
                evenements=get_all_evenement_with_search(cnx, recherche),
                form=form
            )
    return render_template(
        "evenementManagement.html",
        title="Festiut'O | Admin",
        evenements=get_all_evenement(),
        form=form
    )

@app.route('/modifier-evenement/<int:id>', methods=("GET", "POST",))
def modifierEvenement(id):
    form = ModifierEvenementForm()
    if form.validate_on_submit():
        evenement = form.get_modifier_evenement()
        print(evenement)
        gratuit = False
        if evenement[6] == True:
            gratuit = True
        idGroupe = get_id_groupe(cnx, evenement[1])
        idLieu = get_id_lieu(cnx, evenement[0])
        modifier_evenement(cnx, idLieu, idGroupe, evenement[3], evenement[4], evenement[5], gratuit, id)
        return redirect(url_for('modifierEvenement', id=id))
    return render_template(
        "modifierEvenement.html",
        title="Festiut'O | Admin",
        evenement=get_profil_evenement(id),
        form=form
    )

@app.route('/ajouter-evenement', methods=("GET", "POST",))
def ajouterEvenement():
    form = AjouterEvenementForm()
    if form.validate_on_submit():
        evenement = form.get_ajouter_evenement()
        gratuit = False
        if evenement[5] == True:
            gratuit = True
        idGroupe = get_id_groupe(cnx, evenement[1])
        idLieu = get_id_lieu(cnx, evenement[0])
        print(evenement)
        if gratuit:
            ajouter_evenement(cnx, idLieu, idGroupe, evenement[3], evenement[4], evenement[5], 1)
        else:
            ajouter_evenement(cnx, idLieu, idGroupe, evenement[3], evenement[4], evenement[5], 0)
        return redirect(url_for('evenementManagement'))
    return render_template(
        "ajouterEvenement.html",
        title="Festiut'O | Admin",
        form=form
    )

