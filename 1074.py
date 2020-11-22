# problem 1074

N = int(input())
box = []*N
if N < 10000:
    for i in range(N):
        X = int(input())
        if -10**7<X<10**7 :
            if X == 0 :
                box.insert(i,"NULL")
            if X % 2 == 0 and X > 0:
                box.insert(i,"EVEN POSITIVE")
            if X % 2 == 0 and X < 0:\
                box.insert(i,"EVEN NEGATIVE")
            if X % 2 != 0 and X > 0:
                box.insert(i,"ODD POSITIVE")
            if X % 2 != 0 and X < 0:
                box.insert(i,"ODD NEGATIVE")
for i in range(len(box)):
    print(box[i])




