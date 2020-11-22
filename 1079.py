# problem 1079

N = int(input())
box = []*3
for i in range(N):
    num1 , num2 , num3 = map(float , input().split())
    s = ((num1*2)+(num2*3)+(num3*5)) /10
    box.insert(i,'{:.1f}'.format(s))

for i in range(len(box)):
    print(box[i])

