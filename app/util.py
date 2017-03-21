
import time

def log(*args, **kwargs):
    t = time.time()
    print(t, *args, **kwargs)


