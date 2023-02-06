import random
i = 9
j = 4
s = 100 * i + j
random.seed(s)
seq = tuple(random.random() for _ in range(100))
max = seq[0]
min = seq[0]
sum = 0
k = []
print("список:", seq)
e = 0
while e < len(seq):
	if max < seq[e]: max = seq[e]
	e += 1
print("максимальный элемент массива:", max)
e = 0
while e < len(seq):
	if min > seq[e]: min = seq[e]
	e += 1
print("минимальный элемент массива:", min)
e = 0
while e < len(seq):
	if seq[e] > 0.5: sum += seq[e]
	e += 1
print("сумма условных элементов:", sum)
e = 0
while e < len(seq):
	if seq[e] < 0.5: k.append(seq[e])
	e += 1
k = k[:-1]
e = 0
print("список с условными элементами:", k)
t = 0
while e < len(seq):
	if 0.3 < seq[e] <0.7: t += 1
	e += 1
print("количество условных элементов начального массива:", t)
e = 0
while e < len(seq):
	if seq[e] > 0.9:
		print("номер первого элемента условия:", e+1)
		break
	e += 1