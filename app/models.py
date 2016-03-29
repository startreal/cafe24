# -*- coding: utf-8 -*-

from app import db

class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128))
    description = db.Column(db.Text)
    is24 = db.Column(db.BOOLEAN, nullable=False, default=False)
    x = db.Column(db.FLOAT)
    y = db.Column(db.FLOAT)
    thumUrl = db.Column(db.String(128))

    comment = db.relationship('Comment', backref='cafe')
    open_time_list = db.relationship('OpenTime', backref='cafe')
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'is24': self.is24,
            'description': self.description,
            'x': self.x,
            'y': self.y,
            'thumUrl': self.thumUrl,
            'openTime': [open_time.serialize for open_time in self.open_time_list]
        }

class OpenTime(db.Model):
    __tablename__ = 'open_time'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cafe_id = db.Column(db.Integer, db.ForeignKey('cafe.id'))
    label = db.Column(db.String(64))
    time = db.Column(db.String(64))

    @property
    def serialize(self):
        return {
            'label': self.label,
            'time': self.time
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