# problem 1067

X = int(input())
if 1 <= X <= 1000:
    for i in range(X+1,X+1+12):
        if i % 2 != 0 :
            print(i)
