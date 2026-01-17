#!/bin/bash

sudo apt update -y
sudo apt upgrade -y

sudo apt install -y python3-scapy wireshark tcpdump

echo "Installation and configuration complete."