#! /bin/bash

screen -dmS cap
screen -S cap -X screen timeout ${TIMEOUT}s tcpdump -s 65535 -w ${PCAP_PATH}

sleep 1

screen -dmS net
screen -S net -X screen timeout ${TIMEOUT}s python3 /root/group6.py > ${TXT_PATH}

tail -f /dev/null
