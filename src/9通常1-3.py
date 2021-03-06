from util import *
from const import const

CHAPTER_NUM = 1  # 几-几
CHAPTER_NUM2 = 3  # 几-几
CHAPTER_X, CHAPTER_Y = 495, 385  # 几-几的坐标
START_X, START_Y = 260, 267  # 进stage后初始位置
CNT = 2  # 几次出boss
path = const.publicPath() + 'normal1-3/'


# if __name__ == '__main__':
def main():
    time.sleep(2)
    util.logOut(__file__,str(CHAPTER_NUM) + '-' + str(CHAPTER_NUM2) + '脚本开始')
    const.chapterProcess(CHAPTER_NUM, 'N')
    while True:
        # 进入
        util.logOut(__file__,str(CHAPTER_NUM) + '-' + str(CHAPTER_NUM2) + '开始')
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y, 3, 2)
        # 走格子
        X, Y = START_X, START_Y
        # 打CNT个出boss
        for n in range(CNT):
            const.picLoop(const.publicPath() + 'bmp/withdraw.jpg')
            # 等待搜索雷达
            if n == 0:
                time.sleep(4.000)
            X, Y = const.findShip(X, Y, const.getPicNum(path), path)
            util.click(X, Y)
            const.anchorProcess()
        # boss
        const.picLoop(const.publicPath() + 'bmp/withdraw.jpg')
        const.goBossProcess()
        util.logOut(__file__,'-------------------------')
