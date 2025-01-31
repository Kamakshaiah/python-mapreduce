#!/usr/bin/env python3

import sys

male_total = 0
female_total = 0
cnt_m = 0
cnt_f = 0

for line in sys.stdin:
	line = line.strip()
	gender, sal = line.split('\t')
	try:
		if gender == 'male':
			male_total += int(sal)
			cnt_m += 1
		else:
			female_total += int(sal)
			cnt_f += 1
	except Error:
		continue
print(male_total/cnt_m, female_total/cnt_f)
