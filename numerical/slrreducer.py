#!/usr/bin/env python3

import sys

def mean(x):
	return(sum(x)/len(x))

def var(x):
	n = len(x)
	out = sum([(i - mean(x))**2 for i in x])
	out_ = out/n
	return out_

def std(x):
	return var(x)**0.5

def sum_prod(x, y):
	return sum([i*j for i, j in zip(x, y)])
def sum_sqrs(x):
	return sum([i**2 for i in x])
def sum_sqred(x):
	return sum(x)**2

def correl(x, y):
	n = len(x)
	out = (n*sum_prod(x, y) - (sum(x)*sum(y)))/((n*sum_sqrs(x) - sum_sqred(x))*(n*sum_sqrs(y) - sum_sqred(y)))**0.5
	return out

def slope(x, y):
	out = correl(x, y) * (std(y)/std(x))
	return out
	
def constant(x, y):
	out = (mean(y) - (slope(x, y)*mean(x)))
	return out	 
x = []
y = []
for line in sys.stdin:
	line = line.strip()
	values = line.split('\t')
	
	try:
		x.append(int(values[0]))
		y.append(int(values[1]))
	except ValueError:
		continue
		
if __name__ == '__main__':
	print(constant(x, y), slope(x, y))
