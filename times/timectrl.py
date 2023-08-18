#!/usr/bin/python
import com;
def turn(tar,ac):
    com.getHtml("192.168.31."+tar+"?action="+ac+">/dev/null 2>&1")
if __name__ == '__main__':
    #print getCTP();
    time=com.getHM()
    log=com.log()
    print time;
    if(time=="07:30"):
        turn("102","OFF1")
        log.w("Food ON")
    if(time=="08:00"):
        turn("102","ON1")
        log.w("Food OFF")
    if(time=="23:00"):
        turn("145","ON1")
        log.w("TV OFF")

