# coding: utf-8
__author__ = 'caosiyao'

# 思路：检测目录下的代码改动，一旦有改动，就自动重启服务器
# 利用watchdog接收文件变化的通知，如果是.py文件，就自动重启wsgiapp.py进程。
# 利用Python自带的subprocess实现进程的启动和终止，并把输入输出重定向到当前进程的输入输出中

import os, sys, time, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def log(*args, **kwargs):
    print('[Monitor]', *args, **kwargs)


class Handle(FileSystemEventHandler):
    def __init__(self, fn):
        super(Handle, self).__init__()
        self.restart = fn


    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed: {}'.format(event.src_path))
            self.restart()


def kill_process():
    pass

def start_process():
    pass


# 当有文件改动时，就会执行该函数
def restart_process():
    log('restarting process...')
    kill_process()
    start_process()


def start_watch(path, callback):
    observer = Observer()
    observer.schedule(Handle(restart_process), path, recursive=True)
    observer.start()
    log('Watching director {}...'.format(path))
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt as e:
        print('stop watching...')
        observer.stop()
    observer.join()


if __name__ == '__main__':
    path = os.path.abspath('.')
    start_watch(path, None)
