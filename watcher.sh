while true
do
        inotifywait --exclude .swp -e create -e modify -e delete -e move  /etc/nginx/sites-enabled
	NOW=$(date +"%Y-%m-%d %H:%M")
 
	echo '$NOW : Reloading Nginx Config'
        nginx -t
        if [ $? -eq 0 ]
        then
                echo "Reloading Nginx Configuration"
                #service nginx reload
		supervisorctl restart all
        fi
done
