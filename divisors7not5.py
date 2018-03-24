# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def divisors(bot, top):
	a = []
	i = bot
	while i < top:
		if i%7==0 and i%5!=0:
			a.append(i)
			a.append("-")
		i +=1
	m = len(a)-1
	return a[:m]
	
		
print divisors(2000, 3200)