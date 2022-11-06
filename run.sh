#!/bin/sh


cd Desktop/BotJob-0.1
#source ~/home/mauri/miniconda3/bin/python
#conda activate base
while true
do
    
    python3 find2.py
    python3 apply.py
    python3 time.py

done
