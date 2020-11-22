# problem 1072

N = int(input())
m = 0
inin = []*N
out = []*N
if N < 10000:
    for i in range(N):
        X = int(input())
        if -10**7< X < 10**7:
            if (10 <=X <= 20):
                m = m + 1
                inin.insert(i , m)
            else:
                m = m +1
                out.insert(i,m)
print('%d in' %(len(inin)))
print('%d out' %(len(out)))

