def indeks(daftar, target):
	result = []
	for i in range(len(daftar)):
		for j in range(i+1, len(daftar)):
			if daftar[i] + daftar[j] == target:
				result.extend([i, j])
				return result

	return result

a = list(map(int, input().split()))
b = int(input())
hasil = indeks(a, b)
print(hasil)