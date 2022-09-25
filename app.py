from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


# edit this to make it properly suit user entity
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)


# need to edit to make it properly suit guest entity
class VerifiedGuest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)


class Review(db.Model):
    reviewer = db.Column(db.Integer, primary_key=True)
    star_rating = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_review = db.Column(db.String(140), unique=True, nullable=False)


db.create_all()

# add test user to database
db.session.add(User(username="user1", email="user1@example.com"))
db.session.commit()

# add test verified guest to database
db.session.add(VerifiedGuest(username="guest1", email="guest1@example.com"))
db.session.commit()

# add test review to database
db.session.add(Review(reviewer="guest1", star_rating=5))
db.session.commit()

# test code for verifying entries in database
users = User.query.all()
guests = VerifiedGuest.query.all()
reviews = Review.query.all()

print("users:")
for i in users:
    print("id:", i.id)
    print("username:", i.username)
    print("email:",i.email)

print("\nguests:")
for i in guests:
    print("id:", i.id)
    print("username:", i.username)
    print("email:",i.email)

print("\nreviews:")
for i in reviews:
    print("id:", i.id)
    print("reviewer:", i.reviewer)
    print("star rating:",i.star_rating)