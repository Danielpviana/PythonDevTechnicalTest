import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:my-secret-pw@host.docker.internal/aht-global-db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SECRET_KEY = os.urandom(24)
