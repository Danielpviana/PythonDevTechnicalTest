import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@db/inventory_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
