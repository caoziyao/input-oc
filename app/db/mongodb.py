# coding: utf-8

# 启动 mongod --config /usr/local/etc/mongod.conf
import os
from pymongo import MongoClient


host = 'localhost'
port = 27017
dbname = 'WebNote'


try:
    client = MongoClient(host, port)  # 连接 mongo 数据库, 主机是本机, 端口是默认的端口
    db = client[dbname]  # 直接这样就使用数据库了，相当于一个字典
except Exception as e:
    print('inti db error', e)

