from qbnb import app
from flask_sqlalchemy import SQLAlchemy


'''
This file defines data models and related business logics
'''

db = SQLAlchemy(app)

class User(db.Model):
    # may need to edit these eg. password should probably not be db.string()
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
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

# email = db.Column(db.String(), unique=True, nullable=False)
#     password = db.Column(db.String(), nullable=False)
#     username = db.Column(db.String(), unique=True, nullable=False)
#     billing_address = db.Column(db.String(), unique=True, nullable=False)
#     postal_code = db.Column(db.String(), unique=True, nullable=False)
#     balance

# test users for login
db.session.add(User(email="cheese@email.com", password="123", username="cheese", billing_address="000", postal_code="000", balance="000"))
db.session.commit()

def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
# R1-3: The email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation). You can use external libraries/imports.
# R1-4: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.

    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]

# register("cheese", "cheese@email.com", "123")
print(login("cheese@email.com", "123"))

def update_user(old_email, username, new_email, billing_address, postal_code):

    user = User.query.filter_by(email=old_email).first()

    edited = 0

    if username is not None:
        user.username = username
        edited += 1
        db.session.commit()
    if new_email is not None:
        user.email = new_email
        edited += 1
        db.session.commit()
    if billing_address is not None:
        user.billing_address = billing_address
        edited += 1
        db.session.commit()
    if postal_code is not None:
        user.postal_code = postal_code
        edited += 1
        db.session.commit()
    # prob need to check for errors...
    if edited == 0:
        return None
    return user

print(update_user("cheese@email.com", "jeans", None, None, None))

    # R3-1: A user is only able to update his/her user name, user email, billing address, and postal code.
    # R3-2: postal code should be non-empty, alphanumeric-only, and no special characters such as !.
    # R3-3: Postal code has to be a valid Canadian postal code.
    # R3-4: User name follows the requirements above.


