# problem 1066
z, f, p, n = 0, 0, 0, 0
for i in range(5):
    number = int(input())
    if number % 2 == 0:
        z = z + 1
    if number % 2 != 0:
        f = f + 1
    if number > 0:
        p = p + 1
    if number < 0:
        n = n + 1
print('%d valor(es) par(es)' %(z))
print('%d valor(es) impar(es)' %(f))
print('%d valor(es) positivo(s)' %(p))
print('%d valor(es) negativo(s)' %(n))