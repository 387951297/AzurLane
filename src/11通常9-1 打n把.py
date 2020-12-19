from util import *
from const import const

CHAPTER_NUM = 9  # 几-几
CHAPTER_NUM2 = 1  # 几-几
CHAPTER_X, CHAPTER_Y = 220, 189  # 几-几的坐标
START_X, START_Y = 422, 206  # 进stage后初始位置
CNT = 1  # 几次次出boss
path = const.publicPath() + 'normal9-1/'


# if __name__ == '__main__':
def main():
    time.sleep(2)
    print('通常9-1 打n把 开始')
    const.chapterProcess(CHAPTER_NUM, 'N')
    while True:
        # 进入
        print('9-1开始')
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y, 3, 6)
        # 走格子
        X, Y = START_X, START_Y
        # 打CNT个出boss
        for n in range(CNT):
            util.findPicLoop(const.publicPath() + 'bmp/withdraw.jpg')
            # 等待搜索雷达
            time.sleep(4.000)
            X, Y = const.findShip(X, Y, const.getPicNum(path), path)
            util.click(X, Y)
            const.anchorProcess()
        # boss 不打boss
        x , y = util.findPicLoop(const.publicPath() + 'bmp/withdraw.jpg')
        util.click(x,y)
        x , y = util.findPicLoop(const.publicPath() + 'bmp/OK.jpg')
        util.click(x,y)
        print('-------------------------')
