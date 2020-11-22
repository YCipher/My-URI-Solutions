# problem 1095

L = 60
s = 1
print('I={:d}'.format(s) , 'J={:d}'.format(L))
for i in range(0 , int(L) , 5):
    i = i + 5
    j = L - i
    s = s + 3
    print('I={:d}'.format(s), 'J={:d}'.format(j))


