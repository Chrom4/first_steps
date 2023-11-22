N=int(input())
print(f'{N//3600}:{(N//60)-(60*(N//3600)) if N//3600!=0 else N//60}:{N%60}')