import importlib
import sys
import os
import ctypes
import traceback
import time
import subprocess
sys.path.append(os.getcwd().replace('\\', '/')+'/src')

m = ['' for _ in range(100)]
# 引用带数字的py模组
for fileName in os.listdir('./src'):
    num = ''
    try:
        num = int(fileName[0:2])
        m[num] = importlib.import_module(
            fileName.replace('.py', ''))
        continue
    except ValueError:
        pass
    try:
        num = int(fileName[0])
        m[num] = importlib.import_module(
            fileName.replace('.py', ''))
        continue
    except ValueError:
        pass

# 菜单显示
def mainPrint():
    os.system("cls")
    
    printList = ['' for _ in range(100)]
    for fileName in os.listdir('./src'):
        try:
            num = int(fileName[0:2])
            printList[num] = fileName.replace('.py', '')
            continue
        except ValueError:
            pass
        try:
            num = int(fileName[0])
            printList[num] = fileName.replace('.py', '')
            continue
        except ValueError:
            pass
    for str in printList:
        if str != '':
            print(str)
    print('请输入数字来启动对应的脚本：')
    while True:
        str = input()
        for fileName in os.listdir('./src'):
            if str == fileName[0] or str == fileName[0:2]:
                return str
        print('请重新输入数字来启动对应的脚本：')

# 执行adb指令
def adb(command):
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

if __name__ == '__main__':
    # 初始化
    print('adb初始化开始')
    adb('kill-server')
    adb('connect 127.0.0.1:7555')
    while True:
        try:
            m[int(mainPrint())].main()
        except Exception as err:
            print(err.args)
            print('==========')
            print(traceback.format_exc()) 
            input()
            sys.exit()



        
