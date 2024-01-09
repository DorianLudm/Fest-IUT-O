INSERT INTO FESTIVAL (idFestival, nomFestival, dateDebutFestival, dateFinFestival)
VALUES
    (1, 'A', '2023-09-15 14:00:00', '2023-09-16 23:00:00'),
    (2, 'B', '2023-09-20 14:00:00', '2023-09-21 23:00:00'),
    (3, 'C', '2023-09-25 14:30:00', '2023-09-26 23:30:00'),
    (4, 'D', '2023-10-05 14:30:00', '2023-10-06 23:30:00'),
    (5, 'E', '2023-10-10 14:00:00', '2023-10-11 23:00:00');

INSERT INTO BILLETSPARJOUR (idFestival, jour, nombreBillets)
VALUES
    (1, 1, 500),
    (1, 2, 600),
    (2, 1, 450),
    (2, 2, 550),
    (3, 1, 700),
    (3, 2, 800),
    (4, 1, 400),
    (4, 2, 500),
    (5, 1, 600),
    (5, 2, 700);
 
INSERT INTO LIEU (idLieu, adresse, nomLieu, disponibiliteLieu, nbPlacesLieu)
VALUES
    (1, 'adresse','Scène A', 1, 150),
    (2, 'adresse','Scène B', 0, 256),
    (3, 'adresse','Scène XYZ', 1, 800),
    (4, 'adresse','Scène C', 1, 300),
    (5, 'adresse','Scène D', 1, 900);

INSERT INTO LIEUSDUFESTIVAL (idLieu, idFestival)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);

INSERT INTO HEBERGEMENT (idHebergement, nomHebergement, nombreDePlaces)
VALUES
    (1, 'Le gîte', 50),
    (2, 'A', 30),
    (3, 'B', 100), 
    (4, 'C', 40),
    (5, 'D', 60);

INSERT INTO STYLEMUSICAL (idStyle, nom, description)
VALUES
    (1, 'Rock', 'Un genre musical caractérisé par des guitares électriques et une forte rythmique.'),
    (2, 'Pop', 'Un genre musical populaire avec des mélodies accrocheuses et des chansons entraînantes.'),
    (3, 'Jazz', 'Un genre musical improvisé avec des harmonies sophistiquées et des solos.'),
    (4, 'Indie', 'Un genre musical indépendant avec des sonorités expérimentales et originales.'),
    (5, 'Rap', 'Un genre musical rythmé avec des paroles rapides et engagées.'),
    (6, 'Classique', 'Un genre musical riche en traditions avec une notation complexe et des compositions symphoniques.'),
    (7, 'Reggae', 'Un genre musical originaire de la Jamaïque avec un rythme caractéristique et des messages sociaux.'),
    (8, 'Electronique', 'Un genre musical créé à l aide d instruments électroniques et de synthétiseurs.');

INSERT INTO LIAISONMUSICALE(idStyle1, idStyle2)
VALUES
    (2,1);

INSERT INTO RESEAUXSOCIAUX(idReseau, nomReseau)
VALUES
    (1, 'Twitter'),
    (2, 'Youtube'),
    (3, 'Instagram');

INSERT INTO INSTRUMENT(idInstrument, nomInstrument)
VALUES
    (1, 'Trompette'),
    (2, 'Chant'),
    (3, 'Guitare') ;

INSERT INTO ARTISTE(idArtiste, nomArtiste, prenomArtiste)
VALUES
    (1, 'MC', 'Paul'),
    (2, 'Yo', 'Yo'),
    (3, 'X', 'Thimotée');

INSERT INTO JOUEINSTRUMENT(idArtiste, idInstrument)
VALUES
    (1, 3),
    (2, 2),
    (3, 1);

INSERT INTO GROUPE (idGroupe, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe)
VALUES
    (1, 'Les Harmoniques Étoilées', 5, 1, 'Un groupe de rock énergique avec une passion pour les solos de guitare.', 'lien_video1'),
    (2, 'Les Mélodies Célestes', 4, 2, 'Une formation populaire qui enflamme la scène avec ses mélodies accrocheuses.', 'lien_video2'),
    (3, 'Le Jazz Fusion', 6, 3, 'Un groupe de jazz expérimenté qui fusionne des rythmes contemporains avec des harmonies classiques.', 'lien_video3'),
    (4, 'Les Explorateurs Indie', 3, 4, 'Un collectif indie qui explore de nouvelles sonorités et repousse les limites de la créativité.', 'lien_video4'),
    (5, 'Les Poètes du Mic', 7, 5, 'Un groupe de rap engagé avec des paroles percutantes et une présence scénique puissante.', 'lien_video5');

INSERT INTO GROUPEARTISTE(idGroupe, idArtiste)
VALUES
    (1, 1),
    (5, 2),
    (2, 3);

INSERT INTO RESEAUXGROUPE(idReseau, idGroupe,lienReseau)
VALUES
    (1, 1, 'x'),
    (2, 2, 'x'),
    (3, 3, 'x');

INSERT INTO ORGANISATIONGROUPE (idGroupe, idFestival, idHebergement, arrivee, depart, tempsMontage, tempsDemontage)
VALUES
    (1, 1, 1, '2023-09-14 15:00:00', '2023-09-16 12:00:00', '02:00:00', '01:30:00'),
    (2, 2, 2, '2023-09-19 14:00:00', '2023-09-21 11:00:00', '01:45:00', '01:15:00'),
    (3, 3, 3, '2023-09-24 16:30:00', '2023-09-26 09:30:00', '02:30:00', '01:45:00'),
    (4, 4, 4, '2023-10-04 17:45:00', '2023-10-06 14:30:00', '02:15:00', '02:00:00'),
    (5, 5, 5, '2023-10-09 13:00:00', '2023-10-11 10:00:00', '02:15:00', '01:45:00');

