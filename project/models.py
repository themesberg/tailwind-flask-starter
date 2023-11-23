from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    dateOfBirth = db.Column(db.Date())

class Files(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    storageId=db.Column(db.Integer,unique=True)
    userUpload = db.Column(db.String(100))
    uploadDate = db.Column(db.Date())
    fileType = db.Column(db.String(100))
    metadataFile = db.Column(db.String(1000))