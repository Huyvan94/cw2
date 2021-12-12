
from app import app, db, admin
from sqlalchemy.orm import backref
from flask_admin.contrib.sqla import ModelView 

interstedFilm = db.Table('interstedFilms',
db.Column('accountID',db.Integer,db.ForeignKey('Account.id')),
db.Column('filmID',db.Integer,db.ForeignKey('films.id')))

class Account(db.Model):
    __tablename__='Account'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    fname= db.Column(db.String(100))
    lname= db.Column(db.String(100))
    dob = db.Column(db.Date)
    gender= db.Column(db.String(10))
    interested = db.relationship('films', 
        secondary = interstedFilm, 
        backref  = db.backref('interest', lazy = 'dynamic'))

class films(db.Model):
    __tablename__='films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    length = db.Column(db.Integer)
    genre = db.Column(db.String(100))

admin.add_view(ModelView(Account, db.session))
admin.add_view(ModelView(films, db.session))