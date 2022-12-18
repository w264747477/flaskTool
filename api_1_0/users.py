import uuid

from flask_login import login_user

from api_1_0 import api
from tools._init_ import db
from flask import jsonify, request
from models import User

@api.route('/user/register',methods=['POST'])
def register():
   if User.query.filter_by(userName=request.json['userName']).first():
      return jsonify({'success': False, 'msg': '新建用户失败，用户名已存在！'})
   user = User()
   if 'userName' in request.json: user.userName = request.json['userName']
   if 'passWord' in request.json: user.passWord = request.json['passWord']
   user.id = str(uuid.uuid4())
   db.session.add(user)
   db.session.commit()
   return jsonify({'code': 200, 'msg': '新建用户成功！'})
   # db.session.add(user)
   # db.session.commit()
@api.route('/user/login',methods=['POST'])
def login():
   user = User.query.filter_by(userName=request.json['userName']).first()
   print(user.passWord)
   print(request.json['passWord'])
   if user is not None:
      # MD5加密后的内容同数据库密码比较
      if request.json['passWord'] == user.passWord:
         login_user(user)
         return jsonify({'msg': '登录成功~', 'code': 200, 'data' :{
            'expiresIn': 360000,
            'accessToken': str(uuid.uuid4())
         }})
   return jsonify({'msg': '登录失败,账号密码错误~', 'code': 500})
