# Question 8
# Level 2

# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world



def cleaned(w):
    result = []
    virgula = True
    while virgula:
            virgula = w.find(",")
            cuvant = w[:virgula]
            result.append(cuvant)
            w = w[virgula+1:]
    result.append(w)
    result = sorted(result)
    return w

def sorting():
    w = "zare,ana,dana,radu"
    return cleaned(w)

print sorting()