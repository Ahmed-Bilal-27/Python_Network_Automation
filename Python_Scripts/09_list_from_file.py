#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:38:45 2024

@author: ubuntu-23-10-1
"""
#==========Import===========
import paramiko
import time
from getpass import getpass
#==========Import===========
username = 'Ahmed_Bilal'
password = 'Ahmed_Bilal'

DEVICE_LIST = open ('09_Devices.txt')
for RTR in DEVICE_LIST:
    RTR = RTR.strip()
    print ('\n #### Connecting to the device ' + RTR + '####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(RTR,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    COMMANDS = open ('09_config')
    for LINES in COMMANDS:
        time.sleep(.5)
        DEVICE_ACCESS.send(LINES)

    time.sleep(1)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))
    SESSION.close()