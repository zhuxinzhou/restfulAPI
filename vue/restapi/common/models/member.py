# coding: utf-8
from config.DB import db





class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    loginname = db.Column(db.String(20))
    password = db.Column(db.String(16))
