echo "init ssh proxy design by sanwenjing @ 2019.12.11"
echo ""
echo "Create a new ssh-keygen?(y/n)"
read key
if [ $key = 'y' ]; then
echo "Input the hostname@location e.g. testhost@home"
read key
if [ $key != '' ]; then
ssh-keygen -t rsa -C $key
fi
fi

#transfer key

echo "Transfer key?(y/n)"
read key
if [ $key = 'y' ]; then
echo "Input the proxy host info:-p port root@ip e.g. -p 222 root@ip"
read key
#if [ $key != ' ' ]; then
echo $key
ssh-copy-id -i ~/.ssh/id_rsa.pub $key
#fi
fi
