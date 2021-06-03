from util import *
from const import const

def main():
    if 'abc' not in 'abcd':
        print('not in')
    else:
        print('in')
    input()
    

if __name__ == '__main__':
    print('adb初始化开始')
    util.adb('kill-server')
    util.adb('connect 127.0.0.1:7555')
    main()
    
