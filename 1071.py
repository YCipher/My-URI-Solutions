# problem 1071

a = int(input())
b = int(input())
s = 0
for i in range(b+1,a):

    if i % 2 != 0 :
        s = s + i
print(s)
