#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:16:13 2024

@author: ubuntu-23-10-1
"""
#==========Import===========
from telnetlib import Telnet
#==========Import===========
cmd = input('Enter the Command to execute : ')
tn = Telnet('192.168.134.100')
tn.write(b'Ahmed_Bilal\n')
tn.write(b'Ahmed_Bilal\n')
tn.write(b'enable\n')
tn.write(b'Ahmed_Bilal\n')
#tn.write(b'term length 0\n')
tn.write(cmd.encode('ascii') + b'\n')
tn.write(b'exit\n')
print (tn.read_all().decode('ascii'))