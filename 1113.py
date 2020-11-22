# problem 1113

i = 0
result = []
while i > -1:
    a , b = map(int , input().split())
    if a == b:
        break
    else:
        if a > b:
            result.append("Decrescente")
        if a < b:
            result.append("Crescente")

for i in range(len(result)):
    print(result[i])
