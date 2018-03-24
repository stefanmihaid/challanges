
'''
Find out the divisors of a number
'''

def divisor(n):
	a = []
	v = 1
	while v <= n:
		if n%v == 0:
			a.append(v)

		v += 1
	return a

print divisor(91)
