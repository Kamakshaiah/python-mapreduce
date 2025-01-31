#!/usr/bin/env python3

import sys
from functools import reduce 

def sum_prod(x, y):
	return sum([i*j for i, j in zip(x, y)])

def sum_sqrs(l):
	return sum([i**2 for i in l])
def sqrd_sum(l):
	return sum(l)**2
	
def correl(x1, x2):
	n = len(x1)
	out = (n*sum_prod(x1, x2) - (sum(x1)*sum(x2)))/((n*sum_sqrs(x1) - sqrd_sum(x1))*(n*sum_sqrs(x2)-(sqrd_sum(x2))))**0.5
	return out
	
x=[]
y=[]

for line in sys.stdin:
	line = line.strip()
	values = line.split('\t')
	
	try: 
		x.append(int(values[0]))
		y.append(int(values[1]))
	except ValueError:
		continue 

if __name__ == '__main__':
	#deg_ = len(x) - 1
	print(correl(x, y)) 
	
