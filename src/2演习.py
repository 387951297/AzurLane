from util import *
from const import const

# 我的实力
myAttack = 10000
# 演习四个框框的位置
EXERCISE_SIZES = ((157, 170, 202, 217),
                  (322, 173, 364, 212),
                  (487, 175, 530, 212),
                  (654, 173, 697, 212))

# 演习中的四个里面找到最小值
def FindOKExercise():
    min = 999999
    minIndex = -1
    index = -1
    for sizeValue in EXERCISE_SIZES:
        index += 1
        list = []
        while len(list) == 0:
            list = util.getNumbers(sizeValue)
        sum = 0
        avg = 999999
        for value in list:
            sum += int(value)
        avg = sum // 2
        if(avg < min):
            min = avg
            minIndex = index
    return (min, minIndex)


# if __name__ == '__main__':
def main():
    time.sleep(2)
    print('演习脚本开始')
    # 判断是否在演习界面
    if not util.isFindPic(const.publicPath() + 'bmp/is_exercise.jpg'):
        # 返回主页面
        const.backMainProcess()
        # 进入演习界面
        x, y = util.findPicLoop(const.publicPath() + 'bmp/weigh anchor.jpg')
        util.click(x, y)
        time.sleep(.500)
        x, y = util.findPicLoop(const.publicPath() + 'bmp/exercise.jpg')
        util.click(x, y)
        time.sleep(.500)
    while True:
        # 0/10退出
        time.sleep(1)
        list = util.getNumbers((778, 91, 818, 113))
        if list != [] and list[0][0] == '0':
            const.backMainProcess()
            return

        # 识字 选择弱的
        min, minIndex = FindOKExercise()
        while min > myAttack:
            x, y = util.findPicLoop(
                const.publicPath() + 'bmp/new opponent.jpg')
            util.click(x, y)
            time.sleep(6.000)
            min, minIndex = FindOKExercise()

        util.click(EXERCISE_SIZES[minIndex]
                        [0], EXERCISE_SIZES[minIndex][1])
        time.sleep(.500)

        # 开始演习
        x, y = util.findPicLoop(const.publicPath() + 'bmp/start excise.jpg')
        util.click(x, y)
        time.sleep(.500)
        const.anchorProcess()
