#problem 1044

A  , B = map(int , input().split())
A = int(A)
B = int(B)
if B % A == 0 or A % B == 0 :
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
