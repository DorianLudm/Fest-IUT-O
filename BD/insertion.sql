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
    (3, 'Guitare'),
    (4, 'Basse'),
    (5, 'Batterie'),
    (6, 'Clavier'),
    (7, 'Saxophone'),
    (8, 'Violon'),
    (9, 'Flûte'),
    (10, 'Piano'),
    (11, 'Synthétiseur'),
    (12, 'Harmonica'),
    (13, 'Violoncelle'),
    (14, 'Trombone'),
    (15, 'Contrebasse'),
    (16, 'Banjo'),
    (17, 'Accordéon'),
    (18, 'Clarinet'),
    (19, 'Harpe'),
    (20, 'Ondes Martenot'),
    (21, 'Marimba'),
    (22, 'Xylophone'),
    (23, 'Orgue Hammond'),
    (24, 'Steel Drum'),
    (25, 'Bagpipes'),
    (26, 'Didgeridoo'),
    (27, 'Balalaïka'),
    (28, 'Djembe'),
    (29, 'Theremin'),
    (30, 'Sitar'),
    (31, 'Shamisen'),
    (32, 'Koto'),
    (33, 'Tabla'),
    (34, 'Erhu'),
    (35, 'Dulcimer'),
    (36, 'Hang Drum'),
    (37, 'Berimbau'),
    (38, 'Kalimba'),
    (39, 'Cajón'),
    (40, 'Mandoline');

INSERT INTO ARTISTE(idArtiste, nomArtiste, prenomArtiste)
VALUES
    (1, 'Bangalter', 'Thomas'),       
    (2, 'Homem-Christo', 'Guy'),      
    (3, 'Reynolds', 'Dan'),           
    (4, 'Sermon', 'Ben'),             
    (5, 'McVey', 'Andy'),             
    (6, 'Mathers', 'Eminem'),         
    (7, 'Ulrich', 'Lars'),            
    (8, 'Hetfield', 'James'),         
    (9, 'Buckland', 'Jonny'),         
    (10, 'Martin', 'Chris'),          
    (11, 'Gilmour', 'David'),         
    (12, 'Mercury', 'Freddie'),       
    (13, 'Lennon', 'John'),           
    (14, 'Bellamy', 'Matthew'),           
    (15, 'Bono', 'Paul'),             
    (16, 'Yorke', 'Thom'),            
    (18, 'Young', 'Angus'),           
    (19, 'Plant', 'Robert'),          
    (20, 'Jagger', 'Mick'),           
    (21, 'Bennington', 'Chester'),    
    (22, 'Tesfaye', 'Abel'),          
    (23, 'Armstrong', 'Billie Joe'),  
    (24, 'Morrison', 'Jim'),          
    (25, 'Albarn', 'Damon'),          
    (26, 'Idol', 'Billy'),
    (27, 'Partre', 'Jean-Sol'), 
    (28, 'J', 'Jazzy'),
    (29, 'L', 'Lacie'),  
    (30, 'Black', 'Joe'),
    (31, 'Bergling', 'Tim');  


INSERT INTO JOUEINSTRUMENT(idArtiste, idInstrument)
VALUES
    (1, 1),  
    (1, 6),  
    (1, 11), 
    (2, 6),  
    (2, 11),          
    (3, 7),  
    (3, 14),          
    (4, 2),  
    (4, 3),  
    (4, 6),  
    (5, 5),  
    (6, 2),  
    (6, 5),           
    (7, 5),  
    (7, 14),          
    (8, 3),  
    (8, 4),  
    (8, 16), 
    (9, 6),  
    (9, 10),          
    (10, 2), 
    (10, 10),         
    (11, 3), 
    (11, 19),         
    (12, 2), 
    (12, 10),         
    (13, 7), 
    (13, 10),         
    (14, 2), 
    (14, 5),          
    (15, 2), 
    (15, 5),          
    (16, 6), 
    (16, 11),         
    (18, 4), 
    (18, 14),         
    (19, 3), 
    (19, 12),         
    (20, 2), 
    (20, 5),          
    (21, 2), 
    (21, 5),          
    (22, 2), 
    (22, 10),         
    (23, 2), 
    (23, 11),         
    (24, 2), 
    (24, 11),         
    (25, 6), 
    (25, 11),         
    (26, 3), 
    (26, 12),         
    (27, 2), 
    (27, 6),          
    (28, 5), 
    (28, 11),         
    (29, 5), 
    (29, 11),         
    (30, 2), 
    (30, 16);         
    
