import random
i = 9
j = 4
s = 100 * i + j
random.seed(s)
seqs = [[random.random() for _ in range(random.randint(1, 100))] for _ in range(20)]
for seq in seqs:
	if len(seq) % 10 == 1:
		print("в массиве", len(seq), "элемент")
	elif len(seq) % 10 == 2: print("в массиве", len(seq), "элемента")
	else: print("в массиве", len(seq), "элементов")