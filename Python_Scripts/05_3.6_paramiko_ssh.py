#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:11:10 2024

@author: ubuntu-23-10-1
"""

#==========Import===========
import paramiko
import time
#==========Import===========
ip = '192.168.134.100'
username = 'Ahmed_Bilal'
password = 'Ahmed_Bilal'

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
#DEVICE_ACCESS.send(b'term length 0\n')
DEVICE_ACCESS.send(b'enable\n')
DEVICE_ACCESS.send(b'Ahmed_Bilal\n')
DEVICE_ACCESS.send(b'show ip int br\n')
time.sleep(5)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))
SESSION.close()