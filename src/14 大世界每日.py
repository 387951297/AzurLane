from util import *
from const import const

path = const.publicPath() + 'operation/'

# 接收任务步骤
def acceptTaskProcess():
    util.logOut(__file__,'------------接收任务开始-----------')
    x , y = const.picLoop(path + 'mission.jpg')
    util.click(x, y)
    time.sleep(4)
    while util.isFindPic(path + 'accept_task.jpg'):
        x , y = const.picLoop(path + 'accept_task.jpg')
        util.click(x, y)

    x , y = const.picLoop(const.publicPath() + 'bmp/back.jpg')
    util.click(x, y)
    const.picLoop(path + 'mission.jpg')
    x , y = const.picLoop(const.publicPath() + 'bmp/back.jpg')
    util.click(x, y)
    util.logOut(__file__,'------------接收任务结束-----------')

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

# 任务出击步骤
def missionProcess():
    util.logOut(__file__,'------------任务出击开始-----------')
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
    x, y = const.picLoop(const.publicPath() + 'bmp/zilv.jpg')
    time.sleep(4)
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
                return
        util.logOut(__file__,'picLoop没找到图 需要重启脚本！！！！！！')
        const.restartProcess()
        raise ValueError('restart')

    aOrB()
    util.logOut(__file__,'------------任务出击结束-----------')

# 左下NY港口领取任务
def getMission1Process():
    util.logOut(__file__,'------------左下NY港口领取任务开始-----------')
    x , y = const.picLoop(const.publicPath() + 'beacon/overview.jpg')
    time.sleep(2)
    util.click(x,y)
    x , y = const.picLoop(path + 'area_overview.jpg')
    util.click(x,y)
    time.sleep(2)
    util.click(227,345) # 左下角区域
    time.sleep(4)
    if util.isFindPic(path + 'return_sea.jpg'):
        util.logOut(__file__,'------------左下NY港口领取任务失败-----------')
        return False
    elif util.isFindPic(path + 'port1.jpg'):
        x , y = const.picLoop(path + 'port1.jpg')
        util.click(x,y)
        x , y = const.picLoop(path + 'enter_port.jpg')
        util.click(x,y)
        const.picLoop(const.publicPath() + 'beacon/overview.jpg')

        # NY走地图界面
        util.adb('shell input swipe 228 141 760 406')
        util.adb('shell input swipe 228 141 760 406')
        util.adb('shell input swipe 228 141 760 406')
        util.adb('shell input swipe 228 406 228 141')
        x , y = const.picLoop(path + 'port_inside1.jpg')
        util.click(x, y)
        x , y = const.picLoop(path + 'into_port.jpg')
        time.sleep(4)
        util.click(x, y)
        acceptTaskProcess()
    else:
        x , y = const.picLoop(path + 'back_home.jpg')
        util.click(x,y)
    util.logOut(__file__,'------------左下NY港口领取任务结束-----------')
    return True

# 右下角直布罗陀港口领取任务
def getMission2Process():
    util.logOut(__file__,'------------右下角直布罗陀港口领取任务开始-----------')
    x , y = const.picLoop(const.publicPath() + 'beacon/overview.jpg')
    time.sleep(2)
    util.click(x,y)
    x , y = const.picLoop(path + 'area_overview.jpg')
    util.click(x,y)
    time.sleep(2)
    util.click(448,387) # 右下角区域
    time.sleep(2)
    if util.isFindPic(path + 'port2.jpg'):
        x , y = const.picLoop(path + 'port2.jpg')
        util.click(x,y)
        x , y = const.picLoop(path + 'enter_port.jpg')
        util.click(x,y)

        const.picLoop(const.publicPath() + 'beacon/overview.jpg')

        # 直布罗陀走地图界面
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 228 406 637 141')
        x , y = const.picLoop(path + 'port_inside2.jpg')
        util.click(x, y)
        x , y = const.picLoop(path + 'into_port.jpg')
        time.sleep(4)
        util.click(x, y)
        acceptTaskProcess()
    else:
        x , y = const.picLoop(path + 'back_home.jpg')
        util.click(x,y)
    util.logOut(__file__,'------------右下角直布罗陀港口领取任务结束-----------')

