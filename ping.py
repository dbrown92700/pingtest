#!/bin/python3

from os import popen
from time import sleep
from datetime import datetime
import re

target = '8.8.8.8'
repeat = 5
sleeptime = 120

while True:
	text = popen(f'ping -c {repeat} {target}').read().split('\n')
	
	time = datetime.now()
	result = f'{time.month:02}/{time.day:02} {time.hour:02}:{time.minute:02} -'
	for line in text:
		if line.find('packet') > 0:
			line = line.lstrip('')
			linearr = re.sub('[a-zA-Z -]', '', line).split(',')
			for stat in linearr:
				result += f'{stat:>10},'
		if (line.find('avg') > 0):
			linearr = re.sub('[a-zA-Z -]', '', line).lstrip('/').lstrip('=').split('/')[0:3]
			for stat in linearr:
				result += f'{stat:>10},'			
	print(result)
	with open('pingtest.txt', 'a') as file:
		file.write(result + '\n')
	sleep(sleeptime)