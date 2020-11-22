# problem 1143

N = int(input())
if 1 < N < 1000:
    i = 1
    while i < N+1:
        print(i , i**2 , i**3)
        print(i , i**2+1 , i**3+1)
        i = i + 1