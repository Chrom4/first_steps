N = int(input('Quantos números tem a sua média? '))

if N >= 1:
    soma=0
    for x in range(N):
        valor=int(input('Número: '))
        soma=soma+valor
    media=soma/N
    print(media)


    
