while true
do
        inotifywait --exclude .swp -e create -e modify -e delete -e move  /etc/nginx/sites-enabled
        nginx -t
        if [ $? -eq 0 ]
        then
                echo "Reloading Nginx Configuration"
                #service nginx reload
		supervisorctl restart nginx
        fi
done
