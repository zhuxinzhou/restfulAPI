from flask import Flask, request, jsonify
from common.models.member import Member
from flask_cors import CORS
app = Flask(__name__)




@app.route('/')

def hello_world():

 return 'Hello World!'

@app.route('/api/member/login', methods=["GET","POST"])
def login():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values

    name = req['name'] if 'name' in req else ''
    password = req['password'] if 'password' in req else 0



    if name is None or len( name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名"
        return jsonify( resp )

    if password is None or len( password) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的密码"
        return jsonify( resp )

    member_info = Member.query.filter_by(name=name).first()
    if not member_info:
        resp["code"] = -1
        resp["msg"] = "请输入正确的用户名和密码-1"
        return jsonify(resp)
    if member_info.password != password:
        resp["code"] = -1
        resp["msg"] = "请输入正确的用户名和密码-2"
        return jsonify(resp)
    else:
       resp['data']=member_info.id
    return jsonify(resp)


@app.route("/api/member/info", methods=["GET", "POST"])
def foodIndex():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values

    id = req['id'] if 'id' in req else ''
    if id:
        member_info = Member.query.filter_by(id = id).all()
    else:
        member_info = Member.query.all()

    member_info_list = []

    if member_info:
        for item in member_info:
            tmp_data = {
                'id': item.id,
                'name': item.name,
                'realname': item.loginname
            }
            member_info_list.append(tmp_data)
    resp['data']['member_list'] = member_info_list


    return jsonify(resp)



CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run()
