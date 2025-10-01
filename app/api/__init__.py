# app/api/__init__.py

from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='')

from . import routes  # импортируем маршруты, чтобы они зарегистрировались