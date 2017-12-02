#!/bin/bash

echo '#IP адреса <a name="99"></a>' > 99-ip.md
sudo nmap -sN --open 192.168.10.0/24 -p 22 >> 99-ip.md
