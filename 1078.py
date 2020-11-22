# problem 1078

N = int(input())
if 1< N < 1000:
    for i in range(1,11):
        print("%d x %d = %d" %(i,N, i*N))
