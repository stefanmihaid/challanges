# Question 19
# Level 3

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, 
# age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
from operator import itemgetter

def createtup():
    name = raw_input("Please enter the name of the player:  ")
    age = raw_input("Please enter the age:  ")
    points = raw_input("Please enter the points ")
    a = (name,age,points)
    return a
    
def arrange(listajucatori):
	sortat = sorted(listajucatori, key=itemgetter(0,1,2))
	return sortat

def fill():
	tuples = []
	while True:
		answ = raw_input("Are you done yet? Y/N   ")
		if answ == 'y':
			break
		else:
			tuples.append(createtup())
	answ = arrange(tuples)
	return answ


print fill()



