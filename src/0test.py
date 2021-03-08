from util import *
from const import const

def main():
    chapterPos = (82, 43,141, 75)
    prevX , prevY = 33, 251
    nextX , nextY = 826, 251
    list = util.getNumbers(chapterPos)
    if len(list) != 0:
        print(list[0])

if __name__ == '__main__':
    print('adb初始化开始')
    util.adb('kill-server')
    util.adb('connect 127.0.0.1:7555')
    main()
