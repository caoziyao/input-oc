from . import *


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


route_zhihu = {
    '/zhihu': index,
    '/api/zhihu/search': search,
    '/login': login,
}
