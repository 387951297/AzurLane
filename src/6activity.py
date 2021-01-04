from util import *
from const import const

CHAPTER_X, CHAPTER_Y = 650, 204  # 几-几的坐标
START_X, START_Y = 392, 401  # 进stage后初始位置
CNT = 6  # 几次出boss
path = const.publicPath() + 'activity/'

def chapterProcess():
    #判断是否在出击章节界面
    #出击界面
    if not util.isFindPic(const.publicPath() + 'activity/into.jpg'):
        #返回主页面
        const.backMainProcess()
        time.sleep(2.000)
    x,y = const.picLoop(const.publicPath() + 'activity/into.jpg')
    util.click(x,y)
    time.sleep(.500)

#走boss格子
def goBossProcess():
    time.sleep(1.000)
    util.click(437, 229)
    const.anchorProcess()
    util.logOut(__file__,'boss解决')

#滚轮调整显示
def scrollProcess():
    pass
    # pyautogui.scroll(200)
    # time.sleep(.100)
    # pyautogui.scroll(200)
    # time.sleep(.100)
    # pyautogui.scroll(200)

# if __name__ == '__main__':
def main():
    PIC_NUM = const.getPicNum(path)
    time.sleep(2)
    util.logOut(__file__,'activity脚本开始')
    chapterProcess()
    while True:
        # 进入
        time.sleep(2)
        util.logOut(__file__,'SP3开始')
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y)
        # 走格子
        X, Y = START_X, START_Y
        # 打CNT个出boss
        for n in range(CNT):
            # 等待搜索雷达
            time.sleep(5.000)
            if n == 0:
                scrollProcess()
            const.picLoop(const.publicPath() + 'bmp/withdraw.jpg')
            X, Y = const.findShip(X, Y, PIC_NUM, path)
            util.click(X, Y)
            const.anchorProcess()
        # boss
        const.picLoop(const.publicPath() + 'bmp/withdraw.jpg')
        # 等待搜索雷达
        time.sleep(4.000)
        goBossProcess()
        util.logOut(__file__,'-------------------------')
