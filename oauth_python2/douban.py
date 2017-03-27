# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

import urllib
import urllib2


API_KEY = "your api key "  # get it from here http://developers.douban.com/apikey/
SECRET = "your secret"  # get it from here http://developers.douban.com/apikey/
GET_CODE_URL = "https://www.douban.com/service/auth2/auth"
GET_TOKEN_URL = "https://www.douban.com/service/auth2/token"
CODE_REDIRECT_URL = "http://127.0.0.1:8000/douban_code_callback/"
TOKEN_REDIRECT_URL = "http://127.0.0.1:8000/douban_token_callback/"
RESPONSE_TYPE_CHOICE_TOKEN = "token"
RESPONSE_TYPE_CHOICE_CODE = "code"
GRANT_TYPE = "authorization_code"


def authorization_code():
    params = {
        "client_id": API_KEY,
        "redirect_uri": CODE_REDIRECT_URL,
        "response_type": RESPONSE_TYPE_CHOICE_CODE,
    }
    encode_params = urllib.urlencode(params)
    print GET_CODE_URL + "?" + encode_params


def get_the_code(url):
    temp = url.split("code=")
    return temp[1]


def access_token(code):
    params = {
        "client_id": API_KEY,
        "client_secret": SECRET,
        "redirect_uri": TOKEN_REDIRECT_URL,
        "grant_type": GRANT_TYPE,
        "code": code,
    }
    encode_params = urllib.urlencode(params)
    result = urllib2.urlopen(GET_TOKEN_URL, encode_params).read()
    result = result.rstrip('}').lstrip('{')
    pairs = result.split(",")
    token = pairs[0].split(":")[1][1:-1]
    print "The token is: " + token
    return token


def use_token(token):
    douban_request = urllib2.Request("https://api.douban.com/v2/user/~me")
    douban_request.add_header('Authorization', 'Bearer ' + token)
    response = urllib2.urlopen(douban_request).read()
    print response


if __name__ == '__main__':
    try:
        print ""
        print "Click the url below and copy the response url into your clipboard:"
        authorization_code()
        url = raw_input("Paste the url(it may seems like: 'http://127.0.0.1:8000/douban_code_callback"
                        "/?code=fc2ae3267ee3a95f') you just copied here:")
        code = get_the_code(url)
        print ""
        token = access_token(code)
        print ""
        print "Here is the user info:"
        use_token(token)
    except Exception, e:
        print "Some error occurred, see below for details."
        print e