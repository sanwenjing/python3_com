#-*- coding:utf-8 -*-
import RPi.GPIO as io#IO函数导入
io.setmode(io.BOARD)
io.setwarnings(False)
#配置通道类型
def setAction(outpin,ac):
        io.setup(outpin,io.OUT)
        if ac=="ON":
                if io.input(outpin)<>1:
			io.output(outpin,io.HIGH)
                	print(str(outpin)+":ON")
			return True
		else:
			return False
        else:   
                if io.input(outpin)<>0:
			io.output(outpin,io.LOW)
                	print(str(outpin)+":OFF")
			return True
		else:
			return False
if __name__ == '__main__':
	setAction(13,"OFF")
	print(io.input(13))
