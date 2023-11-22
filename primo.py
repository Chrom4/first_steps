def listprimo(x):
	l=[]
	for i in range(x,-1,-1):
		div=0
		for j in range(1,i+1//2):
			if i%j == 0:
				div+=1
			if div > 1:
				break
		if div == 1:
			l.append(i)
	print(l)

def ehprimo(x):
	div=0
	for i in range(1,x+1//2):
		if x%i == 0:
			div+=1
		if div > 1:
			print(False)
			break
	if div == 1:
		print(True)

def primeiroPrimo(x):
	for i in range(x,-1,-1):
		div=0
		for j in range(1,i+1//2):
			if i%j == 0:
				div+=1
			if div > 1:
				break
		if div == 1:
			print(i)
			break

while True:
	x=int(input())
	primeiroPrimo(x)