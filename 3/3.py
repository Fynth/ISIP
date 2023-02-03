i = 9
j = 4
a = 57*9 + 3.4821*(j+1)
a *= 10000
sum = 0
for i in range(0, 7):
    sum += a%10
    a //= 10
print(sum)