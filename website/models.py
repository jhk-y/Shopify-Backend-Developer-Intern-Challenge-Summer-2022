from enum import unique
from . import db 

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)
    quantity = db.Column(db.Integer)
