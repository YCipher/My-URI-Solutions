# problem 1115

i = 0
box = []
while i > -1:
    x , y = map(int , input().split())
    if x == 0 or y == 0 :
        break
    else:
        if x > 0 and y > 0 :
            box.append("primeiro")
        elif x < 0 and y > 0 :
            box.append("segundo")
        elif x < 0 and y < 0 :
            box.append("terceiro")
        else:
            box.append("quarto")

for j in range(len(box)):
    print(box[j])
