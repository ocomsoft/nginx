#!/bin/bash
sudo docker build -t nginx .

mkdir  /home/ocom/docker/nginx/sites-available
mkdir  /home/ocom/docker/nginx/logs

sudo docker run -d -it --name nginx-www -p 80:80 -v /home/ocom/docker/nginx/sites-available:/etc/nginx/sites-enabled -v  /home/ocom/docker/nginx/logs:/var/log/nginx nginx

