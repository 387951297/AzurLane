from util import *
from const import const

CHAPTER_X, CHAPTER_Y = 226, 288  # 几-几的坐标
START_X, START_Y = 780, 281  # 进stage后初始位置
CNT = 5  # 几次出boss
path = const.publicPath() + 'activity/'

def chapterProcess():
    nextX , nextY = 926, 351
    #判断是否在出击章节界面
    #出击界面
    if not util.isFindPic(const.publicPath() + 'activity/into.jpg'):
        #返回主页面
        const.backMainProcess()
        time.sleep(2.000)
    x,y = util.findPicLoop(const.publicPath() + 'activity/into.jpg')
    pyautogui.click(x,y)
    time.sleep(.500)
    #第chapterNum章
    pyautogui.click(nextX,nextY)
    time.sleep(.500)
    #困难模式
    x,y = util.findPic(const.publicPath() + 'bmp/hardmode.jpg')
    if x!=-1 and y!=-1:
        pyautogui.click(x,y)
        time.sleep(.2)

#走boss格子
def goBossProcess():
    time.sleep(1.000)
    pyautogui.click(537, 329)
    const.anchorProcess()
    print('boss解决')

# if __name__ == '__main__':
def main():
    PIC_NUM = const.getPicNum(path)
    time.sleep(2)
    print('activity脚本开始')
    chapterProcess()
    while True:
        # 进入
        print('d1开始')
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y)
        # 走格子
        X, Y = START_X, START_Y
        # 打CNT个出boss
        for n in range(CNT+1):
            # 等待搜索雷达
            time.sleep(4.000)
            if n == 0:
                pyautogui.click(631, 522)
                time.sleep(5)
                if util.isFindPic(const.publicPath() + 'bmp/anchor.bmp'):
                    const.anchorProcess()
            elif n == 1:
                pyautogui.click(809, 403)
                time.sleep(5)
                if util.isFindPic(const.publicPath() + 'bmp/anchor.bmp'):
                    const.anchorProcess()
            elif n == 2:
                pyautogui.click(629, 338)
                time.sleep(5)
                if util.isFindPic(const.publicPath() + 'bmp/anchor.bmp'):
                    const.anchorProcess()
            else:
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
