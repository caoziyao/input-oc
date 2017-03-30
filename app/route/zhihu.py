from . import *
from .login import session, User, curr_user, login_required

def route_static(request):
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    filename = request.query.get('file', '')
    path = 'static/' + filename
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        return http_response(content)


# @login_required
def index(request):
    user = curr_user(request)
    if user:
        username = user.username
    else:
        username = '游客'
    body = tempalte('index.html', username=username)
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
