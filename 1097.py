# problem 1097
start = [7, 6, 5]
for i in range(1,6):
    for j in range(3):
        if i == 1 :
            print('I={:d}'.format(1) , 'J={:d}'.format(start[j]))
        else:
            start[j] = start[j]+2
            p = 2*i - 1
            print('I={:d}'.format(p) , 'J={:d}'.format(start[j]))

