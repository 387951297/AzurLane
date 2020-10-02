from util import *
from const import const

CHAPTER_NUM = 7  # 几-几
CHAPTER_NUM2 = 2  # 几-几
CHAPTER_X, CHAPTER_Y = 461, 246  # 几-几的坐标
START_X, START_Y = 247, 476  # 进stage后初始位置
CNT = 5  # 几次次出boss
path = const.publicPath() + 'normal7-2/'
LIST_QUESTION = [(829, 254, 933, 375),
                 (489, 209, 589, 310),
                 (484, 322, 584, 442)]
Q_NUM = 3  # 问号多少张图


# if __name__ == '__main__':
def main():
    time.sleep(2)
    print('7-2脚本开始')
    const.chapterProcess(7, 'N')
    while True:
        # 进入7-2
        print('7-2开始')
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y)
        # 走格子
        X, Y = START_X, START_Y
        # 打CNT个出boss
        for n in range(CNT):
            util.findPicLoop(const.publicPath() + 'bmp/withdraw.jpg')
            # 等待搜索雷达
            time.sleep(4.000)
            # 先看有没有问号
            for size in LIST_QUESTION:
                for i in range(Q_NUM):
                    x, y = util.findPic(
                        path + 'question' + str(i) + '.jpg', size=size)
                    if x != -1 and y != -1:
                        X, Y = x + size[0], y + size[1]
                        pyautogui.click(X, Y)
                        for j in range(50):
                            xx, yy = util.findPic(
                                const.publicPath() + 'bmp/get_items.bmp')
                            if xx != -1 and yy != -1:
                                break
                            time.sleep(.100)
                        pyautogui.click(454, 562)
                        time.sleep(1)
                        break

            X, Y = const.findShip(X, Y, const.getPicNum(path), path)
            pyautogui.click(X, Y)
            const.anchorProcess()
        # boss
        const.goBossProcess()
        print('-------------------------')
