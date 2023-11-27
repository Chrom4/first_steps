from random import *

def imprimir(l):
	X=8
	print()
	for j in range(len(l)):
		if X>0:
			print(l[j],end=', ')
			X-=1
		else:
			print()
			print(l[j],end=', ')
			X=7
	print('\n')

id_q,itu,idp=[],[],[]

for i in range(120):
	id_q.append(0)
	itu.append(randint(0,99))
	idp.append(randint(0,99))

print('itu:')
imprimir(itu)
print('idp:')
imprimir(idp)

for k in range(120):
	if itu[k]<20 and idp[k]>55:
		id_q[k]=1
	elif itu[k]>0 and idp[k]==0:
		id_q[k]=2

print('id_q:')
imprimir(id_q)