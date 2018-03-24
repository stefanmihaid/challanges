# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world


def find_word(inp):
    cuvinte=[]
    start=0
    spatiu = " "
    end = inp.find(spatiu) 
    while end:
        c = inp[start:end]
        cuvinte.append(c)
        start = end
        inp=inp[start+1:]
        end = inp.find(spatiu)
        start = 0
        if end < 0:
            end = len(inp)
    return cuvinte


def aranajre(listacuv):
    listacuv = sorted(listacuv)
    return listacuv

def main():
    cuvinte = raw_input("Provide the list of words with spaces  ")   
    list_of_words = find_word(cuvinte)
    list_of_words = aranajre(list_of_words)
    # return list_of_words
    for cuv in list_of_words:
        print cuv,

main()

