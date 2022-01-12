from flask import Flask
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "inventory.db"

def create_database(app):
    '''
    Creates a singleton database
    '''
    if not path.exists('website/' + DB_NAME):
        db.create_all(app = app)
        print('New Database Created!')




def create_app():
    app = Flask(__name__)

    # Initialize the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Register Blueprint
    from .views import views
    app.register_blueprint(views, url_prefix = "/")

    # Import database models and create the database
    from .models import Item
    create_database(app)

    return app

