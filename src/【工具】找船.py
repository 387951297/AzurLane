from util import *
from const import const

# 通常
path = const.publicPath() + 'activity/'
# 问号
# path = const.publicPath() + 'normal7-2/'


def main():
    # 通常
    PIC_NUM = const.getPicNum(path)
    # 问号
    # PIC_NUM = 2
    templates = []
    SEARCH_SIZE = (184, 136, 964, 539)
    # SEARCH_SIZE = (829, 254, 933, 375)
    for i in range(PIC_NUM):
        # 通常
        template = cv2.imread(path + str(i)+'.jpg', 0)
        # 问号
        # template = cv2.imread(path + 'question' + str(i) + '.jpg', 0)
        templates.append(template)
    img = util.grab(SEARCH_SIZE)
    cv2.rectangle(img,(0,0),(213, 65),(255,0,0),-1)
    tarImg = img.copy()

    def foo(i):
        temp = util.findPic(None, threshold=0.7, img=img,template=templates[i])
        if temp[0] == -1 and temp[1] == -1:
            return
        print(i, temp)
        a = (int(temp[0]-20), int(temp[1]-20))
        b = (int(temp[0]+20), int(temp[1]+20))
        cv2.rectangle(tarImg, a, b, (0, 0, 255), 2)
        
    for i in range(PIC_NUM):
        foo(i)

    time.sleep(2)
    cv2.imshow('', tarImg)
    cv2.waitKey(0)

if __name__ == '__main__':
    while True:
        main()