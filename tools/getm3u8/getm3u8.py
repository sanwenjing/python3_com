# -*- coding:utf-8 -*-
from selenium import webdriver
from com import getArgs
targetUrl=getArgs(1)
targetVal=getArgs(2)
timeout=20
#print targetUrl
driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
driver.set_page_load_timeout(timeout)
driver.set_script_timeout(timeout)
try:
  driver.get(targetUrl)
except:
  driver.execute_script('window.stop()')
#num = driver.execute_script("return MacPlayer.PlayUrl")
num = driver.execute_script("return "+targetVal)
#num = driver.execute_script("return new Date().getTime()")
print num
driver.quit()
