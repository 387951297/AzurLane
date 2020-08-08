from util import *
from const import const

path = const.publicPath() + 'activity/'


def main():
    PIC_NUM = const.getPicNum(path)
    templates = []
    SEARCH_SIZE = (184, 136, 964, 539)
    for i in range(PIC_NUM):
        template = cv2.imread(path + str(i)+'.jpg', 0)
        templates.append(template)
    img = util.grab(SEARCH_SIZE)
    cv2.rectangle(img, (0, 0), (61, 116), (255, 0, 0), -1)
    cv2.rectangle(img, (0, 0), (213, 65), (255, 0, 0), -1)
    tarImg = img.copy()

    def foo(i):
        temp = util.findPic(None, threshold=0.9, img=img,template=templates[i])
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
    main()