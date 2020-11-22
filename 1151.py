# problem 1151
l = []
N = int(input())
if 0 < N < 46:
    st = 0
    prev = 1
    k = 0
    l.append(st)
    l.append(prev)
    for i in range(N-2):
        p = st + prev
        k = k + p
        st = prev
        prev = k
        k = 0
        l.append(p)
s = ""
for j in range(len(l)):
    s = s + str(l[j])+" "
r = s.replace(s , s[0:-1])
print(r)



