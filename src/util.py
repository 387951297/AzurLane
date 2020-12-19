import base64
import sys
import threading
import time
from datetime import datetime
import os

import numpy as np
import pyautogui
import requests
from cv2 import cv2
from PIL import ImageGrab
import subprocess

class Util:
    __Token = ''

    __TMP_IMAGE = './tmp/image.png'

    def __initToken(self):
        pyautogui.FAILSAFE = False
        # 你的 APPID AK SK
        #APP_ID = '18540285'
        API_KEY = '4jBHa2k1I6BaqXObDXon8PM8'
        SECRET_KEY = '52OBvqTOSaSLYLPRI278Rabv5823zsjI'
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
            API_KEY+'&client_secret='+SECRET_KEY
        response = requests.get(host)
        if response:
            self.__Token = response.json()['access_token']

    def __init__(self):
        self.__initToken()

    # 今天星期几
    def dayOfWeek(self):
        return datetime.now().isoweekday()

    # 执行adb指令
    def adb(self,command):
        AdbPath = '.\\bin\\adb_server.exe '
        ret = subprocess.run(
            AdbPath + command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding="utf-8")
        if ret.returncode == 0:
            if ret.stdout != '':
                print(ret.stdout)
            return ret.stdout
        else:
            print('======adb subprocess error======')
            print(ret)

    # 截图识字
    def getNumbers(self, size):
        request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/numbers'
        img = self.grab(size)
        cv2.imwrite(self.__TMP_IMAGE, img)
        # 二进制方式打开图片文件
        f = open(self.__TMP_IMAGE, 'rb')
        img = base64.b64encode(f.read())

        params = {'image': img}
        access_token = self.__Token
        request_url = request_url + '?access_token=' + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            request_url, data=params, headers=headers).json()
        list = []
        if 'error_code' in response:
            print(response)
            return list
        for i in range(response['words_result_num']):
            list.append(response['words_result'][i]['words'])
        return list

    # 限定范围内百度api识字 输出list
    def getWords(self, size):
        pass
        request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
        img = self.grab(size)
        cv2.imwrite(self.__TMP_IMAGE, img)
        # 二进制方式打开图片文件
        f = open(self.__TMP_IMAGE, 'rb')
        img = base64.b64encode(f.read())

        params = {'image': img}
        access_token = self.__Token
        request_url = request_url + '?access_token=' + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            request_url, data=params, headers=headers).json()
        list = []
        if 'error_code' in response:
            print(response)
            return list
        for i in range(response['words_result_num']):
            list.append(response['words_result'][i]['words'])
        return list

    # 截图返回cv2格式的图片
    def grab(self, size=(0, 0, 0, 0)):
        self.adb('shell screencap /storage/emulated/0/data/screen/image.png')
        self.adb('pull /storage/emulated/0/data/screen/image.png .\\tmp')
        self.adb('shell rm -rf /storage/emulated/0/data/screen/image.png')
        if size != (0, 0, 0, 0):
            return cv2.imread(self.__TMP_IMAGE, 0)[size[1]: size[3], size[0]: size[2]]
        else:
            return cv2.imread(self.__TMP_IMAGE, 0)

    # url图片与屏幕截图匹配,return中心点x,y
    def findPic(self, url, threshold=0.9, size=(0, 0, 0, 0), img=None, template=None):
        if np.all(img == None):
            img = self.grab(size) if size != (0, 0, 0, 0) else self.grab()
        if np.all(template == None):
            template = cv2.imread(url, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        cv2.waitKey(0)
        if max_val >= threshold:
            return (max_loc[0] + w // 2, max_loc[1] + h // 2)
        else:
            return (-1, -1)
        '''
		loc = np.where(res >= threshold)
		cv2.waitKey(0)
		for pt in zip(*loc[::-1]):
			return (pt[0] + w // 2, pt[1] + h // 2)
		return (-1,-1)
		'''

    # 识图返回列表
    def findPicList(self, url, threshold=0.8, size=(0, 0, 0, 0), img=None, template=None):
        if np.all(img == None):
            img = self.grab(size) if size != (0, 0, 0, 0) else self.grab()
        if np.all(template == None):
            template = cv2.imread(url, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        cv2.waitKey(0)
        list = []
        for pt in zip(*loc[::-1]):
            list.append((pt[0] + w // 2, pt[1] + h // 2))
        return list

    # 循环找图 直到找到退出
    def findPicLoop(self, url, threshold=0.8, size=(0, 0, 0, 0)):
        while True:
            x, y = self.findPic(url, threshold, size)
            if x != -1 and y != -1:
                return (x, y)
            time.sleep(.100)

    # 判断是否找到图
    def isFindPic(self, url, threshold=0.8, size=(0, 0, 0, 0)):
        x, y = self.findPic(url, threshold, size)
        if x == -1 and y == -1:
            return False
        else:
            return True

    # 退出脚本
    def exitScript(self):
        print('脚本结束')
        sys.exit()

    # 点击
    def click(self, x, y):
        self.adb('shell input tap ' + str(x) + ' ' + str(y))


util = Util()
