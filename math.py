# Question 6
# Level 2

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30. 10*d/3**2
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24


def calculate(k):
	a = (10*k/3)**2
	return a

def math():
	v = ""
	b = []
	a = raw_input("Enter the values: ")
	for e in a:
		if e != ",":
		 	e = calculate(int(e))
	 		b.append(str(e))
	for j in b:
		v += j + ","
	return v[:len(v)-1]

print math()