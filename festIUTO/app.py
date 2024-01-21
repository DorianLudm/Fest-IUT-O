from flask import Flask, render_template, request, redirect, session
#from flask_sqlalchemy import SQLAlchemy  # pip install Flask-SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import Flask
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = "5bde79f0-262d-43b0-a194-61866f36fd11"
csrf = CSRFProtect(app)
csrf.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

