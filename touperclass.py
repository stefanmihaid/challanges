# Question 5
# Level 1
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class Strings():
	def __init__(self):
		self.cuvant = ""
	def read(self):
		self.cuvant = raw_input("Enter the word:  ")
	def printstring(self):
		print self.cuvant.upper()

a = Strings()
a.read()
a.printstring()


