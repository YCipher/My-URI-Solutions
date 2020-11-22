# Triangle 1043
a , b , c  = map(float , (input().split()))

if ( b-c < a and a < b+c) and ( a-c < b and  b < a+c ) and ( a-b < c and c < a+b):
    print("Perimetro = %.1f" %(a + b + c))

else :
    print("Area = %.1f" %(((a+b)*c )/ 2))
