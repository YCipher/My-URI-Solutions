# problem 1114

i = 0
box = []
while i > -1:
    password = 2002
    enter = int(input())
    if enter == password:
        box.append("Acesso Permitido")
        break
    else:
        box.append("Senha Invalida")

for i in range(len(box)):
    print(box[i])
    