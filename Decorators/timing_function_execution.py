import time

def timer(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return 