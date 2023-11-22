#Recebe uma entrada em dias e retorna quantos anos, meses e dias N corresponde
N=int(input())
print(f'{N//365} ano(s)\n{(400//30)-(400//365)*12} mes(es)\n{400%365-((400//30)-(400//365)*12)*30} dia(s)')
