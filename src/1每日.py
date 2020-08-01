from util import *
from const import const

# 五个名称框框
NAME_SIZES = ((155, 388, 232, 423),
              (285, 395, 380, 434),
              (453, 405, 567, 449),
              (647, 395, 742, 435),
              (804, 392, 884, 421))

# 出击数框框
NUM_SIZES = ((146, 224, 180, 256),
             (285, 201, 314, 226),
             (454, 169, 492, 200),
             (647, 203, 683, 228),
             (806, 231, 831, 253))

# 星期与索引表
INDEXS_BY_WEEK = ((0, 2),
                  (1, 2),
                  (2, 3),
                  (0, 2),
                  (1, 2),
                  (2, 3),
                  (0, 1, 2, 3))

# 是否不是0/3


def isOKByIndex(index):
    # 判断数
    tempList = util.getNumbers(NUM_SIZES[index])
    if tempList == []:
        return False
    # 我只要头一个数
    return int(tempList[0][0]) != 0

# 退出每日界面来重置每日副本的位置


def resetProcess():
    x, y = util.findPicLoop(const.publicPath + "back.jpg")
    time.sleep(.800)
    pyautogui.click(x, y)
    # 进入每日界面
    x, y = util.findPicLoop(const.publicPath + "daily task.jpg")
    pyautogui.click(x, y)
    time.sleep(2.000)


if __name__ == "__main__":
    print("记得把道中队换好")
    print("破交自己打不识别")
    time.sleep(2)
    print("每日脚本开始")

    # 判断是否在出击界面
    if not util.isFindPic('./bmp/exercise.jpg'):
        # 返回主页面
        const.backMainProcess()
        # 进入出击界面
        x, y = util.findPicLoop(const.publicPath + "weigh anchor.jpg")
        pyautogui.click(x, y)
        time.sleep(.8)
    # 进入每日界面
    x, y = util.findPicLoop(const.publicPath + "daily task.jpg")
    pyautogui.click(x, y)
    time.sleep(.8)

    firstIntoFlag = True
    indexTup = INDEXS_BY_WEEK[util.dayOfWeek() - 1]
    for index in indexTup:
        if not firstIntoFlag:
            resetProcess()
        if not isOKByIndex(index):
            continue
        # 移动
        if index != 2:
            pyautogui.click(NAME_SIZES[index][0], NAME_SIZES[index][1])
            time.sleep(.800)
        # 进入
        pyautogui.click(NAME_SIZES[2][0], NAME_SIZES[2][1])
        time.sleep(.800)

        # 打3把
        for k in range(3):
            # 最上面那个子选项位置
            pyautogui.click(603, 234)
            time.sleep(.800)
            const.anchorProcess()

        # 返回
        x, y = util.findPicLoop(const.publicPath + "back.jpg")
        time.sleep(.800)
        pyautogui.click(x, y)

        firstIntoFlag = False

    time.sleep(1)
    const.backMainProcess()
