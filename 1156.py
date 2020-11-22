# problem 1156

s = 1
for i in range(2,10000):
    j = 2*i - 1
    s = s + (j/2**(i-1))
print('{:.2f}'.format(s))
