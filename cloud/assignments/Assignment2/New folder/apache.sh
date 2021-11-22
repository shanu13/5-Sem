#!/usr/bin/sh


sudo yum -y install httpd
sudo systemctl stop httpd.service
sudo systemctl start httpd.service
sudo systemctl enable httpd.service

mkdir assignment_2

# aws s3 cp s3://cloud1901182/* ./assignment_2/ -r
wget https://cloud1901182.s3.amazonaws.com/index.html -P ./assignment_2/
