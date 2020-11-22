# problem 1131

i = 0
intr = 0
grm = 0
count = 0
d = 0
result = []
while i > -1:
    inter , gremio = map(int , input().split())
    r = int(input())
    count = count + 1
    if r != 1:
        result.append("Novo grenal (1-sim 2-nao)")
        if inter - gremio > 0:
            intr = intr + 1
        elif inter - gremio < 0:
            grm = grm + 1
        else:
            d = d + 1
        break
    if r == 1:
        result.append("Novo grenal (1-sim 2-nao)")
        if inter - gremio > 0:
            intr = intr + 1
        elif inter - gremio < 0:
            grm = grm + 1
        else:
            d = d + 1

result.append('{:d} grenais'.format(count))
result.append('Inter:{:d}'.format(intr))
result.append('Gremio:{:d}'.format(grm))
result.append('Empates:{:d}'.format(d))
if intr > grm:
    result.append("Inter venceu mais")
elif intr < grm:
    result.append("Gremio venceu mais")
else:
    result.append("Nao houve vencedor")

for j in range(len(result)):
    print(result[j])
