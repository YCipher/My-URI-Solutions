d = int(input())

list_N = [31 , 27 , 19 , 32 , 21 , 11 , 71 , 61]
list_C = ["Belo Horizonte" , "Vitoria" , "Campinas" , "Juiz de Fora" , "Rio de Janeiro" , "Sao Paulo" , "Salvador" , "Brasilia"]

if d in list_N:
    print(list_C[list_N.index(d)])

else:
    print("DDD nao cadastrado")
