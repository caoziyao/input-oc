

from . import *
import lib.yrequests as yrequests


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

route_api = {
    '/api/weather': weather,
}