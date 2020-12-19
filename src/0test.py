from util import *
from const import const



def main():
    # 初始化
    util.adb('kill-server')
    util.adb('connect 127.0.0.1:7555')
    # 截图
    # adb('shell screencap /storage/emulated/0/data/screen/image.png')
    # adb('pull /storage/emulated/0/data/screen/image.png .\\tmp')
    # adb('shell rm -rf /storage/emulated/0/data/screen/image.png')
    #点击
    # util.adb('shell input tap 200 200')
    const.backMainProcess()




if __name__ == '__main__':
    main()
