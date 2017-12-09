#!/bin/bash
while :
do
	echo "Press [CTRL+C] to stop.."
	./get_ip.sh
	git add --all
	git commit -m "get_ip"
	git push origin master
	sleep 120
done
