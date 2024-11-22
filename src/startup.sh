#! /bin/bash

screen -dmS cap
screen -S cap -X screen timeout ${TIMEOUT}s tcpdump -s 65535 -w ${PCAP_PATH}

sleep 1

timeout ${TIMEOUT}s stdbuf -o0 -e0 bash -c "python3 -u /root/group6.py >> ${TXT_PATH}"

tail -f /dev/null