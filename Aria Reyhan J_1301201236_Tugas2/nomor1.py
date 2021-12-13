def sekali(angka):
	myset = set()
	dup = set()
	n = len(myset)
	for i in angka:
		myset.add(i)
		if n == len(myset):
			dup.add(i)
		n = len(myset)

	return [int(i) for i in myset - dup]

a = sekali(input())
print(a)