import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
nums = '1234567890'
symbols = '!@#$%^&*.()'

warning = print('ATENÇÃO: Responder as perguntas apenas com "sim" ou "nao" (sem aspas)')
warning1 = input('Clique enter para continuar ;)')

length = False
while length == False:
    warning = print('Favor selecionar um número inteiro para o tamanho da sua senha')
    length = input()
    try:
        nm=int(length)+1
        
    except ValueError:
        print('Valor inválido!')
        length = False
length = int(length)
first_choice = input('Deseja Personalizar sua senha? ')
if first_choice == 'sim':
    lower_choice = input('Deseja letras minúsculas na sua senha? ')
    if lower_choice == 'nao':
        lower = ''
    upper_choice = input('Deseja Letras maiúsculas na sua senha? ')
    if upper_choice == 'nao':
        upper = ''
    nums_choice = input('Deseja números na sua senha? ')
    if nums_choice == 'nao':
        nums = ''
    symbols_choice = input('Deseja Caracteres especiais na sua senha? ')
    if symbols_choice == 'nao':
        symbols = ''
    all = lower + upper + symbols + nums
    password = ''
    for _ in range(length):
        password = ''.join([password, random.choice(all)])

    print('Sua senha é:', password)
    
else:
    all = lower + upper + symbols + nums
    password = ''
    for _ in range(length):
        password = ''.join([password, random.choice(all)])

    print('Sua senha é:', password)
    
    