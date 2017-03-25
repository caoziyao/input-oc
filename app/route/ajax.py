
from . import *

def login(request):
    """ ajax 登录"""
    # headers = {'Content-Type', 'application/json'}

    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')
        if not username or not password:
            raise Assistant(msg='请输入用户名或密码')
        data = {
            'username': username
        }
        res = dbuser.findone(data)
        if not res:
            raise Assistant('用户不存在')
        upasswd = res.get('password', '')
        if password != upasswd:
            raise Assistant(msg='密码错误')
            # return redirect('/zhihu')
        r = {
            'status': 1,
            'msg': 'welcome 登录成功!'
        }
        body = json.dumps(r)
        return http_response(body)
    except Assistant as e:
        body = json.dumps(e.__dict__)
        return http_response(body)
    except Exception as e:
        r = {
            'suatus': 0,
            'msg': ' 接口错误'
        }
        body = json.dumps(r)
        return http_response(body)


def register(request):
    """ ajax 注册"""
    # headers = {'Content-Type', 'application/json'}

    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')
        if len(username) < 3 or len(password) < 3:
            raise Assistant(msg='用户名或密码至少3位')

        data = {
            'username': username,
            'password': password
        }
        if dbuser.findone({'username': username}):
            raise Assistant(msg='用户名已存在')

        dbuser.insert(data)
        r = {
            'status': 1,
            'msg': 'welcome 注册成功!'
        }
        body = json.dumps(r)
        return http_response(body)
    except Assistant as e:
        body = json.dumps(e.__dict__)
        return http_response(body)
    except Exception as e:
        r = {
            'suatus': 0,
            'msg': ' 接口错误'
        }
        body = json.dumps(r)
        return http_response(body)


route_ajax = {
    '/ajax/login': login,
    '/ajax/register': register,
}