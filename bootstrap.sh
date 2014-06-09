sudo apt-get update

echo mysql-server-5.5 mysql-server/root_password password "" | sudo debconf-set-selections
echo mysql-server-5.5 mysql-server/root_password_again password "" | sudo debconf-set-selections
sudo apt-get install -y mysql-server mysql-client python-mysqldb python-pip python-dev

sudo pip install -U pip
sudo pip install alembic itsdangerous

result=$(mysql -u root -s -N -e "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='tests'");
if [ -z "$result" ];
then
    echo 'CREATING tests DATABASE'
    mysql -u root -e "CREATE DATABASE tests CHARACTER SET utf8;"
else
    echo 'NO NEED TO CREATE tests DATABASE'
fi

echo "export PYTHONPATH=/vagrant" >> /home/vagrant/.bashrc
