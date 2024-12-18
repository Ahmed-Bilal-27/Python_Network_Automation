#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:17:08 2024

@author: ubuntu-23-10-1
"""
#==========Import===========
import getpass
import telnetlib
#==========Import===========

HOST = "192.168.134.100"
user = input("Enter your Username: ")
print("Enter password:")
password = getpass.getpass()
cmd = input('Enter the Command to execute : ')

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b'Ahmed_Bilal\n')
tn.write(b'Ahmed_Bilal\n')
tn.write(b'enable\n')
tn.write(b'Ahmed_Bilal\n')
tn.write(cmd.encode('ascii') + b'\n')
tn.write(b'exit\n')

print(tn.read_all().decode('ascii'))