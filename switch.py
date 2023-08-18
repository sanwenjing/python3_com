#-*- coding:utf-8 -*-
#！/usr/bin/python
from ioc import setAction
import com
cpin=com.getArgs(1)

if cpin=="":
	print(com.getArgs(0)+": not enough arguments")
	exit()
cpin=int(cpin)
for i in range(1,3):
	setAction(cpin,"ON1")
	com.sleep(0.2)
	setAction(cpin,"ON")
	com.sleep(0.2)
