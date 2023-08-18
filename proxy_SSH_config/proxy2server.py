#!/usr/bin/python
# -*- coding: UTF-8 -*-
#SSH反向代理守护脚本,命令存储在tasklist文件中
import os,sys;
import com;
def checkOL():
    print "Starting checkOnline now!"
    cpath=com.getRunPath()
    #print cpath
    tasklist=open(cpath+"/tasklist")
    task=tasklist.readline().replace("\n","");
    while task:
        kw=" ".join(task.split(" ")[2:])
        #print kw
        if(com.isrun(kw)):
            print "running:"+task
        else:
            if task.find("#")<0:#不执行注释
                print "norunning:"+task
                print "starting..."#执行任务
                os.system(task)
                log=com.log();#日志记录
                log.w(task+":executed")
        task=tasklist.readline().replace("\n","")
    tasklist.close()
if __name__=="__main__":
            if(len(sys.argv)>=2):
                cmd=com.getArgs(1);
                if(cmd=="stop"):
                    com.killByKw("qngfCNTR");
                elif(cmd=="restart"):
                    print("killlinks:");
                    com.killByKw("qngfCNTR");
                    com.sleep(1);
                    checkOL();
                elif(cmd=="start"):
                    checkOL();
