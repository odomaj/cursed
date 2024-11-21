FROM ubuntu:24.10

RUN apt-get update
RUN apt-get install -y python3 pip
RUN python3 -m pip install requests --break-system-packages
ADD src/* /root/
