
from . import *
import requests
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


def weather(request):
    url = 'https://free-api.heweather.com/v5/weather?city=深圳&key=79edc4edd72c4d89a70cd117483fa451'

    res = yrequests.get(url)
    w = json.loads(res)

    data = {
        'basic': w.get('HeWeather5')[0].get('basic'),
        'now': w.get('HeWeather5')[0].get('now'),
        'daily_forecast': w.get('HeWeather5')[0].get('daily_forecast')[0],
        'hourly_forecast': w.get('HeWeather5')[0].get('hourly_forecast')[0]
    }

    # print('text', r.text)
    body = tempalte('index.html', weather=data)
    return http_response(body)

route_zhihu = {
    '/zhihu': index,
    '/api/zhihu/search': search,
    '/weather': weather,
}
