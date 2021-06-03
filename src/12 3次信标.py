from util import *
from const import const

path = const.publicPath() + 'beacon/'

def main():
    time.sleep(2)
    util.logOut(__file__,'3次飞龙 开始')

    #返回主页面
    const.backMainProcess()
    #进入出击界面
    x , y = const.picLoop(const.publicPath() + 'bmp/weigh anchor.jpg')
    util.click(x,y)
    x , y = const.picLoop(path + 'operation.jpg')
    util.click(x,y)
    x , y = const.picLoop(path + 'overview.jpg')
    time.sleep(2)
    util.click(x,y)
    x , y = const.picLoop(path + 'ash.jpg')
    time.sleep(2)
    util.click(x,y)
    x , y = const.picLoop(path + 'beacon list.jpg')
    util.click(x,y)

    # 判断还剩几次
    cnt = 3 # 默认三次
    list = util.getNumbers((726, 9, 757, 39))
    if list != []:
        cnt = int(list[0][0])

    for n in range(cnt):
        util.logOut(__file__,'------------一把开始-----------')
        x , y = const.picLoop(path + 'batile start.jpg')
        util.click(x,y)

        def noTip():
            util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/anchor.bmp')
            util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/quit.jpg')
            for i in range(600):
                x, y = util.findPic(const.publicPath() + 'bmp/anchor.bmp', threshold=0.8, size=(0, 0, 0, 0))
                if x != -1 and y != -1:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/anchor.bmp')
                    return
                x, y = util.findPic(const.publicPath() + 'bmp/quit.jpg', threshold=0.8, size=(0, 0, 0, 0))
                if x != -1 and y != -1:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/quit.jpg')
                    util.click(x,y)
                    util.logOut(__file__,'今日不再提示')
                    return
            util.logOut(__file__,'picLoop没找到图 需要重启脚本！！！！！！')
            const.restartProcess()
            raise ValueError('restart')

        noTip()

        x , y = const.picLoop(path + 'weigh anchor.jpg')
        util.click(x,y)
        x , y = const.picLoop(const.publicPath() + 'bmp/get_items.bmp')
        util.click(x,y)
        x , y = const.picLoop(path + 'ok.jpg')
        util.click(x,y)
        util.logOut(__file__,'------------一把结束-----------')
    #返回主页面
    time.sleep(2)
    util.logOut(__file__,'backMainProcess 返回主页面开始')
    if util.isFindPic(path + 'beacon_home.jpg',0.8):
        x , y = util.findPic(path + 'beacon_home.jpg',0.8)
        util.click(x,y)
        time.sleep(.500)
    elif util.isFindPic(const.publicPath() + 'bmp/weigh anchor.jpg'):
        util.logOut(__file__,'backMainProcess 返回主页面结束')
        return
    else:
        util.logOut(__file__,'backMainProcess 返回主页面结束 失败')
