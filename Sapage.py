#!/usr/bin/python3

from termcolor import cprint, colored
import time
import sys

helpp = '''\n\t\t\t/ ___\/  _ \/  __\/  _ \/  __//  __/
\t\t\t|    \| / \||  \/|| / \|| |  _|  \ 
\t\t\t\___ || |-|||  __/| |-||| |_//|  /_
\t\t\t\____/\_/ \|\_/   \_/ \|\____\\_____\\
\n
'''
cprint(helpp,'blue')

text1 = colored('Base File : ', 'yellow')
text2 = colored('Out  File ', 'yellow')
text3 = colored('Verbose [y/N] : ', 'yellow')

base_file = input(text1)
out_file  = input(text2)
verbose   = input(text3)
print('\n')

try:
	with open(base_file,'r') as base_file:
		words = base_file.readlines()
except Exception as e:
	text = '\n'+str(e)+'\n'
	cprint(text,'red')
	sys.exit()

st_time = time.time()

wc = 0

if verbose.lower() == 'y':
	with open(out_file,'a') as nftw:
		for word in words:
			for word2 in words:
				nftw.write(word.strip()+word2.strip()+'\n')
				print(word.strip()+word2.strip())
				wc += 1
else:
	with open(out_file,'a') as nftw:
		for word in words:
			for word2 in words:
				nftw.write(word.strip()+word2.strip()+'\n')
				wc += 1

print('\nWords count '+str(wc))
print('\nTotal time '+str(time.time()-st_time))