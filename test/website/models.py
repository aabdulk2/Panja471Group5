from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('customer.card_id'))

class Book(db.Model):
    book_number = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    checkout_date = db.Column(db.DateTime(timezone=True))
    checkin_date = db.Column(db.DateTime(timezone=True))
    checkout_customerID = db.Column(db.Integer, db.ForeignKey('customer.card_id'))
    genre = db.Column(db.String(150))


class Customer(db.Model, UserMixin):
    card_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    phone_number = db.Column(db.String(150))
    date_of_birth = db.Column(db.Date)
    def get_id(self):
        return (self.card_id)
    #books = db.relationship('Book', backref='Customer')

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
    id = db.Column(db.Integer, primary_key=True)
    book_number = db.Column(db.Integer, db.ForeignKey('book.book_number'))
    card_id = db.Column(db.Integer, db.ForeignKey('customer.card_id'))

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_number = db.Column(db.Integer, db.ForeignKey('book.book_number'))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
