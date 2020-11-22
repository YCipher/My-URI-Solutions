
y , z, n =  0.0 , 0.0 , 0.0
gama = []

while True:
    x = float(input())
    if n == 1:
        if x == 2:
            break
        elif x == 1:
            n = 0
            continue
        else:
            gama.append("novo calculo (1-sim 2-nao)")
            continue
    else:
        if x < 0 or x > 10:
            gama.append("nota invalida")
        elif z == 0:
            y = x
            z = 1
        else:
            gama.append('media = {:.2f}'.format((x+y)/2))
            z = 0
            n = 1
    if n == 1:
         gama.append("novo calculo (1-sim 2-nao)")


for i in range(len(gama)):
        print(gama[i])


