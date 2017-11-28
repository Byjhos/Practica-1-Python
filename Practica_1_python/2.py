#para saber si tres lados formanun triangulo
a=int(input())
b=int(input())
c=int(input())
if a>b:
	max=a
else:
	max=b
if max<c:
	max=c
s=(a+b+c)/2
if s>max:
	print"forman triangulo"
else:
	print"no forman triangulo"