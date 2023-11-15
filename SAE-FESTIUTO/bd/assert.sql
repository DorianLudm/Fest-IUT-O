
-- Table CONCERT
INSERT INTO CONCERT (idFestival, nomFestival, dateFestival, dateFinFestival, nombreBillets, preinscription)
VALUES
    (1, 'A', '2023-09-15 08:00:00', '2023-09-15 12:00:00', 1000, 1),
    (2, 'B', '2023-09-20 10:00:00', '2023-09-20 14:00:00', 800, 0),
    (3, 'C', '2023-09-25 06:30:00', '2023-09-25 10:30:00', 1200, 1),
    (4, 'D', '2023-10-05 09:30:00', '2023-10-05 13:30:00', 1500, 0),
    (5, 'E', '2023-10-10 07:00:00', '2023-10-10 11:00:00', 900, 1);

-- Table LIEU
INSERT INTO LIEU (idLieu, nomLieu, latitudeLieu, longitudeLieu, disponibiliteLieu)
VALUES
    (1, 'Scène A', '12.345', '67.890', 1),
    (2, 'Scène B', '12.678', '56.432', 0),
    (3, 'Scène XYZ', '34.567', '98.765', 1),
    (4, 'Scène C', '23.456', '78.901', 1),
    (5, 'Scène D', '45.678', '34.567', 1);

-- Table LIEUSDUCONCERT
INSERT INTO LIEUSDUCONCERT (idLieu, idFestival)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);

-- Table HEBERGEMENT
INSERT INTO HEBERGEMENT (idHebergement, nomHebergement, nombreDePlaces, idFestival)
VALUES
    (1, 'Le gîte', 50, 1),
    (2, 'A', 30, 2),
    (3, 'B', 100, 3),
    (4, 'C', 40, 4),
    (5, 'D', 60, 5);

-- Table STYLEMUSICAL
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

-- Table ARTISTE
INSERT INTO ARTISTE (idArtiste, nomGroupe, nbPersn, idStyle, descArtiste, photoArtiste, reseauxArtiste, videoArtiste, instrumentArtiste)
VALUES
    (1, 'Les Harmoniques Étoilées', 5, 1, 'Un groupe de rock énergique avec une passion pour les solos de guitare.', '/media/o22203041/Leo/but2/web/TP1/2a-web-serveur/TP1/tuto-flask/tuto/static/img/imagine-dragon.png', 'lien_reseau_social1', 'lien_video1', 'Guitare, Batterie, Basse'),
    (2, 'Les Mélodies Célestes', 4, 2, 'Une formation populaire qui enflamme la scène avec ses mélodies accrocheuses.', '/media/o22203041/Leo/but2/web/TP1/2a-web-serveur/TP1/tuto-flask/tuto/static/img/imagine-dragon.png', 'lien_reseau_social2', 'lien_video2', 'Chant, Guitare, Clavier'),
    (3, 'Le Jazz Fusion', 6, 3, 'Un groupe de jazz expérimenté qui fusionne des rythmes contemporains avec des harmonies classiques.', '/media/o22203041/Leo/but2/web/TP1/2a-web-serveur/TP1/tuto-flask/tuto/static/img/imagine-dragon.png', 'lien_reseau_social3', 'lien_video3', 'Saxophone, Trompette, Contrebasse'),
    (4, 'Les Explorateurs Indie', 3, 4, 'Un collectif indie qui explore de nouvelles sonorités et repousse les limites de la créativité.', 'lien_photo4.jpg', 'lien_reseau_social4', 'lien_video4', 'Chant, Guitare'),
    (5, 'Les Poètes du Mic', 7, 5, 'Un groupe de rap engagé avec des paroles percutantes et une présence scénique puissante.', 'lien_photo5.jpg', 'lien_reseau_social5', 'lien_video5', 'MC, Beatbox, DJ');

-- Table ORGANISATIONARTISTE
INSERT INTO ORGANISATIONARTISTE (idArtiste, idFestival, idHebergement, arrivee, depart, tempsMontage, tempsDemontage)
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

-- Table CRENEAU
INSERT INTO CRENEAU (idCreneau, idLieu, idArtiste, idEvent, heureDebut, duree, descriptionEvenement)
VALUES
    (1, 1, 1, 1, '2023-09-15 08:00:00', '02:00:00', 'Concert principal'),
    (2, 2, 2, 1, '2023-09-15 09:00:00', '01:30:00', 'Artiste en première partie'),
    (3, 3, 3, 1, '2023-09-15 11:30:00', '01:45:00', 'Artiste en deuxième partie'),
    (4, 4, 4, 2, '2023-09-20 10:30:00', '02:15:00', 'Concert principal'),
    (5, 5, 5, 2, '2023-09-20 11:00:00', '01:30:00', 'Artiste en première partie');

-- Table ACHETEUR
INSERT INTO ACHETEUR (idAcheteur, mdp, nom, prenom)
VALUES
    (1, '123', 'Dupont', 'Jean'),
    (2, '123', 'Martin', 'Sophie'),
    (3, '123', 'Leclerc', 'Pierre'),
    (4, '123', 'Dubois', 'Marie'),
    (5, '123', 'Lefebvre', 'Luc'),
    (6, '123', 'Gagnon', 'Isabelle'),
    (7, '123', 'Tremblay', 'Michel'),
    (8, '123', 'Roy', 'Caroline'),
    (9, '123', 'Lavoie', 'Éric'),
    (10, '123', 'Bertrand', 'Catherine'),
    (11, '123', 'Girard', 'Mathieu'),
    (12, '123', 'Pelletier', 'Josée'),
    (13, '123', 'Lévesque', 'François'),
    (14, '123', 'Beauchamp', 'Valérie'),
    (15, '123', 'Morin', 'Stéphanie'),
    (16, '123', 'Desjardins', 'Sylvain'),
    (17, '123', 'Laplante', 'Nathalie'),
    (18, '123', 'Côté', 'David'),
    (19, '123', 'Boucher', 'Mélanie'),
    (20, '123', 'Poirier', 'Richard'),
    (21, '123', 'Thibault', 'Marie-Pierre'),
    (22, '123', 'Gauthier', 'Jonathan'),
    (23, '123', 'Rousseau', 'Julie'),
    (24, '123', 'Léger', 'Marc'),
    (25, '123', 'Fortin', 'Isabelle'),
    (26, '123', 'Caron', 'Nicolas'),
    (27, '123', 'Michaud', 'Annie'),
    (28, '123', 'Gélinas', 'Martin'),
    (29, '123', 'Arsenault', 'Geneviève'),
    (30, '123', 'Plante', 'Alexandre');

-- Table BILLET
INSERT INTO BILLET (idBillet, idFestival, idAcheteur, duree, prix, nombrePersBillet, nombreJourBillet)
VALUES
    (1, 1, 1, 1, 50.0, 1, 1),
    (2, 1, 2, 2, 90.0, 2, 2),
    (3, 2, 3, 3, 120.0, 1, 3),
    (4, 2, 4, 2, 80.0, 2, 2),
    (5, 3, 5, 1, 60.0, 1, 1),
    (31, 1, 6, 2, 80.0, 2, 2),
    (32, 2, 7, 3, 120.0, 1, 3),
    (33, 2, 8, 2, 90.0, 2, 2),
    (34, 3, 9, 1, 60.0, 1, 1),
    (35, 3, 10, 1, 50.0, 1, 1);

-- Table FAVORIS
INSERT INTO FAVORIS (idAcheteur, idArtiste)
VALUES
    (1, 1),
    (1, 3),
    (2, 2),
    (3, 4),
    (4, 5),
    (5, 1);