from flask import Flask
from app.db_config import db, db_configure, init_db
from app.routes import router


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:my-secret-pw@localhost/aht-global-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #app = db_configure(app)
    
    db.init_app(app)
    
    app.register_blueprint(router)

    return app
