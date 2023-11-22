#Recebe um valor em dinheiro (12,00) e retorna o número mínimo de cada nota que precisa para chegar nesse valor (1 de 10 reais e 1 de 2 reais)
n=int(input())
notas=[100,50,20,10,5,2,1]
print(n)
for i in range(len(notas)):
    if n//notas[i]!=0:
        print(f'{n//notas[i]} nota(s) de R$ {notas[i]},00')
        n=n%notas[i]
    else:
        print(f'{n//notas[i]} nota(s) de R$ {notas[i]},00')
