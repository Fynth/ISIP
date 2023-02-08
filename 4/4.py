i = 9
j = 4
a = 10**9+i*10**8+j+10**6-(i+j)*10**4+2*j+i
print (a)
arrel = []
while (a > 0):
    arrel.insert(0, int(a%10))
    a //= 10
print (arrel)