apt-get update -y
apt-get upgrade -y
sudo -s

apt-get install wget build-essential libncursesw5-dev libssl-dev \ libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

add-apt-repository ppa:deadsnakes/ppa

apt-get install python python2 python3 -y
pip3 install requests
pip3 install future
pip3 install pandas openpyxl
pip2 install pandas openpyxl
chmod + x *
python3 a.py
