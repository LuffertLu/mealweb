sudo apt-get update
sudo apt-get upgrade
sudo apt-get install mysql-server
sudo pip3 install mysqlclient
sudo service mysql start
echo "need to create user in db consle"
echo "sudo mysql -u root"
echo "mysql>create user 'admin'@'localhost' IDENTIFIED BY '1qaz';"
echo "mysql>create database meal-dev character set = utf8;"
echo "mysql>grant all on meal_dev.* to 'admin'@'localhost';"
echo "mysql>create database meal character set = utf8;"
echo "mysql>grant all on meal.* to 'admin'@'localhost';"
echo "exit"