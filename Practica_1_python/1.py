#Hallar el valor intermedio de tres numeros
a=int(input())
b=int(input())
c=int(input())
max=a
min=b
if a<b:
	max=b
	min=a
if max<c:
	max=c
if c<min:
	min=c
inter=a+b+c-max+min
print inter