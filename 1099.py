# problem 1099
from math import fsum
N = int(input())
box = []*N
boxOdd = []

for i in range(N):
    num1 , num2  = map(int , input().split())
    boxOdd = []
    for j in range(abs(num2-num1)-1):
        if num2 > num1 and num1 != num2 :
            num1 = num1 + 1
            if num1 % 2 != 0 :
                boxOdd.append(num1)
        if num1 > num2 and num1 != num2:
            num2 = num2 + 1
            if num2 % 2 != 0:
                boxOdd.append(num2)
    box.insert(i , int(fsum(boxOdd)))
for p in range(len(box)):
    print(box[p])
