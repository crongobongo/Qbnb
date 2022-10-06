# from qbnb import app
from app import db
# from flask_sqlalchemy import SQLAlchemy


'''
This file defines data models and related business logics
'''




class User(db.Model):
    # may need to edit these eg. password should probably not be db.string()
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    billing_address = db.Column(db.String(), unique=True, nullable=False)
    postal_code = db.Column(db.String(), unique=True, nullable=False)
    balance = db.Column(db.Integer(), nullable=False)


class VerifiedGuest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    phone_number = db.Column(db.String(), unique=True, nullable=False)
    payment_method = db.Column(db.String(), nullable=False)


class Review(db.Model):
    # may need to edit these
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(), primary_key=True)
    listing_id = db.Column(db.String(), primary_key=True)
    review_text = db.Column(db.String(), primary_key=True)
    date = db.Column(db.String(), primary_key=True)


class Listing(db.Model):
    # may need to edit these, eg. not sure about owner_id?
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), primary_key=True)
    description = db.Column(db.String(), primary_key=True)
    price = db.Column(db.Integer, unique=True, nullable=False)
    last_modified_date = db.Column(db.String(), unique=True, nullable=False)
    owner_id = db.Column(db.String(), primary_key=True)


class Booking(db.Model):
    # may need to edit these, eg. not sure about user_id?
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(), primary_key=True)
    listing_id = db.Column(db.String(), primary_key=True)
    price = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.String(), unique=True, nullable=False)


db.create_all()

# db = SQLAlchemy(app)


# class User(db.Model):
#     username = db.Column(
#         db.String(80), nullable=False)
#     email = db.Column(
#         db.String(120), unique=True, nullable=False,
#         primary_key=True)
#     password = db.Column(
#         db.String(120), nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username


# # create all tables
# db.create_all()


# def register(name, email, password):
#     '''
#     Register a new user
#       Parameters:
#         name (string):     user name
#         email (string):    user email
#         password (string): user password
#       Returns:
#         True if registration succeeded otherwise False
#     '''
#     # check if the email has been used:
#     existed = User.query.filter_by(email=email).all()
#     if len(existed) > 0:
#         return False

#     # create a new user
#     user = User(username=name, email=email, password=password)
#     # add it to the current database session
#     db.session.add(user)
#     # actually save the user object
#     db.session.commit()

#     return True


# def login(email, password):
#     '''
#     Check login information
#       Parameters:
#         email (string):    user email
#         password (string): user password
#       Returns:
#         The user object if login succeeded otherwise None
#     '''
#     valids = User.query.filter_by(email=email, password=password).all()
#     if len(valids) != 1:
#         return None
#     return valids[0]
