#database models
#1 for users
#1 for notes

from . import db #importing from the current package (the website folder)
from flask_login import UserMixin
from sqlalchemy.sql import func #gets current date and time for new note object

#schema for database
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #referencing the primary key in the user table


#schema for database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) #unique= no user can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #tells flask and sqlalchemy everytime a note is created add the note id


