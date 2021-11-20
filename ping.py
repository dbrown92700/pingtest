#!python3

from os import popen
from time import sleep
from datetime import datetime

file = open('pingtest.txt', 'w')
while True:
	text = popen('ping -c 5 8.8.8.8').read().split('\n')
	
	time = datetime.now()
	result = f'{time.month:02}/{time.day:02} {time.hour:02}:{time.minute:02} -'
	for line in text:
		if line.find('packet') > 0:
			result += ' ' + line
		if line.find('trip') > 0:
			result += ' ' + line	
	print(result)
	file.write(result + '\n')
	sleep(600)