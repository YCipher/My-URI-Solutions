# problem 1153

N = int(input())
if 0< N <13 :
    s = 1
    fact = 1
    for i in range(0,N):
        k = (N-i)
        s = s *k
    print(s)


