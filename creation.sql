CREATE TABLE FESTIVAL(
    idFestival int NOT NULL,
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
    idLieu int NOT NULL,
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
    idHebergement int NOT NULL ,
    nombreDePlaces int NOT NULL check(nombreDePlaces > 0),
    nomHebergement varchar(30) NOT NULL,
    PRIMARY KEY(idHebergement)
);

CREATE TABLE STYLEMUSICAL(
    idStyle int NOT NULL,
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
    idReseau int NOT NULL ,
    nomReseau varchar(30) NOT NULL ,
    UNIQUE(nomReseau),
    PRIMARY KEY(idReseau, nomReseau)
);

CREATE TABLE INSTRUMENT(
    idInstrument int NOT NULL,
    nomInstrument varchar(30),
    UNIQUE(nomInstrument),
    PRIMARY KEY(idInstrument)
);

CREATE TABLE ARTISTE(
    idArtiste int NOT NULL,
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
    idGroupe int NOT NULL,
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

--idHebergement int NOT NULL REFERENCES HEBERGEMENT check (placesdisponibles(idHebergement, idGroupe) > 0),
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

--reprise ici

CREATE TABLE EVENTTYPE(
    idEvent int NOT NULL,
    nom varchar(300) NOT NULL,
    UNIQUE(nom),
    PRIMARY KEY(idEvent)
);

CREATE TABLE CRENEAU(
    idCreneau int NOT NULL,
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

--faire une fonction sur la duree/heure..

CREATE TABLE ACHETEUR(
    mailAcheteur varchar(100) NOT NULL,
    prenom varchar(30) NOT NULL,
    nom varchar(30) NOT NULL,
    mdp varchar(30) NOT NULL,
    PRIMARY KEY(mailAcheteur)
);

CREATE TABLE PREINSCRIRE(
    idCreneau int NOT NULL REFERENCES CRENEAU, 
    mailAcheteur varchar(100) NOT NULL REFERENCES ACHETEUR,
    PRIMARY KEY(idCreneau, mailAcheteur)
);

CREATE TABLE TYPEBILLET(
    idType int NOT NULL,
    dureeEnJours int NOT NULL,
    prix float NOT NULL,
    PRIMARY KEY(idType)
);

CREATE TABLE BILLET(
    idBillet int NOT NULL,
    idFestival int NOT NULL REFERENCES FESTIVAL,
    mailAcheteur varchar(100) NOT NULL REFERENCES ACHETEUR,
    jourdebut date NOT NULL ,
    idType int NOT NULL REFERENCES TYPEBILLET,
    PRIMARY KEY(idBillet)
);

CREATE TABLE FAVORIS(
    mailAcheteur varchar(100) NOT NULL REFERENCES ACHETEUR,
    idGroupe int NOT NULL REFERENCES GROUPE,
    PRIMARY KEY(mailAcheteur, idGroupe)
);


CREATE TABLE IMAGE(
    idImage int NOT NULL,
    nomImage varchar(255) NOT NULL,
    image longblob NOT NULL,
    PRIMARY KEY(idImage)
);

CREATE TABLE PHOTOGROUPE(
    idGroupe int NOT NULL REFERENCES GROUPE,
    idImage int NOT NULL REFERENCES IMAGE,
    PRIMARY KEY(idGroupe, idImage)
)