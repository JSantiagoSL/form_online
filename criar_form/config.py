import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:ptsql24@localhost/forms_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
