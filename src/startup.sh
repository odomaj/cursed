#! /bin/bash

screen -dmS loc
screen -S loc -X screen timeout ${TIMEOUT}s tcpdump -i lo -s 65535 -w ${LOC_PCAP_PATH}

screen -dmS net
screen -S net -X screen timeout ${TIMEOUT}s tcpdump -s 65535 -w ${NET_PCAP_PATH}

sleep 1

screen -dmS sol
screen -S sol -X screen python3 -u /root/solution.py ${SOL_LOG_PATH}

timeout ${TIMEOUT}s stdbuf -o0 -e0 bash -c "python3 -u /root/group6.py >> ${TXT_PATH}"

tail -f /dev/null
