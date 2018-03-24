# implementation of mergesort

def sort(left, right):
	final = []
	l_idx, r_idx = 0,0
	while l_idx<len(left) and r_idx<len(right):
		if left[l_idx] < right[r_idx]:
			final.append(left[l_idx])
			l_idx +=1
		else:
			final.append(right[r_idx])
			r_idx +=1
	if l_idx == len(left):
		final.extend(right[r_idx:])
	else:
		final.extend(left[l_idx])
	return final

def split(a):
	if len(a) <= 1:
		return a
	left = split(a[:len(a)/2])
	right =  split(a[len(a)/2:])
	return sort(left, right)

a = "1921384156651656169841165468124464534657465"
print split(a)