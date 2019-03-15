import datetime
from fluid_contacts import db


class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String, nullable=False)
    starred = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
