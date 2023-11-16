delimiter |
create or replace TRIGGER verif_capacite_preinscription before insert on PREINSCRIRE for each row
begin
    declare cap int;
    declare nb_inscrit int;
    declare mes varchar(255);
    select IFNULL(nbPlacesLieu,0) into cap from PREINSCRIRE NATURAL JOIN CRENEAU NATURAL JOIN LIEU  where idCreneau = new.idCreneau and mailAcheteur = new.mailAcheteur;
    insert into DEBUG (nb) values (cap) ;
    select IFNULL(count(mailAcheteur),0) into nb_inscrit from PREINSCRIRE NATURAL JOIN CRENEAU NATURAL JOIN LIEU where idCreneau = new.idCreneau; 
    insert into DEBUG (nb) values (nb_inscrit) ;
    if(cap <= nb_inscrit) then
        set mes = "Préinscription impossible, le lieu est complet";
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
    
end |
delimiter ;

-- tests sur préinscrire
INSERT INTO PREINSCRIRE(idCreneau, mailAcheteur)
    -> VALUES
    ->     (4,'dup@gmail.com');
Query OK, 1 row affected (0,029 sec)

MariaDB [DBlallier]> SELECT * FROM DEBUG ;
+-------+------+
| idbug | nb   |
+-------+------+
|     3 | NULL |
|     4 |    1 |

