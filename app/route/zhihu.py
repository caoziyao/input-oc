from . import *
import lib.yrequests as yrequests


def route_static(request):
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    filename = request.query.get('file', '')
    path = 'static/' + filename
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        return http_response(content)


def index(request):
    body = tempalte('index.html')
    return http_response(body)


def search(request):
    print('python search')
    body = json.dumps({'i': 'j'})
    return http_response(body)


def login(request):
    """用户登录
    """

    response = tempalte('login.html')
    return http_response(response)


def ajaxlogin(request):
    """ ajax 登录"""
    headers = {'Content-Type', 'application/json'}

    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')
        if len(username) < 3 or len(password) < 3:
            raise Assistant(msg='用户名或密码至少3位')
        r = {
            'status': 1,
            'msg': 'welcome 登录成功!'
        }
        body = json.dumps(r)
        return http_response(body)
    except Assistant as e:
        body = json.dumps(e.__dict__)
        return http_response(body, headers)
    except Exception as e:
        r = {
            'suatus': 0,
            'msg': ' 接口错误'
        }
        body = json.dumps(r)
        return http_response(body)


def ajaxregister(request):
    """ ajax 注册"""
    headers = {'Content-Type', 'application/json'}

    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')
        if len(username) < 3 or len(password) < 3:
            raise Assistant(msg='用户名或密码至少3位')
        r = {
            'status': 1,
            'msg': 'welcome 注册成功!'
        }
        body = json.dumps(r)
        return http_response(body)
    except Assistant as e:
        body = json.dumps(e.__dict__)
        return http_response(body, headers)
    except Exception as e:
        r = {
            'suatus': 0,
            'msg': ' 接口错误'
        }
        body = json.dumps(r)
        return http_response(body)




route_zhihu = {
    '/zhihu': index,
    '/api/zhihu/search': search,
    '/login': login,
    '/ajax/login': ajaxlogin,
    '/ajax/register': ajaxregister,
}
