from util import *
from const import const

CHAPTER_NUM = 6	#几-几
CHAPTER_NUM2 = 4	#几-几
CHAPTER_X , CHAPTER_Y = 352, 412	#几-几的坐标
START_X , START_Y = 780, 281 #进stage后初始位置
CNT = 5	#几次出boss
path = './normal6-4/'
PIC_NUM = 21	#多少张图


if __name__ == "__main__":
	time.sleep(2)
	print(str(CHAPTER_NUM) + "-" + str(CHAPTER_NUM2) + "脚本开始")
	const.chapterProcess(CHAPTER_NUM, "N")
	while True:
		#进入
		print(str(CHAPTER_NUM) + "-" + str(CHAPTER_NUM2) + "开始")
		const.intoStageProcess(CHAPTER_X,CHAPTER_Y)
		#走格子 
		X, Y = START_X, START_Y
		#打CNT个出boss
		for n in range(CNT):
			util.findPicLoop('./bmp/withdraw.jpg') 
			#等待搜索雷达
			time.sleep(4.000)
			X , Y = const.findShip(X,Y,PIC_NUM,path)
			pyautogui.click(X , Y)
			const.anchorProcess()
		#boss
		util.findPicLoop('./bmp/withdraw.jpg') 
		#等待搜索雷达
		time.sleep(4.000)
		const.goBossProcess()
		print("-------------------------")
		
		