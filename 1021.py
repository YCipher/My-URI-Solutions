# problem 1021

value = float(input())
if value >= 0.0 and value <= 1000000.00:
    BlackNotes1 = [100.00 , 50.00 , 20.00 , 10.00 , 5.00 , 2.00 ]
    BlackNotes2 = [1.00 , 0.50 , 0.25 , 0.10 , 0.05 , 0.01]
    box = BlackNotes1 + BlackNotes2
    i = 0
    print("NOTAS:")
    while (i < len(BlackNotes1) + len(BlackNotes2)):
        p = value  // box[i]
        B = value % box[i]
        value = B

        if box[i] > 1.00:
            print("%d nota(s) de R$ %.2f" %(int(p) ,box[i]))
            if box[i] <= 2.00:
                print("MOEDAS:")


        if box[i] <= 1.00 and box[i] >= 0.05   :
            print("%d moeda(s) de R$ %.2f" %(int(p)  ,box[i]))
        elif box[i] <= 0.05:
            print("%d moeda(s) de R$ %.2f" %(int(p) +1  ,box[i]))

        i = i + 1
