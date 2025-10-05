# app/config.py
from dotenv import load_dotenv
import os

load_dotenv()  # ← загружает .env


class Config:
    # это нужно хранить тут и в таком виде? или нет? наверное, TODO
    SQLALCHEMY_DATABASE_URI = "postgresql://" + os.getenv("DB_USER") + ":" + os.getenv("DB_PASS") + "@localhost/db"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "options": "-c search_path=ob,public"
        }
    }
    #SQLALCHEMY_ECHO = True
    # просто чтобы не пищал
    SQLALCHEMY_TRACK_MODIFICATIONS = False