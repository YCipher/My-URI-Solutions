# problem 1134
alcool = 0
gazolin = 0
diesel = 0
while True:
    a = int(input())
    if a > 0:
        if a == 4:
            break
        if a == 1:
            alcool = alcool + 1
        elif a == 2:
            gazolin = gazolin + 1
        elif a == 3:
            diesel = diesel + 1
        else:
            continue
print("MUITO OBRIGADO")
print('Alcool: {:d}'.format(alcool))
print('Gasolina: {:d}'.format(gazolin))
print('Diesel: {:d}'.format(diesel))