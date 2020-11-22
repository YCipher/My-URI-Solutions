# problem 1160
s = 0
T = int(input())
if 1 <= T <= 3000:
    for i in range(T):
        pa, pb, g1 ,g2 = map(float, input().split())
        pa, pb = int(pa), int(pb)
        if (pa < pb) and (g2 < g1) and (100 <= pa <= 10**6) and (100 <= pb <= 10**6) and (0.1<=g1<=10.0) and (0.1<=g2<=10.0):
            a = pa
            b = pb
            s = 0
            for j in range((a+b)):
                pa = int(pa *(g1/100))
                pb = int(pb *(g2/100))
                s = pb-pa
                if s == 0:
                    print(pb)
                    break






















