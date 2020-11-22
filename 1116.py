# problem 1116

N = int(input())
box = []
for i in range(N):
    x, y = map(int , input().split())
    if y == 0:
        box.append("divisao impossivel")
    else:
        d = x/y
        box.append(d)

for j in range(len(box)):
    if type(box[j]) == str:
        print('{:s}'.format(box[j]))
    else:
        print('{:.1f}'.format(box[j]))



