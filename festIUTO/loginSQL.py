#Version BD en ligne
login = "335676" # pip install pymysql
passwd = "annafestiuto"
serveur= "mysql-annalallier.alwaysdata.net"
bd = "annalallier_festiuto2"

#Version MariaDB
# login = "ludmann" # pip install pymysql
# passwd = "ludmann"
# serveur= "servinfo-maria"
# bd = "DBludmann"

def getLogin():
    return login

def getPasswd():
    return passwd

def getServeur():
    return serveur

def getBd():
    return bd