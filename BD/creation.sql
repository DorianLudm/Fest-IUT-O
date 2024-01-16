DROP TABLE IF EXISTS RECHERCHEBILLET;
DROP TABLE IF EXISTS PHOTOGROUPE ;
DROP TABLE IF EXISTS IMAGE;
DROP TABLE IF EXISTS FAVORIS;
DROP TABLE IF EXISTS BILLET;
DROP TABLE IF EXISTS TYPEBILLET;
DROP TABLE IF EXISTS PREINSCRIRE;
DROP TABLE IF EXISTS RESEAUXGROUPE;
DROP TABLE IF EXISTS GROUPEARTISTE;
DROP TABLE IF EXISTS CRENEAU;
DROP TABLE IF EXISTS EVENTTYPE;
DROP TABLE IF EXISTS ORGANISATIONGROUPE;
DROP TABLE IF EXISTS JOUEINSTRUMENT;
DROP TABLE IF EXISTS INSTRUMENT ;
DROP TABLE IF EXISTS ARTISTE ;
DROP TABLE IF EXISTS GROUPE;
DROP TABLE IF EXISTS ACHETEUR;
DROP TABLE IF EXISTS ROLEACHETEUR;
DROP TABLE IF EXISTS RESEAUXSOCIAUX ;
DROP TABLE IF EXISTS LIAISONMUSICALE;
DROP TABLE IF EXISTS STYLEMUSICAL;
DROP TABLE IF EXISTS HEBERGEMENT;
DROP TABLE IF EXISTS LIEUSDUFESTIVAL;
DROP TABLE IF EXISTS LIEU;
DROP TABLE IF EXISTS BILLETSPARJOUR;
DROP TABLE IF EXISTS FESTIVAL;
DROP TABLE IF EXISTS RECHERCHEBILLET;

CREATE TABLE FESTIVAL(
    idFestival int NOT NULL auto_increment,
    nomFestival varchar(30) NOT NULL,
    dateDebutFestival datetime NOT NULL check((HOUR(dateDebutFestival) between 14 and 23 or HOUR(dateDebutFestival) between 0 and 4) AND dateFinFestival > dateDebutFestival and (day(dateDebutFestival)+1) <= day(dateFinFestival)),
    dateFinFestival datetime NOT NULL check((HOUR(dateFinFestival) between 14 and 23 or (HOUR(dateFinFestival) between 0 and 4) AND dateFinFestival > dateDebutFestival and (day(dateDebutFestival)+1) <= day(dateFinFestival))),
    PRIMARY KEY(idFestival)
);

CREATE TABLE BILLETSPARJOUR(
    idFestival int NOT NULL REFERENCES FESTIVAL,
    jour int NOT NULL check(jour between 1 and 31),
    nombreBillets int NOT NULL,
    PRIMARY KEY(idFestival, jour)
);

CREATE TABLE LIEU(
    idLieu int NOT NULL auto_increment,
    nomLieu varchar(30) NOT NULL ,
    adresse varchar(255) NOT NULL ,
    disponibiliteLieu boolean NOT NULL,
    nbPlacesLieu int NOT NULL,
    PRIMARY KEY(idLieu)
);

CREATE TABLE LIEUSDUFESTIVAL(
    idLieu int NOT NULL REFERENCES LIEU,
    idFestival int NOT NULL REFERENCES FESTIVAL,
    PRIMARY KEY(idLieu, idFestival)
);

CREATE TABLE HEBERGEMENT(
    idHebergement int NOT NULL auto_increment,
    nombreDePlaces int NOT NULL check(nombreDePlaces > 0),
    nomHebergement varchar(30) NOT NULL,
    PRIMARY KEY(idHebergement)
);

CREATE TABLE STYLEMUSICAL(
    idStyle int NOT NULL auto_increment,
    nom varchar(30) NOT NULL ,
    description varchar(255) NOT NULL ,
    PRIMARY KEY(idStyle),
    UNIQUE(nom)
);

CREATE TABLE LIAISONMUSICALE(
    idStyle1 int NOT NULL,
    idStyle2 int NOT NULL CHECK(idStyle1 != idStyle2 ),
    PRIMARY KEY(idStyle1, idStyle2)
);

CREATE TABLE RESEAUXSOCIAUX(
    idReseau int NOT NULL auto_increment,
    nomReseau varchar(30) NOT NULL ,
    UNIQUE(nomReseau),
    PRIMARY KEY(idReseau, nomReseau)
);

CREATE TABLE INSTRUMENT(
    idInstrument int NOT NULL auto_increment,
    nomInstrument varchar(30),
    UNIQUE(nomInstrument),
    PRIMARY KEY(idInstrument)
);

CREATE TABLE ARTISTE(
    idArtiste int NOT NULL auto_increment,
    nomArtiste varchar(30) NOT NULL,
    prenomArtiste varchar(30) NOT NULL,
    PRIMARY KEY (idArtiste)
);

