# problem 1094
from math import fsum
N = int(input())
sum = 0
C = []
R = []
S = []
for i in range(N):
    n , t  =   input().split()
    n = int(n)
    t = str(t)
    sum = sum + n
    if t == 'C':
        C.append(n)
    elif t == 'S':
        S.append(n)
    else:
        R.append(n)


print('Total: {:d} cobaias'.format(sum))

print('Total de coelhos: {:d}'.format(int(fsum(C))))
print('Total de ratos: {:d}'.format(int(fsum(R))))
print('Total de sapos: {:d}'.format(int(fsum(S))))


print('Percentual de coelhos: {:.2f} %'.format((fsum(C) / sum)*100))
print('Percentual de ratos: {:.2f} %'.format((fsum(R)/ sum)*100))
print('Percentual de sapos: {:.2f} %'.format((fsum(S) / sum)*100))





