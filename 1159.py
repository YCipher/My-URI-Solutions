# problem 1159
l = []
while True:
    n = int(input())
    if n == 0 :
        break
    else:
        s = n
        sim = 0
        for j in range(10):
            if s % 2 == 0:
                sim = sim + s
                s = s + 1
            else:
                s = s + 1
        l.append(sim)

for i in range(len(l)):
    print(l[i])
