CREATE TABLE CONCERT(
    idFestival int NOT NULL,
    nomFestival varchar(30) NOT NULL,
    dateFestival datetime check(HOUR(dateFestival) between 4 and 14),
    dateFinFestival datetime check(HOUR(dateFestival) between 4 and 14),
    nombreBillets int NOT NULL,
    preinscription boolean NOT NULL,
    PRIMARY KEY(idFestival)
);

CREATE TABLE LIEU(
    idLieu int NOT NULL,
    nomLieu varchar(30),
    latitudeLieu varchar(40),
    longitudeLieu varchar(40),
    disponibiliteLieu boolean NOT NULL,
    nombreDePlaces int,
    PRIMARY KEY(idLieu)
);

CREATE TABLE LIEUSDUCONCERT(
    idLieu int NOT NULL REFERENCES LIEU,
    idFestival int NOT NULL REFERENCES CONCERT,
    PRIMARY KEY(idLieu, idFestival)
);

CREATE TABLE HEBERGEMENT(
    idHebergement int,
    nombreDePlaces int,
    nomHebergement varchar(30),
    idFestival int NOT NULL REFERENCES CONCERT,
    PRIMARY KEY(idHebergement)
);

CREATE TABLE STYLEMUSICAL(
    idStyle int NOT NULL,
    nom varchar(30),
    description varchar(255),
    PRIMARY KEY(idStyle)
);

CREATE TABLE ARTISTE(
    idArtiste int NOT NULL,
    nomGroupe varchar(30),
    nbPersn int,
    idStyle int NOT NULL REFERENCES STYLEMUSICAL,
    descArtiste varchar(300),
    photoArtiste varchar(150), -- liens photos / blob
    reseauxArtiste varchar(150), -- liens resaux sociaux 
    videoArtiste varchar(150), -- liens video
    instrumentArtiste varchar(100), -- les instruments joués par le groupe
    PRIMARY KEY(idArtiste)
);


--CREATE TABLE LIENPERSONNEARTISTE(
--    idArtiste int REFERENCES ARTISTE,
--    idPersonne int REFERENCES PERSONNE,
--    PRIMARY KEY(idArtiste, idPersonne)
--)

--CREATE TABLE PERSONNE(
--    idPersonne int,
--    nom varchar(30) NOT NULL,
--    prenom varchar(30) NOT NULL,
--    PRIMARY KEY(idPersonne)
--)


CREATE TABLE ORGANISATIONARTISTE(
    idArtiste int NOT NULL REFERENCES ARTISTE,
    idFestival int NOT NULL REFERENCES CONCERT,
    idHebergement int NOT NULL REFERENCES HEBERGEMENT,
    arrivee datetime NOT NULL,
    depart datetime NOT NULL,
    tempsMontage time,
    tempsDemontage time,
    PRIMARY KEY(idArtiste, idFestival)
);

CREATE TABLE EVENTTYPE(
    idEvent int NOT NULL,
    nom varchar(300),
    PRIMARY KEY(idEvent)
);

CREATE TABLE CRENEAU(
    idCreneau int NOT NULL,
    idLieu int NOT NULL REFERENCES LIEU,
    idArtiste int NOT NULL REFERENCES ARTISTE,
    idEvent int NOT NULL REFERENCES EVENTTYPE,
    heureDebut datetime check(HOUR(heureDebut) between 4 and 14),
    duree TIME NOT NULL,
    descriptionEvenement varchar(255),
    PRIMARY KEY(idLieu, idArtiste, heureDebut)
);

CREATE TABLE ACHETEUR(
    idAcheteur int NOT NULL,
    nom varchar(30) NOT NULL,
    prenom varchar(30) NOT NULL,
    mdp varchar(30) NOT NULL,
    PRIMARY KEY(idAcheteur)
);

CREATE TABLE BILLET(
    idBillet int NOT NULL,
    idFestival int NOT NULL REFERENCES CONCERT,
    idAcheteur int REFERENCES ACHETEUR,
    duree int NOT NULL,
    prix float,
    nombrePersBillet int NOT NULL,
    nombreJourBillet int NOT NULL,
    PRIMARY KEY(idBillet)
);

CREATE TABLE FAVORIS(
    idAcheteur int NOT NULL REFERENCES ACHETEUR,
    idArtiste int NOT NULL REFERENCES ARTISTE,
    PRIMARY KEY(idAcheteur, idArtiste)
);