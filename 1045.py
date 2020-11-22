# problem 1045

a , b , c = map(float , input().split())
liste = [a , b , c]
liste.sort()
a = liste[2]
b = liste[1]
c = liste[0]
if (a > 0 and b > 0 and c > 0):
    while a >= b + c :
        print("NAO FORMA TRIANGULO")
        break
    while a < b + c :
        if a**2 == b**2 + c**2:
            print("TRIANGULO RETANGULO")
        if a**2 > b**2 + c**2 :
            print("TRIANGULO OBTUSANGULO")
        if  a**2 < b**2 + c**2:
            print("TRIANGULO ACUTANGULO")
        if a == b == c :
            print("TRIANGULO EQUILATERO")
        elif (a == b or b == c or a == c ):
            print("TRIANGULO ISOSCELES")
        break

