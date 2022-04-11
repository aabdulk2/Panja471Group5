from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Book(db.Model):
    book_number = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    checkout_date = db.Column(db.DateTime(timezone=True))
    checkin_date = db.Column(db.DateTime(timezone=True))
    genre = db.Column(db.String(150))


class Customer(db.Model, UserMixin):
    card_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    date_of_birth = db.Column(db.DateTime(timezone=True))
    books = db.relationship('Book')

class Employee(db.Model, UserMixin):
    emp_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    date_of_birth = db.Column(db.DateTime(timezone=True))
    hours_worked = db.Column(db.Integer)
    position = db.Column(db.String(150))
    #books = db.relationship('Book')

class Books_checked_out(db.Model):
    book_number = db.Column(db.Integer, foreign_key=True)
    card_id = db.Column(db.Integer, foreign_key=True)

class Author(db.Model):
    book_number = db.Column(db.Integer, foreign_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
