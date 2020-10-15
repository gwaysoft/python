from flask_sqlalchemy import SQLAlchemy
from gspackage.flask_sqlalchemy_mysql import config

def init_db(app):
    app.config.from_object(config)
    db = SQLAlchemy()
    db.init_app(app)
    return db
