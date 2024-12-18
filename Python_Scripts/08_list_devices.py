#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:35:06 2024

@author: ubuntu-23-10-1
"""
#==========Import===========
import paramiko
import time
#==========Import===========
username = 'Ahmed_Bilal'
password = 'Ahmed_Bilal'

DEVICE_LIST =['192.168.134.100', '10.0.0.1']
for RTR in DEVICE_LIST:
    print ('\n #### Connecting to the device ' + RTR + '####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(RTR,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send(b'enable\n')
    DEVICE_ACCESS.send(f'{password}\n'.encode())
    DEVICE_ACCESS.send(b'config t\n')
    for N in range (2,5):
        DEVICE_ACCESS.send('int lo ' +str(N) + '\n')
        DEVICE_ACCESS.send('ip address 1.1.1.' +str(N) + ' 255.255.255.255\n')  

    time.sleep(3)
    DEVICE_ACCESS.send(b'do term length 0\n')
    DEVICE_ACCESS.send(b'do show ip int brief\n')
    time.sleep(3)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))

    SESSION.close()