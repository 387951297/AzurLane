from util import *
from const import const

path = const.publicPath() + 'operation/'

def main():
    util.adb('shell input swipe 637 141 228 406')
    util.adb('shell input swipe 637 141 228 406')
    util.adb('shell input swipe 637 141 228 406')
    util.adb('shell input swipe 228 406 228 141')
    x , y = const.picLoop(path + 'port_inside4.jpg')
    util.click(x, y)
    input()
    

if __name__ == '__main__':
    print('adb初始化开始')
    util.adb('kill-server')
    util.adb('connect 127.0.0.1:7555')
    main()
    
