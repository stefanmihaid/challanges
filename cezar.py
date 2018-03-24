def main():
	in_litere = []
	mesaj = "cifru"
	print "Mesajul este", mesaj
	rot = 13
	print "Cifrul Cezar are rotire de: ", rot 
	rotit = rotire(mesaj, rot)
	for k in rotit:
		in_litere.append(k)
	for m in in_litere:
		print chr(m)

def rotire(me, ro):
	mesaj_criptat = []
	for i in me:
		mesaj_criptat.append(ord(i)+ro)
	return mesaj_criptat
main()
