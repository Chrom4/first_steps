import math as m
a = 22
b = 3
c = 9

if a < 1:
	x = 0

delta = b**2 - 4*a*c
print(delta)
x1 = (-b+ m.sqrt(delta))/2*a
x2 = (-b- m.sqrt(delta))/2*a

print(x1,x2)