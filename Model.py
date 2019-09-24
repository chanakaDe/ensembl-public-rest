from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint

ma = Marshmallow()
db = SQLAlchemy()

class Gene(db.Model):
    __tablename__ = 'gene_autocomplete'
    __table_args__ = (
        PrimaryKeyConstraint('species', 'stable_id', 'display_label','location'),
    )
    species = db.Column(db.String(200), nullable=True)
    stable_id = db.Column(db.String(200), nullable=False)
    display_label = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    db = db.Column(db.String(200), nullable=False)

    def __init__(self, species,stable_id,display_label,location):
        self.species = species
        self.stable_id = stable_id
        self.display_label = display_label
        self.location = location
        self.db = db

class GeneSchema(ma.Schema):
    species = fields.String(required=True)
    stable_id = fields.String(required=True)
    display_label = fields.String(required=True)
    location = fields.String(required=True)
    db = fields.String(required=True)
