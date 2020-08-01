from util import *

class Const:
	def __init__(self):
		pass
		
	#获取根path
	def path(self):
		return "../"

	#图片资源path
	def publicPath(self):
		return self.path + "public/"

	#临时path
	def tmpPath(self):
		return self.path + "tmp/"

	#返回主页面
	def backMainProcess(self):
		if util.isFindPic(self.publicPath + "home.jpg",0.8):
			x , y = util.findPic(self.publicPath + "home.jpg",0.8)
			pyautogui.click(x,y)
			time.sleep(.500)
		elif util.isFindPic(self.publicPath + "weigh anchor.jpg"):
			return
		else:
			print("返回主页面失败")
			util.exitScript()

	#退役蓝白未锁的船
	def retireProcess(self):
		print("开始退役步骤")
		time.sleep(2)
		#常用点掉
		if util.isFindColor(554, 108, (74, 113, 140)):
			pyautogui.click(554, 108)
			time.sleep(2)
		#筛选
		pyautogui.click(869,118)
		time.sleep(2)
		pyautogui.click(439,183)
		time.sleep(2)
		pyautogui.click(343,231)
		time.sleep(2)
		pyautogui.click(353,321)
		time.sleep(2)
		pyautogui.click(338,417)
		time.sleep(2)
		pyautogui.click(444,412)
		time.sleep(2)
		pyautogui.click(550,410)
		time.sleep(2)
		pyautogui.click(342,461)
		time.sleep(2)
		pyautogui.click(635,534)
		time.sleep(2)
		while True:
			list = util.getWords((153, 322,371, 366))
			if list!=[] and list[0][0] == '暂':
				#退出
				pyautogui.click(137,136)
				return
			x,y = 212,218
			width = 666 // 6
			for i in range(6):
				pyautogui.click(x,y)
				x += width
				time.sleep(.100)
			pyautogui.click(x,y)
			#判断确定按钮颜色是否为灰   
			if util.isFindColor(842,553,(107,69,33)):
				#退出
				pyautogui.click(137,136)
				return
			#已选中确定
			x,y = util.findPicLoop(self.publicPath + "OK.jpg")
			pyautogui.click(x,y)
			#二重确定
			time.sleep(2)
			x,y = util.findPicLoop(self.publicPath + "OK.jpg")
			pyautogui.click(x,y)
			#判断是否有精锐
			time.sleep(2)
			x,y = util.findPic(self.publicPath + "OK.jpg")
			if x!=-1 and y!=-1:
				pyautogui.click(x,y)
			#获得道具
			x , y = util.findPicLoop(self.publicPath + "get_items.bmp")
			time.sleep(2)
			pyautogui.click(x,y)
			#拆解装备
			time.sleep(2)
			x,y = util.findPicLoop(self.publicPath + "OK.jpg")
			pyautogui.click(x,y)
			#二重确定
			time.sleep(2)
			x,y = util.findPicLoop(self.publicPath + "OK.jpg")
			pyautogui.click(x,y)
			#获得道具
			x , y = util.findPicLoop(self.publicPath + "get_items.bmp")
			time.sleep(2)
			pyautogui.click(x,y)
			time.sleep(2)

	#出击到结束的过程
	def anchorProcess(self):
		time.sleep(.800)
		#今日不再提示
		x,y = util.findPic(self.publicPath + "quit.jpg")
		if x!=-1 and y!=-1:
			pyautogui.click(627,425)
			time.sleep(.200)
			pyautogui.click(x,y)
   
		def anchor():
			x , y = util.findPicLoop(self.publicPath + "anchor.bmp")
			time.sleep(0.800)
			pyautogui.click(x,y)
			
		anchor()
		time.sleep(.800)
		#红脸特殊（屑）
		'''
		x , y = util.findPic(self.publicPath + "OK.jpg")
		if x!=-1 and y!=-1:
			print("我是粪提")
			pyautogui.click(x,y)
			time.sleep(2.000)
		'''
		#船坞已满特殊
		x, y = util.findPic(self.publicPath + "zhengli.jpg")
		if x!=-1 and y!=-1:
			pyautogui.click(x,y)
			self.retireProcess()
			time.sleep(.800)
			anchor()	
		time.sleep(10)
		#S
		x , y = util.findPicLoop(self.publicPath + "S.bmp",0.6)
		time.sleep(1.200)
		pyautogui.click(x,y)
		#get_items
		time.sleep(.800)
		pyautogui.click(784,408)
		time.sleep(1.600)
		#打捞到sr或ssr（不存在的）
		if util.isFindPic(self.publicPath + "salvage.jpg"):
			print("打捞到sr或者ssr了")
			pyautogui.click(784,408)
			time.sleep(2)
		pyautogui.click(784,408)
		#exp2
		x , y = util.findPicLoop(self.publicPath + "exp2.bmp")
		pyautogui.click(x,y)
		time.sleep(3)
		#作战失败 特殊
		xx , yy = util.findPic(self.publicPath + "death.jpg")
		if xx!=-1 and yy!=-1:
			pyautogui.click(xx,yy)
		print("一把结束")
		time.sleep(3)
		#紧急委托 特殊
		xx , yy = util.findPic(self.publicPath + "quit.jpg")
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
		if not util.isFindPic(self.publicPath + "exercise.jpg"):
			#返回主页面
			self.backMainProcess()
			#进入出击界面
			x , y = util.findPicLoop(self.publicPath + "weigh anchor.jpg")
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
			x,y = util.findPic(self.publicPath + "hardmode.jpg")
			if x!=-1 and y!=-1:
				pyautogui.click(x,y)
				time.sleep(.2)
		elif type == 'N':
			x,y = util.findPic(self.publicPath + "nomalmode.jpg")
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
			x , y = util.findPicLoop(self.publicPath + "start chapter.jpg")
			pyautogui.click(x,y)
			time.sleep(.800)
		tempInto(xx,yy)
		#船坞已满特殊
		time.sleep(.500)
		x, y = util.findPic(self.publicPath + "zhengli.jpg")
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

		x , y = util.findPicLoop(self.publicPath + "start chapter.jpg")
		pyautogui.click(x,y)
		
	#走boss格子
	def goBossProcess(self):
		x , y = util.findPicLoop(self.publicPath + "boss.jpg",threshold=0.6)
		time.sleep(1.000)
		pyautogui.click(x,y)
		#self.accident(x,y)
		self.anchorProcess()
		print("boss解决")

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
			if util.isFindPic(self.publicPath + "anchor.bmp"):
				return
			#伏击
			xx , yy = util.findPic(self.publicPath + "guibi.jpg")
			if xx!=-1 and yy!=-1:
				pyautogui.click(xx,yy)
				time.sleep(1.000)
				list = util.getWords((879, 440,1044, 493))
				if list != [] and list[0] == "规避失败":
					const.anchorProcess()
			#空袭
			pyautogui.click(x,y)
			time.sleep(1)
	'''
			
	#找船
	__templates = []
	def findShip(self,x,y,num,path):
		SEARCH_SIZE = (184, 136,964, 539)
		if self.__templates == []:
			for i in range(num):
				template = cv2.imread(path + str(i)+'.jpg',0)
				self.__templates.append(template)
		img = util.grab(SEARCH_SIZE)
		cv2.rectangle(img,(0,0),(61, 116),(255,0,0),-1)
		cv2.rectangle(img,(0,0),(213, 65),(255,0,0),-1)

		list = [None for i in range(num)]
		def foo(i):
			temp = util.findPic(None,threshold = 0.9, img = img,template = self.__templates[i])
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
			temp = (value[0] - x)**2 + (value[1] - y)**2
			if temp < minDistance:
				minDistance = temp
				minIndex = index
		return list[minIndex][0],list[minIndex][1]
	
const = Const()