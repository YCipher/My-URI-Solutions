# problem 1101
from math import fsum
ll = []
def func(liste):
    i = 0
    box = []
    while i > -1:
        b , a = map(int , input().split())
        if a> b:
            box.append(b)
        if a < b:
            box.append(a)
        if a <= 0 or b <= 0:
            break
        else:
            for j in range(abs(a - b)):
                if a < b:
                    a = a + 1
                    box.append(a)
                if a > b:
                    b = b + 1
                    box.append(b)
        print(box)
        liste.extend(box)
        box.clear()
    return liste

l = func(ll)
print(l)













        

