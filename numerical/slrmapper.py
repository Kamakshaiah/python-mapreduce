#!/usr/bin/env python3

import sys

x = []
y = []

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	try: 
		x = values[1]
		y = values[2]
		
	except ValueError:
		continue
		
	print('%s\t%s' % (x, y))