# 右上角利物浦港口领取任务
def getMission3Process():
    util.logOut(__file__,'------------右上角利物浦港口领取任务开始-----------')
    x , y = const.picLoop(const.publicPath() + 'beacon/overview.jpg')
    time.sleep(2)
    util.click(x,y)
    x , y = const.picLoop(path + 'area_overview.jpg')
    util.click(x,y)
    time.sleep(2)
    util.click(507, 147) # 右上角区域
    time.sleep(2)
    if util.isFindPic(path + 'port3.jpg'):
        x , y = const.picLoop(path + 'port3.jpg')
        util.click(x,y)
        x , y = const.picLoop(path + 'enter_port.jpg')
        util.click(x,y)

        const.picLoop(const.publicPath() + 'beacon/overview.jpg')

        # 利物浦走地图界面
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 228 406 228 141')
        x , y = const.picLoop(path + 'port_inside3.jpg')
        util.click(x, y)
        x , y = const.picLoop(path + 'into_port.jpg')
        time.sleep(4)
        util.click(x, y)
        acceptTaskProcess()
    else:
        x , y = const.picLoop(path + 'back_home.jpg')
        util.click(x,y)
    util.logOut(__file__,'------------右上角利物浦港口领取任务结束-----------')

# 右上角圣彼得港口领取任务
def getMission4Process():
    util.logOut(__file__,'------------右上角圣彼得港口领取任务开始-----------')
    x , y = const.picLoop(const.publicPath() + 'beacon/overview.jpg')
    time.sleep(2)
    util.click(x,y)
    const.picLoop(path + 'area_overview.jpg')
    time.sleep(4)
    util.adb('shell input swipe 650 275 50 275')
    time.sleep(4)
    if util.isFindPic(path + 'port4.jpg'):
        x , y = const.picLoop(path + 'port4.jpg')
        util.click(x,y)
        x , y = const.picLoop(path + 'enter_port.jpg')
        util.click(x,y)

        const.picLoop(const.publicPath() + 'beacon/overview.jpg')

        # 圣彼得走地图界面
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 637 141 228 406')
        util.adb('shell input swipe 228 406 228 141')
        x , y = const.picLoop(path + 'port_inside4.jpg')
        util.click(x, y)
        x , y = const.picLoop(path + 'into_port.jpg')
        time.sleep(4)
        util.click(x, y)
        acceptTaskProcess()
    else:
        x , y = const.picLoop(path + 'back_home.jpg')
        util.click(x,y)
    util.logOut(__file__,'------------右上角圣彼得港口领取任务结束-----------')

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

    # 领取任务
    util.logOut(__file__,'------------领取任务开始-----------')
    # 左下NY
    flag = getMission1Process()
    if not flag:
        x , y = const.picLoop(path + 'back_home.jpg')
        util.click(x, y)
        getMission2Process()
        getMission3Process()
        getMission4Process()
        getMission1Process()
    else:
        # 右下角直布罗陀
        getMission2Process()
        
        # 右上角利物浦
        getMission3Process()

        # 右上角圣彼得
        getMission4Process()
    util.logOut(__file__,'------------领取任务结束-----------')

    # 兑换任务
    util.logOut(__file__,'------------兑换任务开始-----------')
    x , y = const.picLoop(path + 'details.jpg')
    util.click(x, y)
    const.picLoop(path + 'is_details.jpg')
    while util.isFindPic(path + 'get_task.jpg'):
        x , y = const.picLoop(path + 'get_task.jpg')
        util.click(x, y)
        x , y = const.picLoop(const.publicPath() + 'bmp/OK.jpg')
        util.click(x, y)
        x , y = const.picLoop(const.publicPath() + 'bmp/get_items.bmp')
        util.click(x, y)
        const.picLoop(path + 'is_details.jpg')
    util.logOut(__file__,'------------兑换任务结束-----------')

    # 出击任务
    util.logOut(__file__,'------------出击任务开始-----------')
    size = (0, 0, 0, 0)
    while util.isFindPic(path + 'look.jpg', size=size):
        x , y = const.picLoop(path + 'look.jpg')
        util.click(x, y)
        time.sleep(2)
        util.logOut(__file__,'------------判断是否为每日任务开始-----------')
        if util.isFindPic(path + 'is_map.jpg'):
            util.logOut(__file__,'------------不是每日任务-----------')
            util.click(433, 462)
            const.picLoop(const.publicPath() + 'beacon/overview.jpg')
            x , y = const.picLoop(path + 'details.jpg')
            util.click(x, y)
            const.picLoop(path + 'is_details.jpg')
            size = (0, y + 10, 864, 486)
        else:
            missionProcess()
            const.picLoop(const.publicPath() + 'beacon/overview.jpg')
            x , y = const.picLoop(path + 'details.jpg')
            util.click(x, y)
            const.picLoop(path + 'is_details.jpg')
    util.click(755, 90) # 任务界面关闭按钮
    const.picLoop(const.publicPath() + 'beacon/overview.jpg')
    util.logOut(__file__,'------------出击任务结束-----------')
    
    # 返回主页
    const.backMainProcess()
