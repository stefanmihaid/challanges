def deco(a):
	def wrap():
		print 'inside above func call' 
		a()
		print 'aftr func call'
	return wrap

@deco
def vorbe():
	print "fred"

vorbe()
