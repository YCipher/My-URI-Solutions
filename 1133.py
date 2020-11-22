# problem 1133

a = int(input())
b = int(input())
if (a and b) > 0:
    if a < b:
        for i in range(a+1 ,b):
            if i % 5 == 2 or i % 5 == 3:
                print(i)
    if a > b:
        for i in range(b+1 ,a):
            if i % 5 == 2 or i % 5 == 3:
                print(i)

