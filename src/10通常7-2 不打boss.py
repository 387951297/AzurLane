from util import *
from const import const

CHAPTER_NUM = 7  # 几-几
CHAPTER_NUM2 = 2  # 几-几
CHAPTER_X, CHAPTER_Y = 461, 246  # 几-几的坐标
START_X, START_Y = 247, 476  # 进stage后初始位置
CNT = 6  # 几次次出boss
path = const.publicPath() + 'normal7-2/'
Q_NUM = 3  # 问号多少张图


# if __name__ == '__main__':
def main():
    time.sleep(2)
    print('通常7-2 不打boss 开始')
    const.chapterProcess(7, 'N')
    while True:
        # 进入7-2
        print('7-2开始')
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y, 3, 6, True)
        # 走格子
        X, Y = START_X, START_Y
        # 打CNT个出boss
        for n in range(CNT):
            util.findPicLoop(const.publicPath() + 'bmp/withdraw.jpg')
            # 等待搜索雷达
            time.sleep(4.000)
            # 先看有没有问号
            for i in range(Q_NUM):
                x , y = findQuestion(X, Y, getQuestionPicNum(path), path,ignore=[400, 309,237, 188])
                if x != -1 and y != -1:
                    X, Y = x , y 
                    pyautogui.click(X, Y)
                    for j in range(50):
                        xx, yy = util.findPic(
                            const.publicPath() + 'bmp/get_items.bmp')
                        if xx != -1 and yy != -1:
                            break
                        time.sleep(.100)
                    pyautogui.click(454, 562)
                    time.sleep(1)

            X, Y = const.findShip(X, Y, const.getPicNum(path), path,ignore=[400, 309,237, 188])
            pyautogui.click(X, Y)
            const.anchorProcess(redFace=True)
        # boss 不打boss
        x , y = util.findPicLoop(const.publicPath() + 'bmp/withdraw.jpg')
        pyautogui.click(x,y)
        x , y = util.findPicLoop(const.publicPath() + 'bmp/OK.jpg')
        pyautogui.click(x,y)
        print('-------------------------')

__templates = []
def findQuestion(x,y,num,path,ignore=[0,0,0,0]):
    SEARCH_SIZE = (184, 136,964, 539)
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
    return list[minIndex][0],list[minIndex][1] + 35

def getQuestionPicNum(path):
    num = 0
    for fileName in os.listdir(path):
        try:
            int(fileName[8:9])
            num += 1
        except ValueError:
            pass
    return num