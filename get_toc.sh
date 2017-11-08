#!/bin/bash

cat 00*.md > 1.txt
cat 10*.md >> 1.txt
cat 20*.md >> 1.txt
cat 30*.md >> 1.txt
cat 40*.md >> 1.txt
cat 50*.md >> 1.txt
cat 60*.md >> 1.txt
cat 70*.md >> 1.txt
cat appendix.md >> 1.txt
cat 1.txt | grep \^\#  > toc.txt
sed -i 's/# /#/g' toc.txt
sed -i 's/####/\t\t\t- [/g' toc.txt
sed -i 's/###/\t\t- [/g' toc.txt
sed -i 's/##/\t- [/g' toc.txt
sed -i 's/#/- [/g' toc.txt
sed -i 's/ <a name="/](#/g' toc.txt
sed -i 's/<a name="/](#/g' toc.txt
sed -i 's/"><\/a>/)/g' toc.txt
