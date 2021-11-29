#!python3

from os import popen
from time import sleep
from datetime import datetime

target = '8.8.8.8'
repeat = 5
sleeptime = 120

while True:
	text = popen(f'ping -c {repeat} {target}').read().split('\n')
	
	time = datetime.now()
	result = f'{time.month:02}/{time.day:02} {time.hour:02}:{time.minute:02} -'
	for line in text:
		if line.find('packet') > 0:
			result += ' ' + line
		if line.find('trip') > 0:
			result += ' ' + line	
	print(result)
	with open('pingtest.txt', 'a') as file:
		file.write(result + '\n')
	sleep(sleeptime)