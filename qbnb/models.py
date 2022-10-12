from qbnb import app
from flask_sqlalchemy import SQLAlchemy
import re
import datetime
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
    username = db.Column(db.String(), unique=False, nullable=False)
    billing_address = db.Column(db.String(), unique=False, nullable=False)
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


def register(name, email, password):
    # check that neither password or user is empty
    if (password is None) or (email is None):
        return False

    # check that email is valid
    email_regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]\
    +)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+\
    /-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    if not re.match(email_regex, email):
        return False
    
    # check password is valid
    password_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[-+_\
    !@#$%^&*., ?])\S{6,}$")
    if not re.match(password_regex, password):
        return False

    # check username is valid
    valid_name = True
    user_list = list(name)
    if ((len(name) <= 2) or (len(name) >= 20)):
        return False

    for i in range(len(user_list)):
        if (i == 0) or (i == len(user_list) - 1):
            if (user_list[i].isalnum() is False):
                valid_name = False
        else:
            if (user_list[i].isalnum() is not True) and (user_list[i] != ' '):
                valid_name = False

    if valid_name is False:
        return False

    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    # create a new user 
    # shipping address is empty, postal code is empty, balance = 100
     
    user = User(username=name, email=email, password=password, 
                billing_address='', postal_code='', balance=100)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


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

def create_listing(title_prod, desc_prod, price_prod, date, user_email):
    '''
    R4-1: The title of the product has to be alphanumeric-only,
          and space allowed only if it is not as prefix and suffix.
    R4-2: The title of the product is no longer than 80 characters.
    R4-3: The description of the product can be arbitrary characters,
          with a minimum length of 20 characters, 
          and a maximum of 2000 characters.
    R4-4: Description has to be longer than the product's title.
    R4-5: Price has to be of range [10, 10000].
    R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
    R4-7: owner_email cannot be empty. The owner of the corresponding product
          must exist in the database.
    R4-8: A user cannot create products that have the same title.
    '''
    # check if the title of the product meets the requirements
    if len(title_prod) <= 80:
        if title_prod[0] != " " and title_prod[-1] != " ":
            # go through each word and check that they are only alphanumerics
            title_check_regex = title_prod.split(" ")
            for word in title_check_regex:
                if not re.match(r'^[a-zA-Z0-9]+$', word):
                    return False
        else:
            return False
    else:
        return False
    
    # check that the description of the product meets the requirements
    if len(desc_prod) < len(title_prod):
        return False
    elif len(desc_prod) < 20 or len(desc_prod) > 2000:
        return False

    # price should be in range [10:10000]    
    if price_prod < 10 or price_prod > 10000:
        return False

    # Year-Month-Date check if valid
    try:
        # check that the date exists in the calender
        datetime.datetime.strptime(date, '%Y-%m-%d')

        # check that the year is between 2021 and 2025,
        # if so check that its valid
        if int(date[:4]) >= 2021 and int(date[:4]) <= 2025:
            if date[:4] == "2021" and date[5:7] == "01":
                if date[8:10] == "01":
                    return False

            elif date[:4] == "2025" and date[5:7] == "01":
                if date[8:10] != "01" or date[8:10] != "02":
                    return False                 
        else:
            return False
    except ValueError:
        return False

    # check owner id
    user = User.query.filter_by(email=user_email).first()
    title_exists = Listing.query.filter_by(title=title_prod).first()

    # check that the email isn't empty or does not exist in the database
    if user_email == " ":
        return False
    if user is None:
        return False
    # make sure the title hasn't been used before
    if not (title_exists is None):
        return False
    
    # if the listing requirements all pass, then add it to the
    # database and return True
    new_listing = Listing(title=title_prod, description=desc_prod, price=price_prod, last_modified_date=date, owner_id=user_email)
    db.session.add(new_listing)
    db.session.commit()
    return True