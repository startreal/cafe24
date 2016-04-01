# -*- coding: utf-8 -*-

from . import app, db
from flask import jsonify, request, session, render_template
from . import models
from models import Cafe, Comment, User, OpenTime
from . import cafe_crawler

@app.route('/')
def index():
    return jsonify({'results':'success'})


@app.route('/cafe', methods=['GET', 'POST'])
def cafe():
    if request.method == 'GET':
        cafe_list = Cafe.query.outerjoin(OpenTime).all()

        cafe_serialized_list = []
        for each_cafe in cafe_list:
            cafe_serialized_list.append(each_cafe.serialize)
        return jsonify({'results': cafe_serialized_list})
    elif request.method == 'POST':
        name = request.json.get('name')
        is24 = request.json.get('is24')
        lat = request.json.get('x')
        lng = request.json.get('y')

        cafe = Cafe(name=name, is24=is24, x=lat, y=lng)
        db.session.add(cafe)
        db.session.commit()
        return jsonify({'results':'success'})

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'GET':
        cafe = request.args.get('cafe')
        if cafe is not None:
            comment_list = Comment.query.join(Cafe).filter(Cafe.name == cafe).all()
        else:
            comment_list = Comment.query.all()
        comment_json_list = []
        for each_comment in comment_list:
            comment_json_list.append(each_comment.serialize)
        return jsonify({'results': comment_json_list})

    elif request.method == 'POST':
        content = request.json.get('content')
        cafe_id = request.json.get('cafe_id')
        comment = Comment(cafe_id=cafe_id, content=content, user_id=session['userid'])
        db.session.add(comment)
        db.session.commit()
        return jsonify({'results':'succses'})

@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method =='GET':
        user_list = User.query.all()
        user_json_list = []
        for each_user in user_list:
            user_json_list.append(each_user.serialize)
        return jsonify({'results':user_json_list})

    elif request.method == 'POST':
        userid = request.json.get('userid')
        password = request.json.get('password')
        user = User(userid=userid, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'results': 'success'})


@app.route('/login', methods=['POST'])
def login():
    userid = request.json.get('userid')
    password = request.json.get('password')
    user = User.query.filter_by(userid=userid, password=password).first()
    if user is None:
        return jsonify({'results':'fail'}), 402

    session['userid'] = user.userid
    return jsonify({'results':{
        'userid':user.userid
    }})

@app.route('/crawl')
def crawl_cafe():
    start_page = request.args.get('start_page')
    num = request.args.get('num')
    result_list = cafe_crawler.crawl(start_page, num)
    for each_cafe in result_list:
        cafe = Cafe(name=each_cafe['name'], address=each_cafe['roadAddress'], description=each_cafe['description'],
             x=each_cafe['x'], y=each_cafe['y'], thumUrl=each_cafe['thumUrl'])
        for each_open_time in each_cafe['open']:
            cafe.open_time_list.append(OpenTime(label=each_open_time['label'], time=each_open_time['time']))
        db.session.add(cafe)
        db.session.commit()
    return jsonify({'result': result_list})

@app.route('/map')
def map():
    cafe_list = Cafe.query.outerjoin(OpenTime).all()
    cafe_serialized_list = []
    for each_cafe in cafe_list:
        cafe_serialized_list.append(each_cafe.serialize)
    return render_template('map.html', cafeList=cafe_serialized_list)