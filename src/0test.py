from util import *
from const import const

def main():
    list = util.getWords((337, 301 , 727, 363))
    if len(list) != 0:
        str = list[0][0:1]
        if str == '低':
            x , y = util.findPicLoop(const.publicPath() + 'bmp/OK.jpg')
            pyautogui.click(x,y)


if __name__ == '__main__':
    main()
