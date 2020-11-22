# problem 1098
start = [1, 2, 3]
for i in range(0,11):
    for j in range(3):
        if i == 0:
            print('I={:d}'.format(i) , 'J={:d}'.format(start[j]))
        else:
            start[j] = start[j] + 0.2
            p = i*0.2
            if p == 1 or p == 2:
                print('I={:d}'.format(int(p)) , 'J={:.0f}'.format(start[j]))
            else:
                print('I={:.1f}'.format(p) , 'J={:.1f}'.format(start[j]))





