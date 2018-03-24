'''
Implementation of the mergesort alg.
https://brilliant.org/wiki/sorting-algorithms/ 


n(log n ) --> log n^2 
'''
def merge(a, b):
	mergedlist = []
	a_idx, b_idx = 0,0
	while a_idx<len(a) and b_idx<len(b):
		if a[a_idx] < b[b_idx]:
			mergedlist.append(a[a_idx])
			a_idx +=1
		else:
			mergedlist.append(b[b_idx])
			b_idx +=1
	if a_idx == len(a):
		mergedlist.extend(b[b_idx:])
	else:
		mergedlist.extend(a[a_idx:])
	return mergedlist

def merge_sort(a):
	if len(a)<=1:
		return a
	left = merge_sort(a[:len(a)/2])
	right =	merge_sort(a[len(a)/2:])
	return merge(left,right)

def get_list():
	a = []
	while True:
		answ = raw_input("Done? Y/N        ")
		if answ == "y":
			break
		else:
			a.append(raw_input("enter the values    "))
	
	return merge_sort(a)

print get_list()
