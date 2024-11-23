# CS455 Group 6 Final Project

Repo to run solution.py and group6.py simultaneously and capture the network traffic

## Requirements

- python3
- docker

## Instructions

- run main.py
- cap.pcap, text.txt, and sol_log.txt will be outputted to root directory of the repo

## Action 1

- sends Group 6 to host tcpbin.com

## Action 2

- posts the current time to http://httpbin.org/post

## Action 3

- fetches http://example.com

## Action 4

- sends the response of Action 3 to host tcpbin.com

## Action 5

- connects to host 127.0.0.1 on port 42001
- sends "Try sending me text and see what happens..."
- receives a message
- alters the message and sends it back

## Action 6

- establishes host 0.0.0.0 on port 1234
- when a client connects sends "Try sending me some text and see what happens..."
- when the client sends a host, respond with the result of an http request to the host that was sent
