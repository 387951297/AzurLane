from util import *
from const import const

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
    num = getQuestionNum(const.publicPath() + 'normal7-2/')
    print(num)


if __name__ == '__main__':
    main()
