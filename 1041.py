# 1041 coordinate of point

x , y  = map(float , (input().split()))
if x  > 0.0 :
    if y > 0.0:
        print("Q1")
    if y < 0.0:
        print("Q4")
if x < 0.0 :
    if y > 0.0 :
        print("Q2")
    if y < 0.0:
        print("Q3")
if x == 0.0 and y !=0.0:
    print("Eixo Y")
if x != 0.0 and y == 0.0:
    print("Eixo X")

if x == 0.0 and y == 0.0:
    print("Origem")
