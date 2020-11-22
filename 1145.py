# problem 1145
s = ""
box = []
x, y = map(int , input().split())
if x < y and 1 < x < 20 and  x < y < 100000:
    for i in range(1,y+1):
        s = s + str(i) + " "
        if (i) % x == 0:
            r = s.replace(s , s[0:-1])
            print(r)
            s = ""



