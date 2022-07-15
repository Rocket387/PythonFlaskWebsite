
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# setting up database
db = SQLAlchemy()  # defines database, db object used when want to add something/create a new user
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs' # encrypts/secures cookies in session data (never share in production) 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # tells flask where the db is located
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note # need to make sure models.py file runs and defines classes before we create DB

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # looks for the primary key by default and makes sure it is equal to whatever is passed to it
 

    return app


def create_database(app): # checks if DB exists, if not it will create it
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')