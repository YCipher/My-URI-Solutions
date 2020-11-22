# problem 1065

box = []*5
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        box.insert(i , num)
print('{:d} valores pares'.format(len(box)))
