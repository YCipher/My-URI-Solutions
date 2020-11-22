# problem 1117
from math import fsum
i = 0
box = []
result = []
while i > -1:
    a = float(input())
    if a < 0 or a > 10:
        box.append("nota invalida")
    if a >=0 and a <= 10:
        result.append(a)
        if len(result) == 2:
            break
c = box + result
average = (fsum(result) / 2)
for j in range(len(box)):
    print(box[j])
print('media = {:.2f}'.format(average))






