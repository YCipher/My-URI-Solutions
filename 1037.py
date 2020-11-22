#problem 1037

float_number = float(input())
if float_number >= 0.0 and float_number <=25.0 :
    print("Intervalo [0,25]")
elif float_number > 25.0 and float_number <= 50.0:
    print("Intervalo (25,50]")
elif float_number > 50.0 and float_number <= 75.0:
    print("Intervalo (50,75]")
elif float_number > 75.0 and float_number <=100.0:
    print("Intervalo (75,100]")
elif float_number < 0.0 or float_number > 100:
    print("Fora de intervalo")

