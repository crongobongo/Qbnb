from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


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

# below commented out because it doesn't work with new class parameters

# # add test user to database
# db.session.add(User(username="user1", email="user1@example.com", phone_number="000-000-0000", payment_method="Credit"))
# db.session.commit()

# # add test verified guest to database
# db.session.add(VerifiedGuest(username="guest1", email="guest1@example.com", phone_number="111-111-1111", payment_method="Cash"))
# db.session.commit()

# # add test review to database
# db.session.add(Review(reviewer="guest1", star_rating=5, email="123@hotmail.com", user_review="very nice"))
# db.session.commit()

# # add test listing to database
# db.session.add(Listing(owner="mark townsley", location="1 aberdeen", cost=250, past_guests="userid1,userid2" , reviews = "reviewid1,reviewid2"))
# db.session.commit()

# # test code for verifying entries in database
# users = User.query.all()
# guests = VerifiedGuest.query.all()
# reviews = Review.query.all()
# listings = Listing.query.all()

# print("users:")
# for i in users:
#     print("id:", i.id)
#     print("username:", i.username)
#     print("email:", i.email)
#     print("phone#:", i.phone_number)
#     print("payment:", i.payment_method)

# print("\nguests:")
# for i in guests:
#     print("id:", i.id)
#     print("username:", i.username)
#     print("email:", i.email)
#     print("phone#:", i.phone_number)
#     print("payment:", i.payment_method)

# print("\nreviews:")
# for i in reviews:
#     print("reviewer:", i.reviewer)
#     print("star rating:",i.star_rating)
#     print("user review:", i.user_review)
#     print("email:", i.email)

# print("\nlistings:")
# for i in listings:
#     print("owner:", i.owner)
#     print("location:", i.location)
#     print("cost:", i.cost)