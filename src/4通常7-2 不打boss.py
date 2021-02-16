from util import *
from const import const

CHAPTER_NUM = 7  # 几-几
CHAPTER_NUM2 = 2  # 几-几
CHAPTER_X, CHAPTER_Y = 361, 146  # 几-几的坐标
START_X, START_Y = 147, 376  # 进stage后初始位置
CNT = 4  # 几次次出boss
path = const.publicPath() + 'normal7-2/'
Q_NUM = 3  # 问号多少张图


# if __name__ == '__main__':
def main():
    time.sleep(2)
    util.logOut(__file__,'通常7-2 不打boss 开始')
    const.chapterProcess(7, 'N')
    while True:
        # 进入7-2
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
            # 先看有没有问号
            if n != 0:
                for i in range(Q_NUM):
                    x , y = findQuestion(X, Y, getQuestionPicNum(path), path,ignore=[300, 209,137, 88])
                    if x != -1 and y != -1:
                        util.logOut(__file__,'处理问号 开始')
                        X, Y = x , y + 33
                        util.click(X, Y)
                        for j in range(10):
                            xx, yy = util.findPic(
                                const.publicPath() + 'bmp/get_items.bmp')
                            if xx != -1 and yy != -1:
                                break
                        util.click(354, 462)
                        time.sleep(1)
                        util.logOut(__file__,'处理问号 结束')
                    else:
                        break
            X, Y = const.findShip(X, Y, const.getPicNum(path), path,ignore=[300, 209,137, 88])
            util.click(X, Y)
            const.anchorProcess(redFace=True)
            util.logOut(__file__,'------------一把结束-----------')
        # boss 不打boss
        x , y = const.picLoop(const.publicPath() + 'bmp/withdraw.jpg')
        util.click(x,y)
        x , y = const.picLoop(const.publicPath() + 'bmp/OK.jpg')
        util.click(x,y)
        util.logOut(__file__,'-------------一局结束------------')

__templates = []
def findQuestion(x,y,num,path,ignore=[0,0,0,0]):
    util.logOut(__file__,'findQuestion 找问号 开始')
    SEARCH_SIZE = (84, 36,864, 439)
    if __templates == []:
        for i in range(num):
            template = cv2.imread(path + 'question' + str(i) + '.jpg',0)
            __templates.append(template)
    img = util.grab(SEARCH_SIZE)
    cv2.rectangle(img,(0,0),(263, 65),(0,0,0),-1)
    # 改过了长度
    if ignore != [0,0,0,0]:
        cv2.rectangle(
            img,
            (ignore[0]-SEARCH_SIZE[0],ignore[1]-SEARCH_SIZE[1]),(ignore[2]-SEARCH_SIZE[0], ignore[3]-SEARCH_SIZE[1]),
            (0,0,0),
            -1
        )

    list = [None for i in range(num)]
    def foo(i):
        temp = util.findPic(None,threshold = 0.9, img = img,template = __templates[i])
        tempList = []
        for value in temp:
            tempList.append(value)
        if tempList != [-1,-1]:
            tempList[0] += SEARCH_SIZE[0]
            tempList[1] += SEARCH_SIZE[1]
        list[i] = tempList
    for i in range(num):
        foo(i)

    minDistance = sys.maxsize
    minIndex = 0
    index = -1
    for value in list:
        index += 1
        if value == [-1,-1]:
            continue
        temp = (value[0] - x)**2 + (value[1] - y)**2
        if temp < minDistance:
            minDistance = temp
            minIndex = index
    util.logOut(__file__,'findQuestion 找问号 结束')
    return list[minIndex][0],list[minIndex][1]

def getQuestionPicNum(path):
    num = 0
    for fileName in os.listdir(path):
        try:
            int(fileName[8:9])
            num += 1
        except ValueError:
            pass
    return num