import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db = SQLAlchemy()
DB_NAME = "library.db" #must refactor with library.db

# some_engine = create_engine(f'sqlite:///{DB_NAME}')
# Session = sessionmaker(bind=some_engine)

# session = Session()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Customer, Employee, Book

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader          #come back to this to make it work for emp
    def load_user(id):
        return Customer.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        print
        db.create_all(app=app)
        print('Created Database!')
