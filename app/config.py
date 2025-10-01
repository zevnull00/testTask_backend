# app/config.py

class Config:
    # это нужно хранить тут и в таком виде? или нет? наверное, TODO
    SQLALCHEMY_DATABASE_URI = "postgresql://remote:Klljoy99@localhost/db"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "options": "-c search_path=ob,public"
        }
    }
    # просто чтобы не пищал
    SQLALCHEMY_TRACK_MODIFICATIONS = False