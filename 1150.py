# problem 1150
box = []
result = []
x = int(input())
while True:
    z = int(input())
    if z > x:
        box.append(z)
        break
    else:
        continue
Z = box[0]
m = 0
for i in range(Z):
    m = m + x
    if m > Z:
        result.append(m)
        break
    else:
        result.append(m)
        x = x + 1
        continue
print(len(result))
