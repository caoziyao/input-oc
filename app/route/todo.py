
from . import *
from .login import User


def todo(request):
    """todo 主页面"""
    body = tempalte('todo.html', user='root')

    return http_response(body)


route_todo = {
    '/todo': todo
}