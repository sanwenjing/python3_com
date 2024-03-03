#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys,time,random,requests,re
import datetime as dt;
import platform as pf;
import configparser  #ini



class log:
      fd="";
      def __init__(self,fileaddr=""):
            filepath=getArgs(0);
            if(fileaddr):
                  self.fd=fileaddr;
            else:
                  self.fd=getRunPath()+"/"+getFileName()+".log";
      def getFd(self):
            return(self.fd);
      def w(self,text):
            of=open(self.fd,'a');
            of.write(getTime()+"  "+text+"\r\n");
            of.close();
            return;
def getArgs(position):
    if(len(sys.argv)>=position+1):
        return sys.argv[position];
    else:
        return "";
def getAddrStr(address):
      if getSystemClass()=="Windows":
            return address.replace("/","\\");
      else:
            return address.replace("\\","/");
def getTime():
      return getTimeFormat('%Y-%m-%d %H:%M:%S');
def getTimeFormat(format):
      now=dt.datetime.now();
      return now.strftime(format);
def getHM():
    return getTimeFormat("%H:%M");
def sleep(seconds):#延时程序
      time.sleep(seconds);
def getFileName():
    fn=sys.argv[0][sys.argv[0].rfind(os.sep) + 1:];
    return fn.split(".")[0];

def getSystemClass():
      return pf.system();
def getRunPath():
    curPath=getArgs(0);
    if curPath[0]!="/":
        return getLeft(os.getcwd()+"/"+ curPath,"/");
    else:
        return getLeft(curPath,"/");
def getLeft(string,keyword):
    keyposition=string.rfind(keyword)
    if keyposition>=0:
        return string[0:keyposition];
    else:
        return string;
def killByKw(keyword):#命令行关键字终结程序
      os.system("ps -ef|grep "+keyword+" |awk '{print $2}'|xargs kill -9");
def getHtml(url):#取HTML代码,利用CURL
    html=os.popen("curl "+url)
    htmltxt=""
    while 1:
        line=html.readline()
        if line:
            htmltxt+=line
        else:
            break
    return htmltxt
def isrun(keyword):#判断运行状态
    rs=os.popen("ps -ef |grep '"+keyword+"'|grep -v grep")
    if rs.readline():
        return 1
    else:
        return 0
        
#For adb to get multi devices id
def getDevID():
  if getSystemClass()=="Windows":
    r=os.popen("adb devices |findstr /V devices")
  else:
    r=os.popen("adb devices |grep -v devices")
  #text=r.read()
  #print text
  output=[]
  while 1:
    line=r.readline()
    if not line:
      break
    res=getLeft(line,"device").rstrip()
    #Exit if nothing
    if len(res)==0:
      break
    #print res
    #swipe(res)
    output.append(res)
  r.close()
  return output
  
#send a adb command for swiping
def swipe(DevID):
  x1=291+random.randint(1,100)
  y1=726+random.randint(-50,50)
  x2=291+random.randint(1,100)
  y2=243+random.randint(-50,50)
  #sleepTime=random.randint(1,5)
  #time.sleep(sleepTime)
  cmdline="adb -s {dev} shell input swipe {x1} {y1} {x2} {y2} 200".format(dev=DevID,x1=x1,y1=y1,x2=x2,y2=y2)
  os.system(cmdline)
  #print cmdline

#run cmd bg
def bgrun(cmd):
  cmdline="nohup {cmd}>/dev/null 2>&1 &".format(cmd=cmd)
  print(cmdline)
  os.system(cmdline)

def isrun(progName):
  r=os.popen("ps -ef|grep {kw}|wc -l".format(kw=progName))
  res=r.readline()
  r.close()
#  print res
#  print int(res)
  if int(res)>2:
    return True
  else:
    return False

def utf8ToGbk(text):
  return text.decode("utf-8").encode("gbk")

def gbkToUtf8(text):
  return text.decode("gbk").encode("utf-8")

class Config:
    def __init__(self, path=os.path.join(os.path.dirname(os.path.realpath(__file__)),getFileName()+".ini")):
        self.path = path
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path)
    def get(self,key,field="system"):
        result = ""
        try:
            result = self.cf.get(field, key)
        except:
            result = ""
        return result
    def set(self,key,value,field="system"):
        try:
          self.cf.add_section(field)
        except:
          pass
        self.cf.set(field, key, value)
        self.cf.write(open(self.path,'w'))

def useAliyunSource():
  os.system("pip config set global.index-url https://mirrors.aliyun.com/pypi/simple")


def mkDir(dirName):
# 检查input文件夹是否存在
  if not os.path.exists(dirName):
    os.makedirs(dirName)
def download(fileurl,title,dir="download\\"):#title如 XXX.mp4
  mkDir(dir)#建目录
  file_content = requests.get(url=fileurl).content
  with open(dir + title, mode='wb') as f:
    f.write(file_content)
    
def getCmdText(cmd): #取命令行运行结果
  r = os.popen(cmd)
  res=r.read()
  r.close()
  return res


def getChinese(text): #取文本中所有汉字,用于文件名
  chinese_pattern = re.compile("[\u4e00-\u9fa5]")
  chinese_chars = chinese_pattern.findall(text)
  chinese_text = ''.join(chinese_chars)
  return chinese_text

  
if __name__=="__main__":
         #log1=log();
         #log1.w("test");
         #conf1=Config();
         #print conf1.getFd();
         #conf1.set("test","123456nihao")
         #print(conf1.get("test"))
         #mkDir(".\\input")
         #useAliyunSource()
         #download("https://vdept3.bdstatic.com/mda-qc20br3dig0x0bg5/sc/cae_h264/1709424976869467322/mda-qc20br3dig0x0bg5.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1709438932-0-0-aadb6d7851b811493c024a27c958dcf6&bcevod_channel=searchbox_feed&cr=2&cd=0&pd=1&pt=3&logid=0532247206&vid=10254206589342494431&klogid=0532247206&abtest=116096_1","荣庵老师为粉丝、学员讲解 ——享荫福厚 才学富足 荣庵老师 婚期择吉 易学 传承和弘扬民族文化 弘扬传统文化 荣庵讲易 十二生肖 智慧人生"+".mp4")
         print(getCmdText("dir"))
         #print getHtml("www.baidu.com")         
