n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
O = []
L = [n1 , n2 , n3 , n4 , n5 , n6]
i = 0
while i < len(L):
    if L[i] > 0 :
        O.append(L[i])
    i = i + 1


print("%d valores positivos" %(len(O)))

