import random
def sort(a, comp):
	for n in range(0, len(a)):
		for i in range(0, len(a) - 1):
			if comp(a[i], a[i+1]):
				a[i+1], a[i] = a[i], a[i+1]
def comp(x, y):
	return x < y
i = 9
j = 4
s = 100 * i + j
random.seed(s)
seq10 = [random.random() for _ in range(10)]
seq100 = [random.random() for _ in range(1000)]
seq1000 = [random.random() for _ in range(1000)]
print("массив до:", seq10)
print("")
sort(seq10, comp)
seq10 = seq10[::-1]
print("массив после:", seq10)