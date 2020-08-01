from util import *
from const import const

path = const.publicPath() + 'normal7-2/'
PIC_NUM = 13  # 多少张图

# if __name__ == '__main__':
def main():
    templates = []
    SEARCH_SIZE = (184, 136, 964, 539)
    if templates == []:
        for i in range(PIC_NUM):
            template = cv2.imread(path + str(i)+'.jpg', 0)
            templates.append(template)
    img = util.grab(SEARCH_SIZE)
    cv2.rectangle(img, (0, 0), (61, 116), (255, 0, 0), -1)
    cv2.rectangle(img, (0, 0), (213, 65), (255, 0, 0), -1)
    tarImg = img.copy()

    def foo(i):
        temp = util.findPic(None, threshold=0.9, img=img,
                            template=templates[i])
        a = (int(temp[0]-50), int(temp[1]-50))
        b = (int(temp[0]+50), int(temp[1]+50))
        cv2.rectangle(tarImg, a, b, (0, 0, 255), 10)
        print(i, temp)

    for i in range(PIC_NUM):
        foo(i)

    time.sleep(2)
    cv2.imshow('', tarImg)
    cv2.waitKey(0)
