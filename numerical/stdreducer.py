#!/usr/bin/env python3

import sys

def mean(t, c):
	return(t/c)
def var(l, m):
	return(sum([(i -m)**2 for i in l])/len(l))
def std(vr):
	return(vr**0.5)
	
m_t = 0
f_t = 0
m_c = []
f_c = []
c_f = 0
c_m = 0

for line in sys.stdin:
	line = line.strip()
	gender, sal = line.split()
	
	try: 
		if gender == 'male':
			m_t += int(sal)
			m_c.append(m_t)
			c_m += 1
		else: 
			f_t += int(sal)
			f_c.append(f_t)
			c_f += 1
	except ValueError: 
		continue 
				
if __name__ == '__main__':
	m_mean = mean(m_t, c_m)
	f_mean = mean(f_t, c_f)
	m_var = var(m_c, m_mean)
	f_var = var(f_c, f_mean) 
	print(std(m_var), std(f_var))
