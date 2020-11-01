from util import *
from const import const

CHAPTER_X, CHAPTER_Y = 599, 367  # 几-几的坐标
START_X, START_Y = 659, 559  # 进stage后初始位置
CNT = 6  # 几次出boss
path = const.publicPath() + 'activity/'

def chapterProcess():
    #判断是否在出击章节界面
    #出击界面
    if not util.isFindPic(const.publicPath() + 'activity/into.jpg'):
        #返回主页面
        const.backMainProcess()
        time.sleep(2.000)
    x,y = util.findPicLoop(const.publicPath() + 'activity/into.jpg')
    pyautogui.click(x,y)
    time.sleep(.500)

#走boss格子
def goBossProcess():
    time.sleep(1.000)
    pyautogui.click(537, 329)
    const.anchorProcess()
    print('boss解决')

#滚轮调整显示
def scrollProcess():
    pyautogui.scroll(200)
    time.sleep(.100)
    pyautogui.scroll(200)
    time.sleep(.100)
    pyautogui.scroll(200)

# if __name__ == '__main__':
def main():
    PIC_NUM = const.getPicNum(path)
    time.sleep(2)
    print('activity脚本开始')
    chapterProcess()
    while True:
        # 进入
        time.sleep(2)
        print('SP5开始')
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y)
        # 走格子
        X, Y = START_X, START_Y
        # 打CNT个出boss
        for n in range(CNT):
            # 等待搜索雷达
            time.sleep(5.000)
            if n == 0:
                scrollProcess()
            util.findPicLoop(const.publicPath() + 'bmp/withdraw.jpg')
            X, Y = const.findShip(X, Y, PIC_NUM, path)
            pyautogui.click(X, Y)
            const.anchorProcess()
        # boss
        util.findPicLoop(const.publicPath() + 'bmp/withdraw.jpg')
        # 等待搜索雷达
        time.sleep(4.000)
        goBossProcess()
        print('-------------------------')
