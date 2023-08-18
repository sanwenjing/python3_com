# -*- coding: utf-8 -*-
 
"""
request mod:
xlrd==1.2.0
XlsxWriter==2.0.0

tips:
##pip freeze > req.txt
pip install -r req

"""
 
 
#将多个Excel文件合并成一个
import xlrd,os,com
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding("utf8")
 
#打开一个excel文件
def open_xls(file):
 print file
 fh=xlrd.open_workbook("input/"+file)
 return fh
 
#获取excel中所有的sheet表
def getsheet(fh):
 return fh.sheets()
 
#获取sheet表的行数
def getnrows(fh,sheet):
 table=fh.sheets()[sheet]
 return table.nrows
 
#读取文件内容并返回行内容
def getFilect(file,shnum):
 fh=open_xls(file)
 table=fh.sheets()[shnum]
 num=table.nrows
 for row in range(num):
  rdata=table.row_values(row)
  datavalue.append(rdata)
 return datavalue
 
#获取sheet表的个数
def getshnum(fh):
 x=0
 sh=getsheet(fh)
 for sheet in sh:
  x+=1
 return x
 
#遍历
def getfiles():
  path = '.\\input'
  try:
    path = unicode(path, 'utf-8') # 经过编码处理
  except:
    pass # python3 已经移除 unicode，而且默认是 utf8 编码，所以不用转
  return os.listdir(path)

 
if __name__=='__main__':
 #定义要合并的excel文件列表
 #allxls=['F:/test/excel1.xlsx','F:/test/excel2.xlsx']
 allxls=getfiles()
 #存储所有读取的结果
 datavalue=[]
 for fl in allxls:
  fh=open_xls(fl)
  x=getshnum(fh)
  for shnum in range(x):
   print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
   rvalue=getFilect(fl,shnum)
 #定义最终合并后生成的新文件
 endfile='output/result'+com.getTimeFormat('%Y%m%d%H%M%S')+'.xlsx'
 wb1=xlsxwriter.Workbook(endfile)
 #创建一个sheet工作对象
 ws=wb1.add_worksheet()
 for a in range(len(rvalue)):
  for b in range(len(rvalue[a])):
   c=rvalue[a][b]
   ws.write(a,b,c)
 wb1.close()
 print("文件合并完成")