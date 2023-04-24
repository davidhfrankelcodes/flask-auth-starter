from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get(
        "FLASK_SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY")
    app.config['LOGIN_VIEW'] = "auth.login"
    app.config['LOGIN_MESSAGE'] = "Please log in to access this page."
    app.config['LOGIN_MESSAGE_CATEGORY'] = "info"

    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)

    from flask_app.routes.homepage import homepage_bp
    from flask_app.routes.auth import auth_bp

    app.register_blueprint(homepage_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
