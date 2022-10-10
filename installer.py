#!/usr/bin/python3

import os

os.system('chmod -R 777 Sapage.py')
path = os.getcwd()
os.chdir('/usr/local/sbin')
sf = open('Sapage','w')
sf.write('#!/bin/bash')
sf.write('\ncd '+path+' && ./Sapage.py')
os.system('chmod -R 777 Sapage')
print('\nInstalation completed')
print('\nType Sapage.py from anywhere to run...')