# problem 1158
l = []
N = int(input())
for i in range(N):
    a , b = map(int, input().split())
    s = a
    sume = 0
    for j in range(2*b):
        if s % 2 != 0:
            sume = sume + s
            s = s + 1
        else:
            s = s + 1
    l.append(sume)

for p in range(len(l)):
    print(l[p])



