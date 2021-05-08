from util import *

class Const:
    def __init__(self):
        pass
        
    #获取根path
    def path(self):
        return './'

    #图片资源path
    def publicPath(self):
        return self.path() + 'public/'

    #临时path
    def tmpPath(self):
        return self.path() + 'tmp/'

    #返回主页面
    def backMainProcess(self):
        util.logOut(__file__,'backMainProcess 返回主页面开始')
        if util.isFindPic(self.publicPath() + 'bmp/home.jpg',0.8):
            x , y = util.findPic(self.publicPath() + 'bmp/home.jpg',0.8)
            util.click(x,y)
            time.sleep(.500)
        elif util.isFindPic(self.publicPath() + 'bmp/weigh anchor.jpg'):
            util.logOut(__file__,'backMainProcess 返回主页面结束')
            return
        else:
            util.logOut(__file__,'backMainProcess 返回主页面结束 失败')

    #退役蓝白未锁的船
    def retireProcess(self):
        util.logOut(__file__,'retireProcess 退役步骤开始')
        time.sleep(2)
        x,y = self.picLoop(self.publicPath() + 'bmp/retire.jpg')
        util.click(x,y)
        time.sleep(.800)
        x,y = self.picLoop(self.publicPath() + 'bmp/OK.jpg')
        util.click(x,y)
        x,y = self.picLoop(self.publicPath() + 'bmp/get_items.bmp')
        util.click(x,y)
        time.sleep(.800)
        x,y = self.picLoop(self.publicPath() + 'bmp/OK.jpg')
        util.click(x,y)
        time.sleep(.800)
        x,y = self.picLoop(self.publicPath() + 'bmp/OK.jpg')
        util.click(x,y)
        x,y = self.picLoop(self.publicPath() + 'bmp/get_items.bmp')
        util.click(x,y)
        x,y = self.picLoop(self.publicPath() + 'bmp/back.jpg')
        util.click(x,y)
        util.logOut(__file__,'retireProcess 退役步骤结束')

    #出击到结束的过程
    def anchorProcess(self, redFace = False):
        util.logOut(__file__,'anchorProcess 出击步骤开始')
        time.sleep(.800)
        #今日不再提示
        util.logOut(__file__,'今日不再提示判断 开始')

        def noTip():
            util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/anchor.bmp')
            util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/quit.jpg')
            for i in range(600):
                x, y = util.findPic(const.publicPath() + 'bmp/anchor.bmp', threshold=0.8, size=(0, 0, 0, 0))
                if x != -1 and y != -1:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/anchor.bmp')
                    return
                x, y = util.findPic(const.publicPath() + 'bmp/quit.jpg', threshold=0.8, size=(0, 0, 0, 0))
                if x != -1 and y != -1:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/quit.jpg')
                    util.click(x,y)
                    util.logOut(__file__,'今日不再提示')
                    return
            util.logOut(__file__,'picLoop没找到图 需要重启脚本！！！！！！')
            const.restartProcess()
            raise ValueError('restart')
        noTip()

        # x,y = util.findPic(self.publicPath() + 'bmp/anchor.bmp')
        # if x==-1 and y==-1:
        #     x,y = util.findPic(self.publicPath() + 'bmp/quit.jpg')
        #     if x!=-1 and y!=-1:
        #         util.click(x,y)
        #         util.logOut(__file__,'今日不再提示')
   
        def anchor():
            x , y = self.picLoop(self.publicPath() + 'bmp/anchor.bmp')
            time.sleep(0.800)
            util.click(x,y)
            util.logOut(__file__,'自律 开始')
            
        anchor()
        time.sleep(.800)
        #红脸特殊（屑）
        isRedFace = False
        if redFace:
            util.logOut(__file__,'红脸判断 开始')
            list = util.getWords((237, 201 , 627, 263))
            if len(list) != 0 and '低心情' in list[0]:
                util.logOut(__file__,'我是粪提 结束')
                isRedFace = True
                x , y = self.picLoop(self.publicPath() + 'bmp/OK.jpg')
                util.click(x,y)
                time.sleep(1.500)
        #船坞已满特殊
        util.logOut(__file__,'船坞已满判断 开始')
        x, y = util.findPic(self.publicPath() + 'bmp/zhengli.jpg')
        if x!=-1 and y!=-1:
            util.logOut(__file__,'船坞已满')
            util.click(x,y)
            self.retireProcess()
            time.sleep(.800)
            anchor()	
            if isRedFace:
                time.sleep(2.00)
                x , y = util.findPic(self.publicPath() + 'bmp/OK.jpg')
                if x!=-1 and y!=-1:
                    util.click(x,y)
                    time.sleep(1.500)
        time.sleep(10)
        #S
        x , y = self.picLoop(self.publicPath() + 'bmp/S.bmp',0.6)
        util.logOut(__file__,'自律 结束')
        time.sleep(1.200)
        util.click(x,y)
        #get_items
        time.sleep(.800)
        util.click(684,308)
        time.sleep(1.600)
        #打捞到sr或ssr（不存在的）
        util.logOut(__file__,'打捞到sr或ssr判断 开始')
        if util.isFindPic(self.publicPath() + 'bmp/salvage.jpg'):
            util.logOut(__file__,'打捞到sr或者ssr')
            util.click(684,308)
            time.sleep(2)
        util.click(684,308)
        #exp2
        x , y = self.picLoop(self.publicPath() + 'bmp/exp2.bmp')
        util.click(x,y)
        time.sleep(3)
        #作战失败 特殊
        util.logOut(__file__,'作战失败判断 开始')
        xx , yy = util.findPic(self.publicPath() + 'bmp/death.jpg')
        if xx!=-1 and yy!=-1:
            util.logOut(__file__,'作战失败')
            util.click(xx,yy)
        time.sleep(3)
        #紧急委托 特殊
        util.logOut(__file__,'紧急委托判断 开始')
        xx , yy = util.findPic(self.publicPath() + 'bmp/OK.jpg')
        if xx!=-1 and yy!=-1:
            util.logOut(__file__,'紧急委托')
            util.click(xx,yy)
        util.logOut(__file__,'anchorProcess 出击步骤结束')
    
    #进入出击章节
    #chapterNum:章节数字
    # type：普通'N' 困难'H'
    def chapterProcess(self, chapterNum ,type):
        util.logOut(__file__,'chapterProcess 进入出击章节步骤开始')
        chapterPos = (82, 43,141, 75)
        prevX , prevY = 33, 251
        nextX , nextY = 826, 251
        #返回主页面
        self.backMainProcess()
        #进入出击界面
        x , y = self.picLoop(self.publicPath() + 'bmp/weigh anchor.jpg')
        util.click(x,y)
        # 判断是否为图里面
        util.logOut(__file__,'判断是否为图里面 开始')
        time.sleep(2.000)
        x,y = util.findPic(self.publicPath() + 'bmp/withdraw.jpg')
        if x!=-1 and y!=-1:
            util.click(x,y)
            x, y = self.picLoop(self.publicPath() + 'bmp/OK.jpg')
            util.click(x,y)
        else:
            x, y = self.picLoop(self.publicPath() + 'bmp/main battleline.jpg')
            util.click(x,y)
        self.picLoop(self.publicPath() + 'bmp/exercise.jpg')
        #困难模式
        if type == 'H':
            x,y = util.findPic(self.publicPath() + 'bmp/hardmode.jpg')
            if x!=-1 and y!=-1:
                util.click(x,y)
                time.sleep(.2)
        elif type == 'N':
            x,y = util.findPic(self.publicPath() + 'bmp/nomalmode.jpg')
            if x!=-1 and y!=-1:
                util.click(x,y)
                time.sleep(.2)
        else:
            util.logOut(__file__,'chapterProcess的type有误')
        #第chapterNum章
        list = util.getNumbers(chapterPos)
        tempNum = int(list[0])
        if list != [] and tempNum != chapterNum:
            #判断当前章节 前往第chapterNum章
            chapterNumNow = tempNum
            while chapterNumNow != chapterNum:
                if chapterNumNow < chapterNum:
                    util.click(nextX,nextY)
                    chapterNumNow += 1
                    time.sleep(.500)
                else:
                    util.click(prevX,prevY)
                    chapterNumNow -= 1
                    time.sleep(.500)
        
        util.logOut(__file__,'chapterProcess 进入出击章节步骤结束')

    #进入stage
    #x,y:stage的位置
    #first:上面选择的舰队
    #second:下面选择的舰队 0就清空
    def intoStageProcess(self ,xx,yy , first = -1 , second = -1, redFace = False):
        util.logOut(__file__,'intoStageProcess 进入stage步骤开始')
        def tempInto(x,y):
            util.click(x , y)
            x , y = self.picLoop(self.publicPath() + 'bmp/start chapter.jpg')
            util.click(x,y)
            time.sleep(.800)
        time.sleep(4.00)
        tempInto(xx,yy)
        #船坞已满特殊
        util.logOut(__file__,'船坞已满判断 开始')
        time.sleep(.500)
        x, y = util.findPic(self.publicPath() + 'bmp/zhengli.jpg')
        if x!=-1 and y!=-1:
            util.logOut(__file__,'船坞已满')
            util.click(x,y)
            const.retireProcess()
            time.sleep(4.000)
            tempInto(xx,yy)
        if first != -1 and second != -1:
            #清空 第二个队伍
            util.click(767, 220)
            time.sleep(.200)
            #选择1 
            util.click(713, 131)
            time.sleep(.200)
            #第first队伍
            util.click(740, 176 + (first - 1) * 28)
            time.sleep(.200)
            if second != 0:
                #选择2
                util.click(714, 223)
                time.sleep(.200)
                #第second队伍
                util.click(740, 266 + (second - 1) * 28)

        x , y = self.picLoop(self.publicPath() + 'bmp/start chapter.jpg')
        util.click(x,y)
        if redFace:
            util.logOut(__file__,'红脸判断 开始')
            time.sleep(1.000)
            list = util.getWords((237, 201 , 627, 263))
            if len(list) != 0 and '低心情' in list[0]:
                util.logOut(__file__,'红脸')
                x , y = self.picLoop(self.publicPath() + 'bmp/OK.jpg')
                util.click(x,y)
        util.logOut(__file__,'intoStageProcess 进入stage步骤结束')

    #走boss格子
    def goBossProcess(self):
        util.logOut(__file__,'goBossProcess 走boss格子 开始')
        x , y = self.picLoop(self.publicPath() + 'bmp/boss.jpg',threshold=0.6)
        util.click(x,y)
        self.anchorProcess()
        util.logOut(__file__,'goBossProcess boss解决')

    # 重启
    def restartProcess(self):
        util.logOut(__file__,'restartProcess 重启脚本开始')
        util.adb('shell am force-stop com.bilibili.azurlane')
        util.adb('shell am start -n com.bilibili.azurlane/com.manjuu.azurlane.MainActivity')

        util.logOut(__file__,'findPicLoop 循环找图开始 '+const.publicPath() + 'bmp/login.jpg')
        while True:
            x, y = util.findPic(const.publicPath() + 'bmp/login.jpg')
            if x != -1 and y != -1:
                util.logOut(__file__,'findPicLoop 循环找图结束 '+const.publicPath() + 'bmp/login.jpg')
                break

        findLoginCnt = 5
        while findLoginCnt != 0:
            util.click(200,200)
            x, y = util.findPic(const.publicPath() + 'bmp/login.jpg')
            if x == -1 and y == -1:
                findLoginCnt = findLoginCnt - 1
            
        util.logOut(__file__,'findPicLoop 循环找图开始 '+'weigh anchor、login-btn、get_items、salvage、home、quit')
        while True:
            x, y = util.findPic(const.publicPath() + 'bmp/weigh anchor.jpg')
            if x != -1 and y != -1:
                break
            x, y = util.findPic(const.publicPath() + 'bmp/login-btn.jpg')
            if x != -1 and y != -1:
                util.click(x,y)
                continue
            x, y = util.findPic(const.publicPath() + 'bmp/get_items.bmp')
            if x != -1 and y != -1:
                util.click(x,y)
                continue
            x, y = util.findPic(const.publicPath() + 'bmp/salvage.jpg')
            if x != -1 and y != -1:
                util.click(200,200)
                continue
            x, y = util.findPic(const.publicPath() + 'bmp/home.jpg')
            if x != -1 and y != -1:
                util.click(x,y)
                continue
            x, y = util.findPic(const.publicPath() + 'bmp/quit.jpg')
            if x != -1 and y != -1:
                util.click(x,y)
                continue

        util.logOut(__file__,'restartProcess 重启脚本结束')

    #找船
    __templates = []
    def findShip(self,x,y,num,path,ignore=[0,0,0,0]):
        util.logOut(__file__,'findShip 找船 开始')
        SEARCH_SIZE = (84, 36,864, 439)
        if self.__templates == []:
            for i in range(num):
                template = cv2.imread(path + str(i)+'.jpg',0)
                self.__templates.append(template)
        img = util.grab(SEARCH_SIZE)
        # cv2.rectangle(img,(0,0),(61, 116),(255,0,0),-1)
        cv2.rectangle(img,(0,0),(263, 65),(255,0,0),-1)
        # 改过了长度
        if ignore != [0,0,0,0]:
            cv2.rectangle(
                img,
                (ignore[0]-SEARCH_SIZE[0],ignore[1]-SEARCH_SIZE[1]),(ignore[2]-SEARCH_SIZE[0], ignore[3]-SEARCH_SIZE[1]),
                (255,0,0),
                -1
            )

        list = [None for i in range(num)]
        def foo(i):
            temp = util.findPic(None,threshold = 0.7, img = img,template = self.__templates[i])
            tempList = []
            for value in temp:
                tempList.append(value)
            if tempList != [-1,-1]:
                tempList[0] += SEARCH_SIZE[0]
                tempList[1] += SEARCH_SIZE[1]
            list[i] = tempList
        for i in range(num):
            foo(i)
        '''
        threads = []
        for i in range(num):
            threads.append(threading.Thread(target=foo,args=(i,)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        '''
        
        minDistance = sys.maxsize
        minIndex = 0
        index = -1
        for value in list:
            index += 1
            if value == [-1,-1]:
                continue
            temp = (value[0] - x)**2 + (value[1] - y)**2
            if temp < minDistance:
                minDistance = temp
                minIndex = index
        util.logOut(__file__,'findShip 找船 结束')
        return list[minIndex][0],list[minIndex][1]
    
    # 获取path内有多少图需要搜索
    def getPicNum(self,path):
        num = 0
        for fileName in os.listdir(path):
            try:
                int(fileName[0])
                num += 1
            except ValueError:
                pass
        return num

    # 带重启的找图
    def picLoop(self, url, threshold=0.8, size=(0, 0, 0, 0)):
        x,y = util.findPicLoop(url, threshold=threshold, size=size)
        if x==-2 and y==-2:
            util.logOut(__file__,'picLoop没找到图 需要重启脚本！！！！！！')
            self.restartProcess()
            raise ValueError('restart')
        return (x,y)
    
const = Const()