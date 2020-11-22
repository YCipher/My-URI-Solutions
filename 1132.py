# problem 1132

a = int(input())
b = int(input())
s = 0
if a < b:
    for i in range(a, b + 1):
        if i % 13 != 0:
            s = s + i

if a > b:
    for i in range(b, a + 1):
        if i % 13 != 0:
            s = s + i


print(s)
