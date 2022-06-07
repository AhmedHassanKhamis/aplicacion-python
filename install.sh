git clone https://github.com/coolacid/docker-misp.git
git clone https://github.com/ahmedhassank/corteza.git
chown 1001:1001 corteza/data/db
chown 4242:4242 corteza/data/server
apt-get install python3-pyqt5 -y
apt-get install pyqt5-dev-tools -y
apt-get install qttools5-dev-tools -y
apt update
apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt update
apt-cache policy docker-ce
apt install docker-ce -y
curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
sysctl -w vm.max_map_count=262144
echo "127.0.0.1	dominio.cm" >> /etc/hosts
service apache2 stop && service nginx stop
whoami | usermod -aG docker
id -nG
