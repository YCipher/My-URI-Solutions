# problem 1146
r = []
box = []
s = ""
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(1,n+1):
        s = s + str(i) + " "
        if i % n == 0 :
            p = s.replace(s , s[0:-1])
            box.append(p)
            s = ""
for j in range(len(box)):
    print(box[j])




