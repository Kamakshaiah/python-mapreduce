#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	try:
		gender = values[0]
		salary = values[1]
	except ValueError: 
		continue 
	print(gender, salary) 
