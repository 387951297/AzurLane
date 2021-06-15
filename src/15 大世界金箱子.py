from util import *
from const import const

path = const.publicPath() + 'operation/'

# 信标100/100步骤
def beaconProcess():
    util.logOut(__file__,'------------信标100/100开始-----------')
    x , y = const.picLoop(path + 'intelligence.jpg')
    util.click(x, y)
    x , y = const.picLoop(path + 'help.jpg')
    util.click(x, y)
    x , y = const.picLoop(path + 'help1.jpg')
    util.click(x, y)
    x , y = const.picLoop(path + 'help2.jpg')
    util.click(x, y)
    x , y = const.picLoop(path + 'help3.jpg')
    util.click(x, y)
    x , y = const.picLoop(path + 'OK_ask.jpg')
    util.click(x, y)
    while util.isFindPic(const.publicPath() + 'beacon/batile start.jpg'):
        x, y = const.picLoop(const.publicPath() + 'beacon/batile start.jpg')
        util.click(x, y)

        util.logOut(__file__,'今日不再提示判断 开始')
        def noTip():
            util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/anchor.bmp')
            util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/quit.jpg')
            for i in range(600):
                x, y = util.findPic(const.publicPath() + 'bmp/anchor.bmp', threshold=0.8, size=(0, 0, 0, 0))
                if x != -1 and y != -1:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/anchor.bmp')
                    util.click(x,y)
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

        x, y = const.picLoop(const.publicPath() + 'beacon/ok.jpg')
        util.click(x,y)
        const.picLoop(const.publicPath() + 'beacon/beacon list.jpg')

    x , y = const.picLoop(path + 'collect_beward.jpg')
    util.click(x, y)
    x , y = const.picLoop(const.publicPath() + 'bmp/get_items.bmp')
    util.click(x, y)
    x , y = const.picLoop(path + 'back.jpg')
    util.click(x, y)
    util.logOut(__file__,'------------信标100/100结束-----------')

# 金箱子出击步骤
def goldenBoxProcess():
    util.logOut(__file__,'------------金箱子出击开始-----------')
    x, y = const.picLoop(path + 'enter_sea.jpg')
    util.click(x, y)
    time.sleep(4)
    util.logOut(__file__,'------------判断行动力 开始-----------')
    if util.isFindPic(path + 'use.jpg'):
        util.logOut(__file__,'------------行动力不足-----------')
        x, y = const.picLoop(path + 'use.jpg')
        util.click(x, y)
        util.click(x, y)
        util.click(x, y)
        util.click(x, y)
        util.click(x, y)
        x, y = const.picLoop(const.publicPath() + 'bmp/quit.jpg')
        util.click(x, y)
        x, y = const.picLoop(path + 'enter_sea.jpg')
        util.click(x, y)

    const.picLoop(const.publicPath() + 'beacon/overview.jpg')
    time.sleep(4)
    util.click(695, 125)
    x, y = const.picLoop(path + 'airspace.jpg')
    util.click(x, y)
    x, y = const.picLoop(const.publicPath() + 'bmp/OK.jpg')
    util.click(x, y)
    time.sleep(4)
    util.logOut(__file__,'------------判断行动力 开始-----------')
    if util.isFindPic(path + 'use.jpg'):
        util.logOut(__file__,'------------行动力不足-----------')
        x, y = const.picLoop(path + 'use.jpg')
        util.click(x, y)
        util.click(x, y)
        util.click(x, y)
        util.click(x, y)
        util.click(x, y)
        x, y = const.picLoop(const.publicPath() + 'bmp/quit.jpg')
        util.click(x, y)
        time.sleep(4)
        util.click(695, 125)
        x, y = const.picLoop(path + 'airspace.jpg')
        util.click(x, y)
        x, y = const.picLoop(const.publicPath() + 'bmp/OK.jpg')
        util.click(x, y)
    x, y = const.picLoop(const.publicPath() + 'bmp/zilv.jpg')
    time.sleep(2)
    util.click(x, y)

    def aOrB():
        util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/OK.jpg')
        util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/leave.jpg')
        for i in range(600):
            x, y = util.findPic(const.publicPath() + 'bmp/OK.jpg', threshold=0.8, size=(0, 0, 0, 0))
            if x != -1 and y != -1:
                util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/OK.jpg')
                util.click(x, y)
                beaconProcess()
                x , y = const.picLoop(const.publicPath() + 'bmp/leave.jpg')
                util.click(x, y)
                x , y = const.picLoop(const.publicPath() + 'bmp/zilv.jpg')
                time.sleep(4)
                util.click(x, y)
                aOrB()
                return
            x, y = util.findPic(const.publicPath() + 'bmp/leave.jpg', threshold=0.8, size=(0, 0, 0, 0))
            if x != -1 and y != -1:
                util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/leave.jpg')
                util.click(x, y)
                x, y = const.picLoop(path + 'exit.jpg')
                util.click(x, y)
                x, y = const.picLoop(const.publicPath() + 'bmp/OK.jpg')
                util.click(x, y)
                time.sleep(2)
                util.click(433, 462)
                return
        util.logOut(__file__,'picLoop没找到图 需要重启脚本！！！！！！')
        const.restartProcess()
        raise ValueError('restart')

    aOrB()
    util.logOut(__file__,'------------金箱子出击结束-----------')

def main():
    time.sleep(2)
    util.logOut(__file__,'大世界每日 开始')

    #返回主页面
    const.backMainProcess()
    #进入出击界面
    x , y = const.picLoop(const.publicPath() + 'bmp/weigh anchor.jpg')
    util.click(x,y)
    x , y = const.picLoop(const.publicPath() + 'beacon/operation.jpg')
    util.click(x,y)

    # 出击金箱子
    util.logOut(__file__,'------------出击金箱子开始-----------')
    x, y = const.picLoop(path + 'box.jpg')
    util.click(x, y)
    const.picLoop(path + 'is_box.jpg')

    while util.isFindPic(path + 'golden_box.jpg'):
        x, y = const.picLoop(path + 'golden_box.jpg')
        util.click(x, y)
        x, y = const.picLoop(path + 'check.jpg')
        util.click(x, y)
        time.sleep(2)
        goldenBoxProcess()
        const.picLoop(const.publicPath() + 'beacon/overview.jpg')
        x, y = const.picLoop(path + 'box.jpg')
        util.click(x, y)
        const.picLoop(path + 'is_box.jpg')
        
    x, y = const.picLoop(const.publicPath() + 'bmp/back.jpg')
    util.click(x, y)
    const.picLoop(const.publicPath() + 'beacon/overview.jpg')
    util.logOut(__file__,'------------出击金箱子结束-----------')
    
    # 返回主页
    const.backMainProcess()
