s aux
ps aux
apt update
apt install git
apt install php
php --ini |grep Loaded
l /etc/php/
l /etc/php/7.2/
apt install nginx
apt install php-fpm
cd /var/www/html/
ls -la
rm -rf index.html 
mv index.nginx-debian.html index.html
l
git clone https://github.com/bolt/bolt.git
l
ls -la
cd bolt/
ls -la
useradd -m bolt
cd /home/
l
ls -la
userdel bolt
l
rm -rf bolt/
cd /root/
l
ls -la
mkdir .ssh
cd .ssh/
l
ls -la
vi config
edit config
apt install vim
vi config
ssh-keygen -t rsa -b 4096 -C "bolt@registry.htb"
l
ls -la
cd ..
ls -la
ssh-add /root/.ssh/id_rsa
eval `ssh-agent -s`
ssh-add /root/.ssh/id_rsa
ps aux | grep ssh
l /etc/profile.d/
l /etc/profile.d/01-locale-fix.sh 
cat /etc/profile.d/01-locale-fix.sh 
cat /etc/profile
l /etc/bash.bashrc
cat /etc/bash.bashrc
l
wd
pwd
ls -la
cat .profile 
cat .bashrc 
l
vi /etc/profile.d/01-ssh.sh
apt install expect
which expect
vi /etc/profile.d/01-ssh.sh
l /etc/profile.d/
ls -la /etc/profile.d/
sh /etc/profile.d/01-ssh.sh 
which spawn
apt install spawn
chmod +x /etc/profile.d/01-ssh.sh 
/etc/profile.d/01-ssh.sh 
cat /etc/profile.d/01-ssh.sh 
ps aux
vi /etc/profile.d/01-ssh.sh
/etc/profile.d/01-ssh.sh 
vi /etc/profile.d/01-ssh.sh
/etc/profile.d/01-ssh.sh 
ps aux
ssh registry
ping registry.htb
apt install ping
apt install iputils-ping
ping registry.htb
cat .ssh/id_rsa.pub 
ssh registry
cd /etc/profile.d/
l
cp 01-ssh.sh 02-ssh.sh 
vi 01-ssh.sh 
ssh 01-ssh.sh 
chmod +x 01-
chmod +x 01-ssh.sh 
./01-ssh.sh 
ps aux
kill 11162 11241 11365
ssh registry
cat /etc/profile
l
cd /root/
ls -la
cat .profile 
vi .profile 
ps aux
cat /etc/profile.d/01-ssh.sh 
vi .profile 
eval `ssh-agent -s`
vi .profile 
ps aux
systemctl restart nginx.service
/etc/init.d/nginx start
/etc/init.d/php7.2-fpm start
ps aux
l
ls -la
cd /var/www/html/
l
vi sync.sh
chmod +x sync.sh 
./sync.sh 
apt install rsync
./sync.sh 
l
/etc/profile.d/01-ssh.sh 
/etc/profile.d/02-ssh.sh 
./sync.sh 
l
ls -la
rm -rf bolt/
./sync.sh 
l
ls -la
cd bolt/
ls -la
cd ..
l
rm -rf bolt
l
ls -la
cat sync.sh 
ps aux
kill 11412 11531
ps aux
cd /
ls -la
cd /home/
l 
ls -la
exit