INSERT INTO GROUPE (idGroupe, nomGroupe, nbPersn, idStyle, descGroupe, videoGroupe)
VALUES
    (1, 'Daft Punk', 2, 6, 'Légendaire duo électronique français connu pour ses beats contagieux et son style futuriste.', 'lien_video_daft_punk'),
    (2, 'Imagine Dragons', 4, 7, 'Groupe de pop-rock américain reconnu pour ses refrains puissants et ses performances énergiques.', 'lien_video_imagine_dragons'),
    (3, 'D12', 6, 5, 'Groupe de rap américain, célèbre pour ses membres, dont Eminem, avec des paroles provocantes et un style distinctif.', 'lien_video_d12'),
    (4, 'Avicii', 1, 8, 'DJ et producteur suédois de musique électronique, célèbre pour ses succès planétaires et son influence dans le genre.', 'lien_video_avicii'),
    (5, 'Coldplay', 4, 2, 'Groupe de pop-rock britannique reconnu pour ses ballades émotionnelles et ses arrangements mélodiques.', 'lien_video_coldplay'),
    (6, 'Pink Floyd', 5, 1, 'Groupe de rock progressif légendaire avec des compositions complexes et des performances visuelles impressionnantes.', 'lien_video_pink_floyd'),
    (7, 'Queen', 4, 1, 'Groupe de rock britannique emblématique, dirigé par Freddie Mercury, avec des hymnes anthémiques.', 'lien_video_queen'),
    (8, 'The Beatles', 4, 2, 'Légendaire groupe de rock britannique qui a révolutionné la musique pop avec ses mélodies novatrices.', 'lien_video_beatles'),
    (9, 'Muse', 3, 1, 'Groupe de rock alternatif britannique connu pour ses performances live dynamiques et ses compositions créatives.', 'lien_video_muse'),
    (10, 'U2', 4, 2, 'Groupe de rock irlandais avec des chansons engagées et des performances scéniques spectaculaires.', 'lien_video_u2'),
    (11, 'Radiohead', 5, 4, 'Groupe de rock indépendant britannique connu pour ses expérimentations sonores et ses paroles poétiques.', 'lien_video_radiohead'),
    (12, 'Eminem', 1, 5, 'Légendaire rappeur américain avec des paroles percutantes et une carrière solo remarquable.', 'lien_video_eminem'),
    (13, 'AC/DC', 5, 1, 'Groupe de hard rock australien célèbre pour ses riffs de guitare puissants et son énergie électrique.', 'lien_video_acdc'),
    (14, 'Led Zeppelin', 4, 1, 'Groupe de rock emblématique avec une fusion de blues, de hard rock et de folk.', 'lien_video_led_zeppelin'),
    (15, 'The Rolling Stones', 5, 1, 'Légendaire groupe de rock britannique avec une carrière musicale exceptionnelle.', 'lien_video_rolling_stones'),
    (16, 'Porcupine Tree', 6, 1, 'Groupe de rock alternatif américain mêlant rock, rap et électronique.', 'lien_video_linkin_park'),
    (17, 'The Weeknd', 4, 7, 'Artiste canadien de R&B et pop connu pour sa voix distinctive et ses productions innovantes.', 'lien_video_the_weeknd'),
    (18, 'Green Day', 3, 1, 'Groupe de punk rock américain avec des hits énergiques et des paroles rebelles.', 'lien_video_green_day'),
    (19, 'The Doors', 4, 1, 'Groupe de rock psychédélique avec la voix inimitable de Jim Morrison et des compositions atmosphériques.', 'lien_video_the_doors'),
    (20, 'Gorillaz', 4, 8, 'Groupe virtuel animé créé par Damon Albarn et Jamie Hewlett, fusionnant divers genres musicaux.', 'lien_video_gorillaz'),
    (21, 'Les Harmoniques Étoilées', 5, 1, 'Un groupe de rock énergique avec une passion pour les solos de guitare.', 'lien_video1'),
    (22, 'Les Mélodies Célestes', 4, 2, 'Une formation populaire qui enflamme la scène avec ses mélodies accrocheuses.', 'lien_video2'),
    (23, 'Le Jazz Fusion', 6, 3, 'Un groupe de jazz expérimenté qui fusionne des rythmes contemporains avec des harmonies classiques.', 'lien_video3'),
    (24, 'Les Explorateurs Indie', 3, 4, 'Un collectif indie qui explore de nouvelles sonorités et repousse les limites de la créativité.', 'lien_video4'),
    (25, 'Les Poètes du Mic', 7, 5, 'Un groupe de rap engagé avec des paroles percutantes et une présence scénique puissante.', 'lien_video5');


INSERT INTO GROUPEARTISTE(idGroupe, idArtiste)
VALUES
    (1, 1),
    (1, 2),                    
    (2, 3),
    (2, 4),                   
    (3, 5),
    (3, 6), 
    (4, 7), 
    (4, 8),  
    (4, 31),                
    (5, 9), 
    (5, 10),                  
    (5, 11),                  
    (6, 11),
    (8, 13), 
    (9, 14),              
    (10, 15), 
    (11, 16), 
    (12, 6),
    (13, 18),
    (14, 19),
    (15, 20),
    (16, 21),
    (17, 22),
    (18, 23),
    (19, 24),
    (20, 25),
    (21, 1),
    (22, 2),
    (23, 25),
    (24, 26),
    (25, 27),
    (25, 28),
    (23, 29),
    (23, 30);

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

