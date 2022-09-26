from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    phone_number = db.Column(db.String(), unique=True, nullable=False)
    payment_method = db.Column(db.String(), nullable=False)


class VerifiedGuest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    phone_number = db.Column(db.String(), unique=True, nullable=False)
    payment_method = db.Column(db.String(), nullable=False)

class Review(db.Model):
    reviewer = db.Column(db.Integer, primary_key=True)
    star_rating = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_review = db.Column(db.String(140), unique=True, nullable=False)


class Listing(db.Model):
    owner = db.Column(db.String(), primary_key=True)
    location = db.Column(db.String(), primary_key=True)
    cost = db.Column(db.Integer, unique=True, nullable=False)
    past_guests = db.Column(db.String(), unique=True, nullable=False)
    reviews = db.Column(db.String(), unique=True, nullable=False)

db.create_all()

# add test user to database
db.session.add(User(username="user1", email="user1@example.com", phone_number="000-000-0000", payment_method="Credit"))
db.session.commit()

# add test verified guest to database
db.session.add(VerifiedGuest(username="guest1", email="guest1@example.com", phone_number="111-111-1111", payment_method="Cash"))
db.session.commit()

# add test review to database
db.session.add(Review(reviewer="guest1", star_rating=5, email="123@hotmail.com", user_review="very nice"))
db.session.commit()

# add test listing to database
db.session.add(Listing(owner="mark townsley", location="1 aberdeen", cost=250, past_guests="userid1,userid2" , reviews = "reviewid1,reviewid2"))
db.session.commit()

# test code for verifying entries in database
users = User.query.all()
guests = VerifiedGuest.query.all()
reviews = Review.query.all()
listings = Listing.query.all()

print("users:")
for i in users:
    print("id:", i.id)
    print("username:", i.username)
    print("email:", i.email)
    print("phone#:", i.phone_number)
    print("payment:", i.payment_method)

print("\nguests:")
for i in guests:
    print("id:", i.id)
    print("username:", i.username)
    print("email:", i.email)
    print("phone#:", i.phone_number)
    print("payment:", i.payment_method)

print("\nreviews:")
for i in reviews:
    print("reviewer:", i.reviewer)
    print("star rating:",i.star_rating)
    print("user review:", i.user_review)
    print("email:", i.email)

print("\nlistings:")
for i in listings:
    print("owner:", i.owner)
    print("location:", i.location)
    print("cost:", i.cost)