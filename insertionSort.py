# insertion sort O(n^2)

def insertion(a):
	for i in range(1, len(a)):
		j = i-1
		while a[j] > A[j+1] and j>=0:
			a[j], a[j+1] = a[j+1], a[j]
			j -=1