'''
Verify 2 strings are anagrams

'''

def remove_spaces(w):
	w = w.replace(' ', '')
	return w



def sort_letters(w1, w2):
	anag = False
	for l in w1:
		for l2 in w2:
			if l == l2:
				anag = True
	return anag


def anagram(w1, w2):
	# print ("The first word is  " + w1)
	# print ("The seccond word is  " + w2)
	w1 = remove_spaces(w1)
	w2 = remove_spaces(w2)
	if len(w1) is not len(w2):
		return "It is not an anagram"
	else:
		return sort_letters(w1, w2)


print anagram('ana', 'maria')
print anagram('ana', 'ana')
print anagram('listen', 'silent')
print anagram('lis ten', 'sil ent')