-- Table EVENTTYPE
INSERT INTO EVENTTYPE (idEvent, nom)
VALUES
    (1, 'Concert'),
    (2, 'Interview'),
    (3, 'Backstage');

INSERT INTO CRENEAU (idCreneau, idLieu, idGroupe, idEvent, visibleAuPublic, heureDebut, duree, descriptionEvenement, preinscriptionPossible, gratuit)
VALUES
    (1, 1, 1, 1, 0, '2023-09-15 08:00:00', '02:00:00', 'Festival principal', 0, 1),
    (2, 2, 2, 1, 0, '2023-09-15 09:00:00', '01:30:00', 'Groupe en première partie', 0, 0),
    (3, 3, 3, 1, 0, '2023-09-15 11:30:00', '01:45:00', 'Groupe en deuxième partie', 1, 0),
    (4, 4, 4, 2, 0, '2023-09-20 10:30:00', '02:15:00', 'Festival principal', 1, 1),
    (5, 5, 5, 2, 0, '2023-09-20 11:00:00', '01:30:00', 'Groupe en première partie', 0, 1);

INSERT INTO ACHETEUR (mailAcheteur, mdp, nom, prenom)
VALUES
    ('dup@gmail.com', '123', 'Dupont', 'Jean'),
    ('mart@gmail.com', '123', 'Martin', 'Sophie'),
    ('lecl@gmail.com', '123', 'Leclerc', 'Pierre'),
    ('dub@gmail.com', '123', 'Dubois', 'Marie'),
    ('lef@gmail.com', '123', 'Lefebvre', 'Luc'),
    ('gagn@gmail.com', '123', 'Gagnon', 'Isabelle'),
    ('tremb@gmail.com', '123', 'Tremblay', 'Michel'),
    ('roy@gmail.com', '123', 'Roy', 'Caroline'),
    ('lav@gmail.com', '123', 'Lavoie', 'Éric'),
    ('bertr@gmail.com', '123', 'Bertrand', 'Catherine'),
    ('gir@gmail.com', '123', 'Girard', 'Mathieu'),
    ('pell@gmail.com', '123', 'Pelletier', 'Josée'),
    ('lev@gmail.com', '123', 'Lévesque', 'François'),
    ('beau@gmail.com', '123', 'Beauchamp', 'Valérie'),
    ('mor@gmail.com', '123', 'Morin', 'Stéphanie'),
    ('des@gmail.com', '123', 'Desjardins', 'Sylvain'),
    ('lap@gmail.com', '123', 'Laplante', 'Nathalie'),
    ('cot@gmail.com', '123', 'Côté', 'David'),
    ('bou@gmail.com', '123', 'Boucher', 'Mélanie'),
    ('poi@gmail.com', '123', 'Poirier', 'Richard'),
    ('thi@gmail.com', '123', 'Thibault', 'Marie-Pierre'),
    ('gau@gmail.com', '123', 'Gauthier', 'Jonathan'),
    ('rous@gmail.com', '123', 'Rousseau', 'Julie'),
    ('leg@gmail.com', '123', 'Léger', 'Marc'),
    ('fort@gmail.com', '123', 'Fortin', 'Isabelle'),
    ('car@gmail.com', '123', 'Caron', 'Nicolas'),
    ('mic@gmail.com', '123', 'Michaud', 'Annie'),
    ('gel@gmail.com', '123', 'Gélinas', 'Martin'),
    ('ars@gmail.com', '123', 'Arsenault', 'Geneviève'),
    ('pla@gmail.com', '123', 'Plante', 'Alexandre'),
    ('anna@', 'cbo', "Lallier", "Anna");

INSERT INTO PREINSCRIRE(idCreneau, mailAcheteur)
VALUES
    (3,'dup@gmail.com'),
    (4,'mart@gmail.com');

INSERT INTO TYPEBILLET (idType, dureeEnJours, prix)
VALUES
    (1, 1, 50.00), 
    (2, 2, 90.00), 
    (3, 3, 120.00);

INSERT INTO BILLET (idBillet, idFestival, mailAcheteur, jourdebut, idType)
VALUES
    (1, 3, 'dup@gmail.com',  '2023-09-25', 3),
    (2, 3, 'ars@gmail.com',  '2023-09-25', 3),
    (3, 3, 'mart@gmail.com', '2023-09-26', 2),
    (4, 4, 'mart@gmail.com', '2023-10-05', 1),
    (5, 4, 'gagn@gmail.com', '2023-10-06', 2),
    (6, 5, 'bou@gmail.com',  '2023-10-11', 1);


INSERT INTO FAVORIS (mailAcheteur, idGroupe)
VALUES
    ('dup@gmail.com', 1),
    ('ars@gmail.com', 3),
    ('mart@gmail.com', 2),
    ('mart@gmail.com', 4),
    ('gagn@gmail.com', 5),
    ('bou@gmail.com', 1);

INSERT INTO PHOTOGROUPE(idGroupe, nomImage) 
VALUES
    (1, 'daftpunk.png'),
    (2, 'groupemoderne.png'),
    (3, 'imagine-dragon.png'),
    (4, 'groupe.png'),
    (5, 'groupe2.png');