from util import *
from const import const

path = const.publicPath() + 'operation/'

def main():
    time.sleep(2)
    util.logOut(__file__,'3次飞龙 开始')

    #返回主页面
    const.backMainProcess()
    #进入出击界面
    x , y = const.picLoop(const.publicPath() + 'bmp/weigh anchor.jpg')
    util.click(x,y)
    x , y = const.picLoop(const.publicPath() + 'beacon/operation.jpg')
    util.click(x,y)

    while True:
        # 去西北航道F图
        util.logOut(__file__,'------------一把开始-----------')
        x , y = const.picLoop(const.publicPath() + 'beacon/overview.jpg')
        time.sleep(2)
        util.click(x,y)
        x , y = const.picLoop(path + 'area_overview.jpg')
        util.click(x,y)
        time.sleep(2)
        util.click(340,160) # 左上角区域
        time.sleep(2)
        util.click(70,200) # 西北航道F
        x , y = const.picLoop(path + 'enter.jpg')
        util.click(x,y)

        # 自律
        time.sleep(4)
        def other():
            util.logOut(__file__,'判断skip')
            x , y = util.findPic(path + 'skip.jpg')
            if x != -1 and y != -1:
                util.logOut(__file__,'skip')
                util.click(x,y)
                time.sleep(2)
                return
            util.logOut(__file__,'判断落地踩到猫')
            x , y = util.findPic(path + 'TB.jpg')
            if x != -1 and y != -1:
                util.logOut(__file__,'落地踩到猫')
                util.click(647, 197) # 派遣（指挥猫将暂时离队）
                time.sleep(2)
                return
            util.logOut(__file__,'判断落地踩到箱子')
            x , y = util.findPic(const.publicPath() + 'get_items.bmp')
            if x != -1 and y != -1:
                util.logOut(__file__,'落地踩到箱子')
                util.click(x, y)
                time.sleep(2)
                return
     
        other()
        x , y = const.picLoop(path + 'zilv.jpg')
        time.sleep(2)
        util.click(x,y)
        time.sleep(60)
        x , y = const.picLoop(path + 'leave.jpg')
        util.click(x,y)
        util.logOut(__file__,'------------一把结束-----------')

        # 去利物浦
        util.logOut(__file__,'------------去趟利物浦开始-----------')
        x , y = const.picLoop(const.publicPath() + 'beacon/overview.jpg')
        time.sleep(2)
        util.click(x,y)
        x , y = const.picLoop(path + 'area_overview.jpg')
        util.click(x,y)
        time.sleep(2)
        util.click(500,150) # 右上角区域
        time.sleep(2)
        x , y = const.picLoop(path + 'port.jpg')
        util.click(x,y)
        x , y = const.picLoop(path + 'enter_port.jpg')
        util.click(x,y)
        util.logOut(__file__,'------------去趟利物浦结束-----------')
