#bin/sh
rs=`date|awk '{print $4}'|awk -F: '{print $1""":"""$2}'`
echo $rs

#Food CTRL
if [ "$rs" = "12:55" ]
then
`curl 192.168.31.102?action=OFF1>/dev/null 2>&1`
fi

#Food CTRL
if [ "$rs" = "12:59" ]
then
`curl 192.168.31.102?action=ON1>/dev/null 2>&1`
fi

#TV CTRL
if [ "$rs" = "23:00" ]
then
`curl 192.168.31.145?action=ON1>/dev/null 2>&1`
fi
