def ConvertToBin(j):
    char_dec = ord(j)
    to_bin = bin(char_dec)
    return to_bin

def remove_b(a):
    return a[2:]

def add_b(g):
    g.insert(0, "0")
    g.insert(1, "b")
    return g

def convert_to_letter(l):
	concat = ''.join(str(x) for x in l)
	dec_value = int(concat, base=2)
	character = chr(dec_value)
	return character

def encript(message, key):
    encripted = []
    c = 0
    message2 = remove_b(message)
    key2 = remove_b(key)
    while (c < len(message2)):
        encripted.append(int(message2[c], 2) ^ int(key2[c], 2))
        c = c+1
    encripted = add_b(encripted)
    letter = convert_to_letter(encripted)
    return letter

def main():
    c = 0
    print ("This is an OTP example")
    textencript = "mesaj"
    print "The messge  ", textencript
    key = "cheie"
    print "Using key   ", key
    bin_message = []
    bin_key = []
    kripto_text = []
    secret_message = []

    for i in textencript:
        bin_message.append(ConvertToBin(i))
    for j in key:
        bin_key.append(ConvertToBin(j))
    while (c < len(bin_message)):
        secret_message.append(encript(bin_message[c],bin_key[c]))
        c = c+1
    print "The encripted string is:", secret_message
main()