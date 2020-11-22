# problem 1080
# highest position
box = []*100
y = 0
m= 0
for i in range(4):
    box.append(int(input()))
m = (max(box))
y = (box.index(m))
print(m)
print(y+1)