CREATE TABLE JOUEINSTRUMENT(
    idArtiste int NOT NULL REFERENCES ARTISTE,
    idInstrument int NOT NULL REFERENCES INSTRUMENT,
    PRIMARY KEY(idArtiste, idInstrument)
);

CREATE TABLE GROUPE(
    idGroupe int NOT NULL auto_increment,
    nomGroupe varchar(30) NOT NULL ,
    nbPersn int NOT NULL check(nbPersn > 0),
    idStyle int NOT NULL REFERENCES STYLEMUSICAL,
    descGroupe varchar(1500) NOT NULL ,
    videoGroupe varchar(150) NOT NULL ,
    PRIMARY KEY(idGroupe)
);

CREATE TABLE GROUPEARTISTE(
    idGroupe int NOT NULL REFERENCES GROUPE,
    idArtiste int NOT NULL REFERENCES ARTISTE,
    PRIMARY KEY (idGroupe, idArtiste)
);

CREATE TABLE RESEAUXGROUPE(
    idReseau int NOT NULL REFERENCES RESEAUXSOCIAUX,
    idGroupe int NOT NULL REFERENCES GROUPE,
    lienReseau varchar(255) NOT NULL,
    PRIMARY KEY(idReseau, idGroupe)
);

CREATE TABLE ORGANISATIONGROUPE(
    idGroupe int NOT NULL REFERENCES GROUPE,
    idFestival int NOT NULL REFERENCES FESTIVAL,
    idHebergement int NOT NULL REFERENCES HEBERGEMENT,
    arrivee datetime NOT NULL check (arrivee < depart),
    depart datetime NOT NULL check (arrivee < depart),
    tempsMontage time NOT NULL,
    tempsDemontage time NOT NULL,
    PRIMARY KEY(idGroupe, idFestival)
);

CREATE TABLE EVENTTYPE(
    idEvent int NOT NULL auto_increment,
    nom varchar(300) NOT NULL,
    UNIQUE(nom),
    PRIMARY KEY(idEvent)
);

CREATE TABLE CRENEAU(
    idCreneau int NOT NULL auto_increment,
    idLieu int NOT NULL REFERENCES LIEU,
    idGroupe int NOT NULL REFERENCES GROUPE,
    idEvent int NOT NULL REFERENCES EVENTTYPE,
    heureDebut datetime NOT NULL check(HOUR(heureDebut) between 4 and 14),
    duree TIME NOT NULL,
    descriptionEvenement varchar(255) NOT NULL,
    preinscriptionPossible boolean NOT NULL,
    gratuit boolean NOT NULL,
    visibleAuPublic boolean NOT NULL,
    PRIMARY KEY(idCreneau)
);

CREATE TABLE ROLEACHETEUR(
    idRoleAcheteur int NOT NULL auto_increment,
    nomRoleAcheteur varchar(30) NOT NULL,
    UNIQUE(nomRoleAcheteur),
    PRIMARY KEY(idRoleAcheteur)
);

CREATE TABLE ACHETEUR(
    mailAcheteur varchar(100) NOT NULL,
    prenom varchar(30) NOT NULL,
    nom varchar(30) NOT NULL,
    mdp varchar(30) NOT NULL,
    idRoleAcheteur int NOT NULL REFERENCES ROLEACHETEUR,
    PRIMARY KEY(mailAcheteur)
);

CREATE TABLE PREINSCRIRE(
    idCreneau int NOT NULL REFERENCES CRENEAU, 
    mailAcheteur varchar(100) NOT NULL REFERENCES ACHETEUR,
    PRIMARY KEY(idCreneau, mailAcheteur)
);

CREATE TABLE TYPEBILLET(
    idType int NOT NULL auto_increment,
    dureeEnJours int NOT NULL,
    prix float NOT NULL,
    PRIMARY KEY(idType)
);

CREATE TABLE BILLET(
    idBillet int NOT NULL auto_increment,
    idFestival int NOT NULL REFERENCES FESTIVAL,
    mailAcheteur varchar(100) NOT NULL REFERENCES ACHETEUR,
    jourdebut date NOT NULL ,
    jourDeux date,
    idType int NOT NULL REFERENCES TYPEBILLET,
    PRIMARY KEY(idBillet)
);

CREATE TABLE FAVORIS(
    mailAcheteur varchar(100) NOT NULL REFERENCES ACHETEUR,
    idGroupe int NOT NULL REFERENCES GROUPE,
    PRIMARY KEY(mailAcheteur, idGroupe)
);

CREATE TABLE PHOTOGROUPE(
    idImage int NOT NULL auto_increment,
    idGroupe int NOT NULL REFERENCES GROUPE,
    nomImage varchar(800) NOT NULL,
    PRIMARY KEY(idImage)
);

CREATE TABLE RECHERCHEBILLET(
    idRechercheBillet int NOT NULL auto_increment,
    idType int NOT NULL REFERENCES TYPEBILLET,
    jourUn datetime,
    jourDeux datetime,
    PRIMARY KEY(idRechercheBillet)
)
