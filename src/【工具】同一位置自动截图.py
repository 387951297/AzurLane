from util import *
from const import const

SEARCH_SIZE = (184, 136, 964, 539)
path = const.publicPath() + 'activity/'
# path = const.publicPath() + 'normal7-2/'
MUST_FIND_AREAS = [
    [421, 279,497, 309],
    ]
for area in MUST_FIND_AREAS:
    area[0] -= 184
    area[1] -= 136
    area[2] -= 184
    area[3] -= 136


# 获取识图找到的点数组

tarImg = util.grab(SEARCH_SIZE)


def getFindPoints():
    points = []
    templates = []
    if templates == []:
        # for i in range(getQuestionNum(path)):
        for i in range(const.getPicNum(path)):
            template = cv2.imread(path + str(i)+'.jpg', 0)
            # template = cv2.imread(path + 'question' + str(i) + '.jpg', 0)
            templates.append(template)
    img = util.grab(SEARCH_SIZE)
    # cv2.rectangle(img, (0, 0), (61, 116), (255, 0, 0), -1)
    cv2.rectangle(img, (0, 0), (263, 65), (255, 0, 0), -1)
    global tarImg
    tarImg = img.copy()

    def foo(i):
        temp = util.findPic(None, threshold=0.7, img=img,
                            template=templates[i])
        if temp != (-1, -1):
            points.append(temp)
    for i in range(const.getPicNum(path)):
    # for i in range(getQuestionNum(path)):
        foo(i)
    return points


def isFindArea(points, areas):
    tempAreas = []
    for area in areas:
        flag = False
        for point in points:
            if point[0] >= area[0] and point[0] <= area[2] and point[1] >= area[1] and point[1] <= area[3]:
                flag = True
                break
        if not flag:
            tempAreas.append(area)
    return (len(tempAreas) == 0, tempAreas)


def showTarImg(points, areas):
    tempImg = tarImg.copy()
    for point in points:
        a = (int(point[0]), int(point[1]))
        b = (int(point[0]), int(point[1]))
        cv2.rectangle(tempImg, a, b, (0, 0, 255), 10)
    for area in areas:
        a = (int(area[0]), int(area[1]))
        b = (int(area[2]), int(area[3]))
        cv2.rectangle(tempImg, a, b, (0, 0, 255), 10)
    cv2.imshow('', tempImg)
    cv2.waitKey(0)


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

def saveImg(area):
    x0 = area[0]
    y0 = area[1]
    x1 = area[2]
    y1 = area[3]
    cropped = tarImg[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
    # 通常
    picNum = str(const.getPicNum(path))
    cv2.imwrite(path + picNum + ".jpg", cropped)
    # 问号
    # picNum = str(getQuestionNum(path))
    # cv2.imwrite(path + 'question' + picNum + '.jpg', cropped)
    print('imwrite：'+picNum)
    cv2.waitKey(0)


def main():
    index = 0
    while index < 100:
        index += 1
        print(index)

        findPoints = getFindPoints()
        flag, unfindArea = isFindArea(findPoints, MUST_FIND_AREAS)
        # showTarImg(findPoints, MUST_FIND_AREAS)
        if not flag:
            for area in unfindArea:
                saveImg(area)


if __name__ == '__main__':
    main()
