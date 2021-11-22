#!/bin/bash
yum -y update
yum -y install httpd
service httpd start
aws s3 cp s3://solina/index.php /var/www/html/
aws s3 cp s3://solina/login.php /var/www/html/
aws s3 cp s3://solina/login2.php /var/www/html/
aws s3 cp s3://solina/r2.php /var/www/html/
aws s3 cp s3://solina/show.php /var/www/html/
aws s3 cp s3://solina/feed.php /var/www/html/

