# -*- coding:utf-8 -*-
from selenium import webdriver #pip uninstall selenium  &&  pip install selenium==2.48.0
from com import getArgs
targetUrl=getArgs(1)
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
num = driver.execute_script("return player_aaaa.url")
#num = driver.execute_script("return new Date().getTime()")
print(num)
driver.quit()
