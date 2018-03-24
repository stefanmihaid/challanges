# Question:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

import re

def separate(stri):
    words = []
    start = 0
    end = stri.find(",")
    while end:
        cuvant = stri[start:end]
        words.append(cuvant)
        stri = stri[end+1:]
        end = stri.find(",")
        if end < 0:
            end = len(stri)
    return words

def conditie(w):
    if re.search("[a-z]", w) and re.search("[0-9]",w) and re.search("[$#@]",w):
        return True
    else:
        return False

def main():
    passwd = raw_input("Provide PWD:   ")
    pwd = separate(passwd)
    err = "No passwd met the crytheria   "
    for j in pwd:
        if len(j) > 6 and len(j) <12 and conditie(j):
            return j
        else:
            return err

print main()