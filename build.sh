#!/bin/bash
sudo docker build -t nginx .

sudo docker run -d -it --name nginx-www -p 80:80 -v /home/ocom/apps/nginx/sites-available:/etc/nginx/sites-enabled -v  /home/ocom/apps/nginx/logs:/var/log/nginx nginx

