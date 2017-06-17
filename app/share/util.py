# coding: utf-8

import hashlib


def sh1hexdigest(pwd):
    """
    摘要算法
    """
    salt = 'abcdefght'
    def sh1hex(ascii_str):
        return hashlib.sha1(ascii_str.encode('ascii')).hexdigest()
    s1 = sh1hex(pwd)
    s2 = sh1hex(s1 + salt)

    return s2


def  md5(pwd):
    """
    摘要算法
    :return:
    """
    m = hashlib.md5()
    m.update(pwd.encode('ascii'))
    r = m.hexdigest()

    return r