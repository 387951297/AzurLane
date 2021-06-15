from util import *
from const import const
import importlib
import sys
import os
import ctypes
import traceback
import time
sys.path.append(os.getcwd().replace('\\', '/')+'/src')

def main():
    m = ['' for _ in range(100)]
    # 引用带数字的py模组
    for fileName in os.listdir('./src'):
        num = ''
        try:
            num = int(fileName[0:2])
            m[num] = importlib.import_module(
                fileName.replace('.py', ''))
            continue
        except ValueError:
            pass
        try:
            num = int(fileName[0])
            m[num] = importlib.import_module(
                fileName.replace('.py', ''))
            continue
        except ValueError:
            pass
    m[12].main()
    time.sleep(2.000)
    m[2].main()
    time.sleep(2.000)
    m[3].main()
    time.sleep(2.000)
    m[14].main()
    time.sleep(2.000)
    

if __name__ == '__main__':
    main()
