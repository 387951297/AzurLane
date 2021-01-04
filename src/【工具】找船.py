from util import *
from const import const

# 通常
path = const.publicPath() + 'activity/'
# 问号
# path = const.publicPath() + 'normal7-2/'

# 获取path内有多少question图需要搜索
def getQuestionNum(path):
    num = 0
    for fileName in os.listdir(path):
        try:
            int(fileName[8:9])
            num += 1
        except ValueError:
            pass
    return num

def main():
    # 初始化
    print('adb初始化开始')
    util.adb('kill-server')
    util.adb('connect 127.0.0.1:7555')
    # 通常
    PIC_NUM = const.getPicNum(path)
    # 问号
    # PIC_NUM = getQuestionNum(path)
    templates = []
    SEARCH_SIZE = (84, 36,864, 439)
    for i in range(PIC_NUM):
        # 通常
        template = cv2.imread(path + str(i)+'.jpg', 0)
        # 问号
        # template = cv2.imread(path + 'question' + str(i) + '.jpg', 0)
        templates.append(template)
    img = util.grab(SEARCH_SIZE)
    # 通常
    cv2.rectangle(img,(0,0),(263, 65),(255,0,0),-1)
    # 问号
    # cv2.rectangle(img,(0,0),(263, 65),(0,0,0),-1)
    # cv2.rectangle(img,(400-184, 309-136),(237-184, 188-136),(0,0,0),-1)
    tarImg = img.copy()

    def foo(i):
        # 通常
        temp = util.findPic(None, threshold=0.7, img=img,template=templates[i])
        # 问号
        # temp = util.findPic(None, threshold=0.9, img=img,template=templates[i])
        if temp[0] == -1 and temp[1] == -1:
            return
        print(i, temp)
        # 通常
        a = (int(temp[0]-20), int(temp[1]-20))
        b = (int(temp[0]+20), int(temp[1]+20))
        # 问号
        # a = (int(temp[0]-20), int(temp[1]-20) +35)
        # b = (int(temp[0]+20), int(temp[1]+20) +35)
        cv2.rectangle(tarImg, a, b, (0, 0, 255), 2)
        
    for i in range(PIC_NUM):
        foo(i)

    time.sleep(2)
    cv2.imshow('', tarImg)
    cv2.waitKey(0)

if __name__ == '__main__':
    while True:
        main()
        