"""init file"""
from os import path

from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app() -> Flask:
    """create_app function"""
    app = Flask(__name__)
    # openssl rand -hex 32
    app.config[
        "SECRET_KEY"
    ] = "9365ee2fb7a791737f0b961a40f2240d58bab9b0443d7520eb2f37fc0bdbccab"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    create_database(app)
    return app


def create_database(app: Flask) -> None:
    """database creatio"""

    if not path.exists(path.join("website", DB_NAME)):
        db.create_all(app=app)
