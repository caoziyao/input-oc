
from . import *

def route_static(request):
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    filename = request.query.get('file', '')
    path = 'static/' + filename
    with open(path, 'r') as f:
        content = f.read()
        return http_response(content)



def index(request):
    body = tempalte('index.html')

    return http_response(body)

route_zhihu = {
    '/zhihu': index
}
