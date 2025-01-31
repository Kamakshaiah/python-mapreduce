#!/usr/bin/env python3

import sys

def mean(t, c):
	return(t/c)
	
def var(m, l):
	return(sum([(i - m)**2 for i in l]))
	
def std(vr):
	return(vr**0.5)

m_t = 0
c_m = 0
m_l = []

f_t = 0
c_f = 0
f_l = []

for line in sys.stdin:
	line = line.strip()
	gender, sal = line.split()
	
	try: 
		if gender == 'male':
			m_t += int(sal)
			c_m += 1
			m_l.append(int(sal))
		else: 
			f_t += int(sal)
			c_f += 1
			f_l.append(int(sal))
	except ValueError: 
		continue 
		
if __name__ == '__main__':
	m_m = mean(m_t, c_m)
	m_f = mean(f_t, c_f)
	v_m = var(m_m, m_l)
	v_f = var(m_f, f_l)
	s_m = std(v_m)
	s_f = std(v_f) 
	print(m_m, m_f)
	print(v_m, v_f)
	print(s_m, s_f) 
