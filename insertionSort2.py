def insertionSort(a):
    for j in range(1, len(a)):  
        key = a[j]
        i = j - 1
        while (i > -1 and a[i] > key): 
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
       

    return a

a = [6, 5, 3, 1, 8, 7, 2, 4] 
print insertionSort(a)


def inso(a):
	i, j = 0, 1
	rez = []
	while i < len(a):
		while j < len(a):
			if a[j] < a[i]:
				
			j +=1
		i +=1
	return rez

b = [6, 5, 3, 1, 8, 7, 2, 4] 
print inso(b)