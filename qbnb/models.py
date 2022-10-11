from qbnb import app
from flask_sqlalchemy import SQLAlchemy
import re
import email

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
    postal_code = db.Column(db.String(), nullable=False)
    balance = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


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

# R2-1: A user can log in using her/his email address and the password.
# R2-2: The login function should check if the supplied 
# inputs meet the same email/password requirements 
# as above, before checking the database.
def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    # R1-3: The email has to follow addr-spec defined in RFC 5322 
    # R1-4: Password has to meet the required complexity: minimum 
    # length 6, at least one upper case, at least one lower case,
    #  and at least one special character.

    email_regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]\
    +)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+\
    /-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    password_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[-+_\
    !@#$%^&*., ?])\S{6,}$")

    # check email and password requirements
    if not re.match(email_regex, email):
        return None
    if not re.match(password_regex, password):
        return None

    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]
    

# R3-1: A user is only able to update his/her user name, 
# user email, billing address, and postal code.
# R3-2: postal code should be non-empty, alphanumeric-only, 
# and no special characters such as !.
# R3-3: Postal code has to be a valid Canadian postal code.
# R3-4: User name follows the requirements R1-5, R1-6.
# R1-5: User name has to be non-empty, alphanumeric-only, 
# and space allowed only if it is not as the prefix or suffix.
# R1-6: User name has to be longer than 2 characters 
# and less than 20 characters.
def update_user(old_email, username, new_email, billing_address, postal_code):
    '''
    Update user information
      Parameters:
        old_email (string): users current email
        username (string): updated username
        new_email (string): updated email
        billing_address (string): updated billing address
        postal_code (string): updated postal code
      Returns:
        The user object if update succeeded otherwise None
    '''
    # checks to make sure user to be updated is a valid user
    user = User.query.filter_by(email=old_email).first()
    if user is None:
        return None
    edited = 0

    if postal_code:
        postal_spaceless = postal_code.replace(' ', '')
        if not re.match(r"[a-zA-Z][0-9][a-zA-Z][0-9][a-zA-Z][0-9]",
                        postal_spaceless):
            return None
        else:
            user.postal_code = postal_spaceless
            edited += 1
            db.session.commit()
    else:
        return None

    if username:
        if re.match(r"^[a-zA-Z0-9][a-zA-Z0-9 ]{1,17}[a-zA-Z0-9]$", username):
            user.username = username
            edited += 1
            db.session.commit()
        else:
            return None
    if new_email:
        user.email = new_email
        edited += 1
        db.session.commit()
    if billing_address:
        user.billing_address = billing_address
        edited += 1
        db.session.commit()

    if edited == 0:
        return None
    return user

