

# 启动 mongod --config /usr/local/etc/mongod.conf
import os
from pymongo import MongoClient
from util import json_save
from util import json_loads

# 引入数据库配置文件
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'constant', 'config.txt'))
data = json_loads(config_path)
host = data.get('mongodb').get('dataurl')
port = data.get('mongodb').get('dataport')
dbname = data.get('mongodb').get('dataname')

# 连接 mongo 数据库, 主机是本机, 端口是默认的端口
# 也可以 MongoClient('mongodb://localhost:27017/')
try:
    client = MongoClient(host, port)    # 连接 mongo 数据库, 主机是本机, 端口是默认的端口
    db = client[dbname] # 直接这样就使用数据库了，相当于一个字典
except Exception as e:
    print('db error')

def selectall(collection):
    """
    selectall 方法返回全部所有数据
    :return:
    """
    try:
        col = db[collection]
        # col = db.get_collection('user')
        return col.find()      # find 返回一个可迭代对象，是一个生成器。使用 list 函数转为数组
    except Exception as e:
        print('selectall error', e)
        return None


def selectone(collection, query=None):
    """
    selectone 查询符合条件的数据
    :return:
    """
    try:
        col = db[collection]
        return col.find_one(query)
    except Exception as e:
        print('selectall error', e)
        return None


def insert(collection, query):
    """
    insert 添加数据格式json格式
    :return:
    """
    try:
        col = db[collection]
        return col.insert(query)
    except Exception as e:
        print('selectall error', e)
        return None


def update():
    """
    update 修改数据的方法
    :return:
    """
    pass

def remove():
    """
    remove 删除数据的方法
    :return:
    """
    pass

def removeall():
    """
    removeall 删除全部数据的方法
    :return:
    """
    pass