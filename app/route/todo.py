
from util import http_response
from util import tempalte

def todo(request):
    """todo 主页面"""
    body = tempalte('todo.html', user='root')

    return http_response(body)


route_todo = {
    '/todo': todo
}