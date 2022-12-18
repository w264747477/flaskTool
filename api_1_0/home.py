

from api_1_0 import api
from tools._init_ import db
from flask import jsonify, request


@api.route('/indexImgs',methods=['GET'])
def getIndexImg():
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

