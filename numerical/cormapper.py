#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	
	try: 
		x1 = int(values[1])
		x2 = int(values[2])
	except ValueError:
		continue
	print('%s\t%s' % (x1, x2))
