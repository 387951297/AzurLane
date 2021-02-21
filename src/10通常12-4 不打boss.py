from util import *
from const import const

CHAPTER_NUM, CHAPTER_NUM2 = 12, 4  # 几-几
CHAPTER_X, CHAPTER_Y = 691, 368  # 几-几的坐标
START_X, START_Y = 413, 410  # 进stage后初始位置
CNT = 2  # 道中打几次
path = const.publicPath() + 'normal' + str(CHAPTER_NUM) + '-' + str(CHAPTER_NUM2) + '/'

def main():
    time.sleep(2)
    util.logOut(__file__,'通常' + str(CHAPTER_NUM) + '-' + str(CHAPTER_NUM2) + ' 不打boss 开始')
    const.chapterProcess(CHAPTER_NUM, 'N')
    while True:
        # 进入12-4
        util.logOut(__file__,'-------------一局开始------------')
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y, 3, 6, True)
        # 走格子
        X, Y = START_X, START_Y
        # 打CNT个出boss
        for n in range(CNT):
            util.logOut(__file__,'------------一把开始-----------')
            const.picLoop(const.publicPath() + 'bmp/withdraw.jpg')
            # 等待搜索雷达
            time.sleep(4.000)
            X, Y = const.findShip(X, Y, const.getPicNum(path), path)
            util.click(X, Y)
            const.anchorProcess(redFace=True)
            util.logOut(__file__,'------------一把结束-----------')
        # boss 不打boss
        x , y = const.picLoop(const.publicPath() + 'bmp/withdraw.jpg')
        util.click(x,y)
        x , y = const.picLoop(const.publicPath() + 'bmp/OK.jpg')
        util.click(x,y)
        util.logOut(__file__,'-------------一局结束------------')
