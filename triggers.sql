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
create or replace TRIGGER verif_capacite_préinscription before insert on PREINSCRIRE for each row
begin
    declare 