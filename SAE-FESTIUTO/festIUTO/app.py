from flask import Flask, render_template, request, redirect, session
#from flask_sqlalchemy import SQLAlchemy  # pip install Flask-SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector 
from datetime import datetime
from flask import Flask
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'

# Configuration de la base de données SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/saeweb'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

# Configuration de la base de données MariaDB
DATABASE = mysql.connector.connect(
     user='root',
     password= 'root',
     host= 'localhost',
     database= 'saeweb',
)

idAcheteur = 1

# Modèle SQLAlchemy pour la table des utilisateurs (ACHETEUR)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#    date_joined = db.Column(db.datetime, default=datetime.utcnow)


# DATABASE = get_db_connection()
# cursor = DATABASE.cursor()
# cursor.execute("SHOW TABLES")
# for table in cursor:
#     print(table)
# cursor.close()
# DATABASE.close()


# session.pop('user_id', None)  # Supprimez l'ID de l'utilisateur de la session


if __name__ == '__main__':
    app.run(debug=True)
