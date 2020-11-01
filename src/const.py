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
        if util.isFindPic(self.publicPath() + 'bmp/home.jpg',0.8):
            x , y = util.findPic(self.publicPath() + 'bmp/home.jpg',0.8)
            pyautogui.click(x,y)
            time.sleep(.500)
        elif util.isFindPic(self.publicPath() + 'bmp/weigh anchor.jpg'):
            return
        else:
            print('返回主页面失败')

    #退役蓝白未锁的船
    def retireProcess(self):
        print('开始退役步骤')
        time.sleep(2)
        x,y = util.findPicLoop(self.publicPath() + 'bmp/retire.jpg')
        pyautogui.click(x,y)
        time.sleep(.800)
        x,y = util.findPicLoop(self.publicPath() + 'bmp/OK.jpg')
        pyautogui.click(x,y)
        x,y = util.findPicLoop(self.publicPath() + 'bmp/get_items.bmp')
        pyautogui.click(x,y)
        time.sleep(.800)
        x,y = util.findPicLoop(self.publicPath() + 'bmp/OK.jpg')
        pyautogui.click(x,y)
        time.sleep(.800)
        x,y = util.findPicLoop(self.publicPath() + 'bmp/OK.jpg')
        pyautogui.click(x,y)
        x,y = util.findPicLoop(self.publicPath() + 'bmp/get_items.bmp')
        pyautogui.click(x,y)
        x,y = util.findPicLoop(self.publicPath() + 'bmp/back.jpg')
        pyautogui.click(x,y)

    #出击到结束的过程
    def anchorProcess(self):
        time.sleep(.800)
        #今日不再提示
        x,y = util.findPic(self.publicPath() + 'bmp/quit.jpg')
        if x!=-1 and y!=-1:
            pyautogui.click(x,y)
   
        def anchor():
            x , y = util.findPicLoop(self.publicPath() + 'bmp/anchor.bmp')
            time.sleep(0.800)
            pyautogui.click(x,y)
            
        anchor()
        time.sleep(.800)
        #红脸特殊（屑）
        '''
        x , y = util.findPic(self.publicPath() + 'bmp/OK.jpg')
        if x!=-1 and y!=-1:
            print('我是粪提')
            pyautogui.click(x,y)
            time.sleep(2.000)
        '''
        #船坞已满特殊
        x, y = util.findPic(self.publicPath() + 'bmp/zhengli.jpg')
        if x!=-1 and y!=-1:
            pyautogui.click(x,y)
            self.retireProcess()
            time.sleep(.800)
            anchor()	
        time.sleep(10)
        #S
        x , y = util.findPicLoop(self.publicPath() + 'bmp/S.bmp',0.6)
        time.sleep(1.200)
        pyautogui.click(x,y)
        #get_items
        time.sleep(.800)
        pyautogui.click(784,408)
        time.sleep(1.600)
        #打捞到sr或ssr（不存在的）
        if util.isFindPic(self.publicPath() + 'bmp/salvage.jpg'):
            print('打捞到sr或者ssr了')
            pyautogui.click(784,408)
            time.sleep(2)
        pyautogui.click(784,408)
        #exp2
        x , y = util.findPicLoop(self.publicPath() + 'bmp/exp2.bmp')
        pyautogui.click(x,y)
        time.sleep(3)
        #作战失败 特殊
        xx , yy = util.findPic(self.publicPath() + 'bmp/death.jpg')
        if xx!=-1 and yy!=-1:
            pyautogui.click(xx,yy)
        print('一把结束')
        time.sleep(3)
        #紧急委托 特殊
        xx , yy = util.findPic(self.publicPath() + 'bmp/OK.jpg')
        if xx!=-1 and yy!=-1:
            pyautogui.click(xx,yy)
    
    #进入出击章节
    #chapterNum:章节数字
    # type：普通'N' 困难'H'
    def chapterProcess(self, chapterNum ,type):
        chapterPos = (182, 143,241, 175)
        prevX , prevY = 133, 351
        nextX , nextY = 926, 351
        #判断是否在出击章节界面
        #出击界面
        if not util.isFindPic(self.publicPath() + 'bmp/exercise.jpg'):
            #返回主页面
            self.backMainProcess()
            #进入出击界面
            x , y = util.findPicLoop(self.publicPath() + 'bmp/weigh anchor.jpg')
            pyautogui.click(x,y)
            time.sleep(2.000)
        #第chapterNum章
        list = util.getWords(chapterPos)
        tempNum = int(list[0][1:-1])
        if list != [] and tempNum != chapterNum:
            #判断当前章节 前往第chapterNum章
            chapterNumNow = tempNum
            while chapterNumNow != chapterNum:
                if chapterNumNow < chapterNum:
                    pyautogui.click(nextX,nextY)
                    chapterNumNow += 1
                    time.sleep(.500)
                else:
                    pyautogui.click(prevX,prevY)
                    chapterNumNow -= 1
                    time.sleep(.500)
        #困难模式
        if type == 'H':
            x,y = util.findPic(self.publicPath() + 'bmp/hardmode.jpg')
            if x!=-1 and y!=-1:
                pyautogui.click(x,y)
                time.sleep(.2)
        elif type == 'N':
            x,y = util.findPic(self.publicPath() + 'bmp/nomalmode.jpg')
            if x!=-1 and y!=-1:
                pyautogui.click(x,y)
                time.sleep(.2)
        else:
            print('chapterProcess的type有误')
            return

    #进入stage
    #x,y:stage的位置
    #first:上面选择的舰队
    #second:下面选择的舰队 0就清空
    def intoStageProcess(self ,xx,yy , first = -1 , second = -1):
        def tempInto(x,y):
            pyautogui.click(x , y)
            x , y = util.findPicLoop(self.publicPath() + 'bmp/start chapter.jpg')
            pyautogui.click(x,y)
            time.sleep(.800)
        tempInto(xx,yy)
        #船坞已满特殊
        time.sleep(.500)
        x, y = util.findPic(self.publicPath() + 'bmp/zhengli.jpg')
        if x!=-1 and y!=-1:
            pyautogui.click(x,y)
            const.retireProcess()
            time.sleep(4.000)
            tempInto(xx,yy)
        if first != -1 and second != -1:
            #清空 第二个队伍
            pyautogui.click(867, 320)
            time.sleep(.200)
            #选择1 
            pyautogui.click(813, 231)
            time.sleep(.200)
            #第first队伍
            pyautogui.click(840, 276 + (first - 1) * 28)
            time.sleep(.200)
            if second != 0:
                #选择2
                pyautogui.click(814, 323)
                time.sleep(.200)
                #第second队伍
                pyautogui.click(840, 366 + (second - 1) * 28)

        x , y = util.findPicLoop(self.publicPath() + 'bmp/start chapter.jpg')
        pyautogui.click(x,y)
        
    #走boss格子
    def goBossProcess(self):
        x , y = util.findPicLoop(self.publicPath() + 'bmp/boss.jpg',threshold=0.6)
        pyautogui.click(x,y)
        self.anchorProcess()
        print('boss解决')

    '''
    #左下角拖拽再居中(和分辨率有关系)
    def dragProcess(self):
        time.sleep(.500)
        for i in range(3):
            pyautogui.moveTo(459, 882, duration=0.25)
            pyautogui.dragTo(1644, 250, duration=0.25)
        pyautogui.moveTo(1460, 513, duration=0.25)
        pyautogui.dragTo(220, 719, duration=0.75)
    '''
    
    '''
    #意外情况
    def accident(self,x,y):
        while True:
            #没有意外
            if util.isFindPic(self.publicPath() + 'bmp/anchor.bmp'):
                return
            #伏击
            xx , yy = util.findPic(self.publicPath() + 'bmp/guibi.jpg')
            if xx!=-1 and yy!=-1:
                pyautogui.click(xx,yy)
                time.sleep(1.000)
                list = util.getWords((879, 440,1044, 493))
                if list != [] and list[0] == '规避失败':
                    const.anchorProcess()
            #空袭
            pyautogui.click(x,y)
            time.sleep(1)
    '''
            
    #找船
    __templates = []
    def findShip(self,x,y,num,path,ignore=[0,0,0,0]):
        SEARCH_SIZE = (184, 136,964, 539)
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
    
const = Const()