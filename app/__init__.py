# app/__init__.py

from flask import Flask
from .config import Config
from .models import db
from .api import api_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Регистрация blueprint'ов
    app.register_blueprint(api_bp)

    return app