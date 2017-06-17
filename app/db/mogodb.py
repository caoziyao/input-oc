# coding: utf-8

# 启动 mongod --config /usr/local/etc/mongod.conf
import os
from pymongo import MongoClient


host = 'localhost'
port = 27017
dbname = 'WebNote'

# 连接 mongo 数据库, 主机是本机, 端口是默认的端口
# 也可以 MongoClient('mongodb://localhost:27017/')
# log('开始连接数据库 mongodb://{}:{}/{}'.format(host, port, dbname))
try:
    client = MongoClient(host, port)  # 连接 mongo 数据库, 主机是本机, 端口是默认的端口
    db = client[dbname]  # 直接这样就使用数据库了，相当于一个字典
except Exception as e:
    print('inti db error', e)


# log('连接数据库成功')


class Mainpulation:
    """
    mongodb 操作对象
    """

    def __init__(self, collectionname):
        """
        :param collection:
        :return:
        """
        self.collection = db[collectionname]

    def findall(self):
        """
        selectall 方法返回全部所有数据
        :return:
        """
        try:
            # col = db.get_collection('user')
            return self.collection.find()  # find 返回一个可迭代对象，是一个生成器。使用 list 函数转为数组
        except Exception as e:
            print('selectall error', e)
            return None

    def findone(self, query=None):
        """
        selectone 查询符合条件的数据
        :return:
        """
        try:
            return self.collection.find_one(query)
        except Exception as e:
            print('selectone error', e)
            return None

    def findquery(self, query, projection=None):
        """

        :param query:
        :return:
        """
        try:
            print(query, projection)
            return self.collection.find(query, projection=None)
        except Exception as e:
            print('selectone error', e)
            return None

    def findone_by_id(self):
        """
        通过 objectid 来查找
        :param collection:
        :return:
        """
        try:
            obj = self.collection.find_one()
            obj_id = obj['_id']
            pass
        except Exception as e:
            print('selectone by id error', e)
            return None

    def insert(self, query):
        """
        insert 添加数据格式json格式
        :return:
        """
        try:
            return self.collection.insert(query)
        except Exception as e:
            print('selectall error', e)
            return None

    def update(self, query, newdata):
        """
        update方法的第一个参数为“查找的条件”，第二个参数为“更新的值”
        update 修改数据的方法
        :return:
        """
        try:
            return self.collection.update(query, newdata)
        except Exception as e:
            print('selectall error', e)
            return None

    def remove(self, query):
        """
        remove 删除数据的方法
        :return:
        """
        try:
            return self.collection.remove(query)
        except Exception as e:
            print('selectall error', e)
            return None

    def removeall(self):
        """
        removeall 删除全部数据的方法
        :return:
        """
        try:
            return self.collection.remove()
        except Exception as e:
            print('selectall error', e)
            return None

dbtags = Mainpulation('tags')
dbnotes = Mainpulation('notes')
dbcontent = Mainpulation('content')
dbsequence = Mainpulation('sequence')