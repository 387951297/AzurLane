from util import *
from const import const

from aip import AipImageSearch
def main():
    """ 你的 APPID AK SK """
    APP_ID = '23182724'
    API_KEY = 'yqovkvjCAzRmvDhrFn6hid9A'
    SECRET_KEY = 'i21lCfxppo3Mk1kKFrnCra4QR62Tbf5H'

    client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content('./public/bmp/QQ截图20201002134754.jpg')
    ret = client.sameHqSearch(image)
    print(ret)




if __name__ == '__main__':
    main()
