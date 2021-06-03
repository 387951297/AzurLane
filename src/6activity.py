from util import *
from const import const

# CHAPTER_X, CHAPTER_Y = 663, 198  # 几-几的坐标 D3
CHAPTER_X, CHAPTER_Y = 407, 399  # 几-几的坐标 C2
redFace = True # 红脸是否继续刷
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

# if __name__ == '__main__':
def main():
    PIC_NUM = const.getPicNum(path)
    time.sleep(2)
    util.logOut(__file__,'activity脚本开始')
    chapterProcess()
    while True:
        # 进入
        time.sleep(2)
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y)
        util.logOut(__file__,'活动图开始-------------------------')
        time.sleep(60.000)

        def noTipAgain():
            util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/again.jpg')
            util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/zhengli.jpg')
            for i in range(600):
                x, y = util.findPic(const.publicPath() + 'bmp/again.jpg', threshold=0.8, size=(0, 0, 0, 0))
                if x != -1 and y != -1:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/again.jpg')
                    util.logOut(__file__,'活动图结束-------------------------')
                    x,y = const.picLoop(const.publicPath() + 'bmp/leave.jpg')
                    util.click(x,y)
                    return
                x, y = util.findPic(const.publicPath() + 'bmp/zhengli.jpg', threshold=0.8, size=(0, 0, 0, 0))
                if x != -1 and y != -1:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/zhengli.jpg')
                    util.logOut(__file__,'船坞已满')
                    time.sleep(2)
                    util.click(x,y)
                    const.retireProcess()
                    time.sleep(4.000)
                    x,y = const.picLoop(const.publicPath() + 'bmp/zilv.jpg')
                    util.click(x,y)
                #红脸特殊（屑）
                if redFace and i % 10 == 0: # 10次判断一次
                    util.logOut(__file__,'红脸判断 开始')
                    list = util.getWords((237, 201 , 627, 263))
                    if len(list) != 0 and '低心情' in list[0]:
                        util.logOut(__file__,'我是粪提 结束')
                        x, y = const.picLoop(const.publicPath() + 'bmp/OK.jpg')
                        util.click(x, y)

            util.logOut(__file__,'picLoop没找到图 需要重启脚本！！！！！！')
            const.restartProcess()
            raise ValueError('restart')

        noTipAgain()

