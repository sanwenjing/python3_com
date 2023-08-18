#!/bin/sh

#check the homebridge run status
bin="homebridge"
start(){
status=`/etc/init.d/$bin status`
if [ "$status" = "Stopped" ] 
then
	`/etc/init.d/$1 start>/dev/null 2>&1`
	echo "Starting $1 now"
else 
	echo "The $1 is "$status
fi
}
stop(){
	`ps -ef|grep $1|grep -v grep|awk '{print $2}'|xargs kill -9`
	echo "$1 stoped!"
}
case $1 in
"start")
	start $bin
;;
"stop")
	stop $bin
;;
"restart")
	stop $bin
	start $bin
;;
"status")
	echo "$bin status:`/etc/init.d/$bin status`"
;;
*)
	echo "usage: start|stop|restart|status"
;;
esac
