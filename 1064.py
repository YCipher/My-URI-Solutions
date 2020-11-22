# problem 1064
box = []*6
s = 0.0
for i in range(6):
    value = float(input())
    if value > 0:
        box.insert(i , value)

print('%d valores positivos'%(len(box)))
for i in range(len(box)):
    s = s + box[i]
print('{:.1f}'.format(s/len(box)))
