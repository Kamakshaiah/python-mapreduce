#!/usr/bin/env python3

import sys
gender = []
for line in sys.stdin:
	line = line.strip()
	gender, sal = line.split(',')
	print('%s\t%s' % (gender, sal))
