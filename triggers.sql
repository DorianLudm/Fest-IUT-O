delimiter |
create or replace TRIGGER verif_style_mysical before insert on TABLE for each row
begin
    declare var type;
    select * into var from ... where ...;
    if() then
        set mes = "Texte explicant l'erreur";
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if
end
delimiter;
