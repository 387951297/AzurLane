from util import *
from const import const

def main():
    list = util.getWords((237, 201 , 627, 263))
    print(list[0])
    if '低心情' in list[0]:
        print('ok')

if __name__ == '__main__':
    print('adb初始化开始')
    util.adb('kill-server')
    util.adb('connect 127.0.0.1:7555')
    main()