INSERT INTO ROLEACHETEUR (idRoleAcheteur, nomRoleAcheteur) 
VALUES 
    (1, 'Administrateur'),
    (2, 'Client');

INSERT INTO ACHETEUR (mailAcheteur, mdp, nom, prenom, idRoleAcheteur)
VALUES
    ('dup@gmail.com', '123', 'Dupont', 'Jean', 2),
    ('mart@gmail.com', '123', 'Martin', 'Sophie', 2),
    ('lecl@gmail.com', '123', 'Leclerc', 'Pierre', 2),
    ('dub@gmail.com', '123', 'Dubois', 'Marie', 2),
    ('lef@gmail.com', '123', 'Lefebvre', 'Luc', 2),
    ('gagn@gmail.com', '123', 'Gagnon', 'Isabelle', 2),
    ('tremb@gmail.com', '123', 'Tremblay', 'Michel', 2),
    ('roy@gmail.com', '123', 'Roy', 'Caroline', 2),
    ('lav@gmail.com', '123', 'Lavoie', 'Éric', 2),
    ('bertr@gmail.com', '123', 'Bertrand', 'Catherine', 2),
    ('gir@gmail.com', '123', 'Girard', 'Mathieu', 2),
    ('pell@gmail.com', '123', 'Pelletier', 'Josée', 2),
    ('lev@gmail.com', '123', 'Lévesque', 'François', 2),
    ('beau@gmail.com', '123', 'Beauchamp', 'Valérie', 2),
    ('mor@gmail.com', '123', 'Morin', 'Stéphanie', 2),
    ('des@gmail.com', '123', 'Desjardins', 'Sylvain', 2),
    ('lap@gmail.com', '123', 'Laplante', 'Nathalie', 2),
    ('cot@gmail.com', '123', 'Côté', 'David', 2),
    ('bou@gmail.com', '123', 'Boucher', 'Mélanie', 2),
    ('poi@gmail.com', '123', 'Poirier', 'Richard', 2),
    ('thi@gmail.com', '123', 'Thibault', 'Marie-Pierre', 2),
    ('gau@gmail.com', '123', 'Gauthier', 'Jonathan', 2),
    ('rous@gmail.com', '123', 'Rousseau', 'Julie', 2),
    ('leg@gmail.com', '123', 'Léger', 'Marc', 2),
    ('fort@gmail.com', '123', 'Fortin', 'Isabelle', 2),
    ('car@gmail.com', '123', 'Caron', 'Nicolas', 2),
    ('mic@gmail.com', '123', 'Michaud', 'Annie', 2),
    ('gel@gmail.com', '123', 'Gélinas', 'Martin', 2),
    ('ars@gmail.com', '123', 'Arsenault', 'Geneviève', 2),
    ('pla@gmail.com', '123', 'Plante', 'Alexandre', 2),
    ('anna@', 'cbo', "Lallier", "Anna", 2),
    ('leo.lucidor@gmail.com', '123', 'lucidor', 'léo', 1),
    ('colin@', '123', 'pilet', 'colin', 1);

INSERT INTO PREINSCRIRE(idCreneau, mailAcheteur)
VALUES
    (3,'dup@gmail.com'),
    (4,'mart@gmail.com');

INSERT INTO TYPEBILLET (idType, dureeEnJours, prix)
VALUES
    (1, 1, 20.00), 
    (2, 2, 35.00), 
    (3, 3, 90.00);

INSERT INTO BILLET (idBillet, idFestival, mailAcheteur, jourdebut, jourDeux, idType)
VALUES
    (1, 3, 'dup@gmail.com',  '2023-09-25', NULL, 3),
    (2, 3, 'ars@gmail.com',  '2023-09-25', NULL, 3),
    (3, 3, 'mart@gmail.com', '2023-09-26', '2023-09-26', 2),
    (4, 4, 'mart@gmail.com', '2023-10-05', NULL, 1),
    (5, 4, 'gagn@gmail.com', '2023-10-06', '2023-10-07', 2),
    (6, 5, 'bou@gmail.com',  '2023-10-11', NULL, 1);


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
    (3, 'imagine-dragon.png'),
    (2, 'd12.png'),
    (4, 'avicii.png'),
    (5, 'coldplay.png'),
    (6, 'pinkfloyd.png'),
    (7, 'queen.png'),
    (8, 'beatles.png'),
    (9, 'muse.png'),
    (10, 'u2.png'),
    (11, 'radiohead.png'),
    (12, 'eminem.png'),
    (13, 'acdc.png'),
    (14, 'ledzep.png'),
    (15, 'stones.png'),
    (16, 'porcupinetree.png'),
    (17, 'weeknd.png'),
    (18, 'greenday.png'),
    (19, 'thedoors.png'),
    (20, 'gorillaz.png'),
    (21, 'default.png'),
    (22, 'groupemoderne.png'),
    (23, 'groupe2.png'),
    (24, 'groupe.png'),
    (25, 'default.png');
