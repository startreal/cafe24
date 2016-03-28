# -*- coding: utf-8 -*-

from app import db

class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    is24 = db.Column(db.BOOLEAN, nullable=False)
    lat = db.Column(db.FLOAT)
    lng = db.Column(db.FLOAT)

    comment = db.relationship('Comment', backref='cafe')
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'is24': self.is24,
            'lat': self.lat,
            'lng': self.lng
        }


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String(128), nullable=False)
    cafe_id = db.Column(db.Integer, db.ForeignKey('cafe.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id
        }


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    userid = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'userid': self.userid,
            'password': self.password
        }