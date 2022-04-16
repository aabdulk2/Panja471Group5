from turtle import position
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Customer, Employee
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
import sqlite3

from website.models import Customer


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Customer.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
               flash('Logged in successfully!', category='success')
               login_user(user, remember=True)
               return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)



@auth.route('/login-employee', methods=['GET', 'POST'])
def login_employee():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Employee.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
               flash('Logged in successfully!', category='success')
               login_user(user, remember=True)
               return redirect(url_for('views.home'))   #Change this 
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("loginEmployee.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        address = request.form.get('address')
        phone_number = request.form.get('phoneNumber')
        date_of_birth_str = request.form.get('dateOfBirth')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        
        user = Customer.query.filter_by(email=email).first()
        if user:
           flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 2:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #date_of_birth = datetime.strptime(date_of_birth_str,  '%yyyy-%mm-%dd')
            #date_of_birth = datetime.date(datetime(date_of_birth_str))
            new_user = Customer(email=email, first_name=first_name, last_name=last_name, 
                                address=address, password=generate_password_hash(
                                password1, method='sha256'), phone_number=phone_number)
                                #date_of_birth=date_of_birth#
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/sign-up-employee', methods=['GET', 'POST'])
def sign_up_employee():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        address = request.form.get('address')
        position = request.form.get('position')
        phone_number = request.form.get('phoneNumber')
        date_of_birth_str = request.form.get('dateOfBirth')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        
        user = Employee.query.filter_by(email=email).first()
        if user:
           flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 2:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #date_of_birth = datetime.strptime(date_of_birth_str,  '%yyyy-%mm-%dd')
            #date_of_birth = datetime.date(datetime(date_of_birth_str))
            new_user = Employee(email=email, first_name=first_name, last_name=last_name, 
                                address=address, password=generate_password_hash(
                                password1, method='sha256'), phone_number=phone_number, 
                                position=position, hours_worked=0)
                                #date_of_birth=date_of_birth#
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))           #TO-DO change later

    return render_template("sign_up_employee.html", user=current_user)