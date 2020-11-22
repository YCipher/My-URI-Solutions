# problem 1154
from math import fsum
l = []
while True:
    n = int(input())
    if n < 0 :
        break
    else:
        l.append(n)
print('{:.2f}'.format(fsum(l)/len(l)))

