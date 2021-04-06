from datetime import datetime
import os

def log_decorator(func):
    def wrapper(*args):
        x = func(*args)
        filename = 'logs.txt'
        if os.path.exists(filename):
            append_write = 'a'
        else:
            append_write = 'w'
        writeLog = open(filename,append_write)
        writeLog.write('Timestamp: ' + str(datetime.now()) + ', value: ' + str(x) + ', args: ' + str([*args]) + '\n')
        writeLog.close()
        return x
    return wrapper

@log_decorator
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

@log_decorator
def printer(text):
    return (text + ', ' + text) ## MUST BE RETURN, OTHERWISE DOESN'T WORK W/ E.G. PRINT()