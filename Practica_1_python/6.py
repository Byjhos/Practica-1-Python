#otro programa para halla el maximo comun divisor
a=int(input())
b=int(input())
while residuo(a,b)!=0:
	r=residuo(a,b)
	a=b
	b=r
print b