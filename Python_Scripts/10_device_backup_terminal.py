#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:42:26 2024

@author: ubuntu-23-10-1
"""
#==========Import===========
import paramiko
import time
from getpass import getpass
import datetime
#==========Import===========
TNOW = datetime.datetime.now().replace(microsecond=0)

username = 'Ahmed_Bilal'
password = 'Ahmed_Bilal'

DEVICE_LIST = open ('09_Devices.txt')
for RTR in DEVICE_LIST:
    RTR = RTR.strip()
    print ('\n #### Connecting to the device ' + RTR + ' ####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(RTR,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send(b'terminal len 0\n')
    DEVICE_ACCESS.send(b'enable\n')
    DEVICE_ACCESS.send(f'{password}\n'.encode())
    DEVICE_ACCESS.send(b'show run\n')

    time.sleep(5)
    output = DEVICE_ACCESS.recv(65000)
    SAVE_FILE = open('ROUTER_' + RTR + str(TNOW), 'w')
    SAVE_FILE.write(output.decode('ascii'))
    SAVE_FILE.close()

    SESSION.close()