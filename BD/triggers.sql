delimiter |
create or replace TRIGGER verif_liaison_musicale before insert on LIAISONMUSICALE for each row
begin
    declare style1 int;
    declare style2 int;
    declare mes varchar(255);
    select idStyle1 into style1 from LIAISONMUSICALE where idStyle1 = new.idStyle2 and idStyle2 = new.idStyle1;
    select idStyle2 into style2 from LIAISONMUSICALE where idStyle2 = new.idStyle1 and idStyle1 = new.idStyle2;
    if(style1 != 0 and style2 !=0) then
        set mes = "La liaison inverse existe déjà";
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
end |
delimiter ;

delimiter |
create or replace TRIGGER update_nbpersn_insert after insert on GROUPEARTISTE for each row
begin
    declare totalartistes int;

    select count(idArtiste) into totalartistes from GROUPEARTISTE where idGroupe = new.idGroupe;

    update GROUPE set nbPersn = totalartistes where idGroupe = new.idGroupe;
end |
delimiter ;

delimiter |
create or replace TRIGGER update_nbpersn_update after update on GROUPEARTISTE for each row
begin
    declare totalartistes int;

    select count(idArtiste) into totalartistes from GROUPEARTISTE where idGroupe = new.idGroupe;

    update GROUPE set nbPersn = totalartistes where idGroupe = new.idGroupe;
end |
delimiter ;

delimiter |
create or replace TRIGGER update_nbpersn_delete before delete on GROUPEARTISTE for each row
begin
    declare totalartistes int;

    select count(idArtiste) into totalartistes from GROUPEARTISTE where idGroupe = old.idGroupe;

    update GROUPE set nbPersn = totalartistes where idGroupe = old.idGroupe;
end |
delimiter ;

delimiter |
create or replace TRIGGER verif_capacite_préinscription before insert on PREINSCRIRE for each row
begin
    declare date_debut date;
    declare date_fin date;
    declare datetimeDebut datetime;
    declare dureeHeure time;
    declare fini boolean default false ;

    SELECT dateDebutFestival, dateFinFestival into date_debut, date_fin from FESTIVAL NATURAL JOIN LIEUSDUFESTIVAL NATURAL JOIN LIEU NATURAL JOIN CRENEAU where idCreneau = new.idCreneau;
    SELECT heureDebutCreneau, duree into datetimeDebut, dureeHeure from CRENEAU where idCreneau = new.idCreneau;
    declare heureFinCreneau datetime;
    set heureFinCreneau = DATE_ADD(datetimeDebut, INTERVAL  HOUR(dureeHeure) HOUR_SECOND);


    if (date_debut > date(datetimeDebut) or date_fin < date(datetimeDebut) or date_debut > date(heureFinCreneau) or date_fin < date(heureFinCreneau)) then
        set fini = true;
    end if;
    end |
delimiter ;

delimiter |
create or replace TRIGGER verif_horaires_creneau_dans_dates_festival before insert on CRENEAU for each row
begin
    declare date_debut date;
    declare date_fin date;
    declare datetimeDebut datetime;
    declare dureeHeure time;
    declare fini boolean default false ;

    SELECT dateDebutFestival, dateFinFestival into date_debut, date_fin from FESTIVAL NATURAL JOIN LIEUSDUFESTIVAL NATURAL JOIN LIEU NATURAL JOIN CRENEAU where idCreneau = new.idCreneau;
    SELECT heureDebutCreneau, duree into datetimeDebut, dureeHeure from CRENEAU where idCreneau = new.idCreneau;
    declare heureFinCreneau datetime;
    set heureFinCreneau = DATE_ADD(datetimeDebut, INTERVAL  HOUR(dureeHeure) HOUR_SECOND);


    if (date_debut > date(datetimeDebut) or date_fin < date(datetimeDebut) or date_debut > date(heureFinCreneau) or date_fin < date(heureFinCreneau)) then
        set fini = true;
    end if;
    end |
delimiter ;