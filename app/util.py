import time, os, json
import datetime
from jinja2 import Environment, FileSystemLoader


def log(*args, **kwargs):
    """log 日志"""
    dt = datetime.datetime.now()
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'log', 'log.txt'))
    with open(path, 'a', encoding='utf-8') as f:
        print(dt, *args, **kwargs)
        print(dt, *args, file=f, **kwargs)


def json_save(path, data):
    """保持 json 格式字符串到文件"""
    data = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)


def json_loads(path):
    """从文件读取
    返回对象字典
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
        return json.loads(data)


# __file__ 就是本文件的名字
# 得到用于加载模板的目录
path = '{}/templates/'.format(os.path.dirname(__file__))
# 创建一个加载器, jinja2 会从这个目录中加载模板
loader = FileSystemLoader(path)
# 用加载器创建一个环境, 有了它才能读取模板文件
env = Environment(loader=loader)


def tempalte(path, **kwargs):
    """
    本函数接受一个路径和一系列参数
    读取模板并渲染返回
    """
    t = env.get_template(path)
    return t.render(**kwargs)


def http_response(body, headers=None):
    """
    headers 是可选的字典格式的 HTTP 头
    """
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    return header + '\r\n' + body


def error(code=404):
    body = tempalte('404.html')
    return http_response(body)
