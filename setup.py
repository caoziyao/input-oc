# coding: utf-8
from subprocess import Popen



# 启动 mongodb
def start_mogodb():
    """ 启动 mogodb"""
    start_mogodb_cmd = 'mongod --config /usr/local/etc/mongod.conf'
    Popen(start_mogodb_cmd, shell=True)




def start():
    start_mogodb()


if __name__ == '__main__':
    start()