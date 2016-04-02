# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .cafe_crawl import CafeCrawler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entry_hims.db'
db = SQLAlchemy(app)
cafe_crawler = CafeCrawler()
app.config['SECRET_KEY'] = 'secret'
from . import views
