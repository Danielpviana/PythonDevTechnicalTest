from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def db_configure(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:my-secret-pw@localhost/aht-global-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    global db
    db.init_app(app)
    
    return app, db

def init_db():
    db.create_all()