from util import *
from const import const

CHAPTER_NUM = 11  # 几-几
CHAPTER_NUM2 = 1  # 几-几
CHAPTER_X, CHAPTER_Y = 269,182  # 几-几的坐标

# if __name__ == '__main__':
def main():
    time.sleep(2)
    util.logOut(__file__,'困难'+str(CHAPTER_NUM)+'-'+str(CHAPTER_NUM2)+'脚本开始')

    # 进入困难第CHAPTER_NUM章界面
    const.chapterProcess(CHAPTER_NUM, 'H')

    # 判断每日几次
    cnt = 3 # 默认三次
    list = util.getNumbers((60, 407, 93, 429))
    if list != []:
        cnt = int(list[0][0])
        
    # 每日困难cnt次
    for i in range(cnt):
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y)
        time.sleep(3)

        # 阵容锁定判断
        x, y = util.findPic(const.publicPath() + 'bmp/lock.jpg', 0.95)
        if x != -1 and y != -1:
            util.logOut(__file__,'阵容锁定解锁')
            util.click(x, y)

        const.goBossProcess()
    const.backMainProcess()
    return
