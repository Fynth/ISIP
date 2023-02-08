def exist(a, b, c):
	if a + b > c and a + c > b and b + c > a:
		return 1
	else: return 0

def correct(a, b, c):
	if a > 0 and b > 0 and c > 0:
		return 1
	else: return 0

def ravnobed(a, b, c):
	if a == b or a == c or b == c: return 1
	else: return 0

def ravnostor(a, b, c):
	if a == b == c: return 1
	else: return 0

a = int(input("введите сторону А:"))
b = int(input("введите сторону В:"))
c = int(input("введите сторону С:"))
if correct(a, b, c) == 1:
	print("значения верны")
	if exist(a, b, c) == 1:
		print("треугольник существует")
		if ravnobed(a, b, c) == 1:
			if ravnostor(a, b, c) == 1:
				print("треугольник равносторонний")
			else:
				print("треугольник равнобедренный")
			
	else: print("треугольникa с такими значениями не существует")
else: print("некорректные данные")