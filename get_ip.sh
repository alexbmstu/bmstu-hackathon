#!/bin/bash

echo "# 7. IP адреса" > 99-ip.md
sudo nmap -sN 192.168.10.0/24 -p 22 >> 99-ip.md
