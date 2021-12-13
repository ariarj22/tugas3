def frekuensi(item):
	mydict = {}
	result = {}
	for i in item:
		if i in mydict:
			mydict[i] += 1
		else:
			mydict[i] = 1
	temp = sorted(mydict, key = mydict.get)
	for i in temp:
		result[i] = mydict[i]

	return result

a = list(input().split())
hasil = frekuensi(a)
for i in hasil:
	print('{}: {}'.format(i, hasil[i]))