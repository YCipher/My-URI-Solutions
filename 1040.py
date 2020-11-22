# problem 1040

N1 , N2 , N3 , N4 = map(float , input().split())
Avrege_3 = (N1*2 + N2*3 + N3*4 + N4) / 10
print("Media: %.1f" %(Avrege_3))
if Avrege_3 <= 6.9 and Avrege_3 >= 5.0:
    print("Aluno em exame.")
    new_socre = float(input())
    print("Nota do exame: %.1f" %(new_socre))
    Avrege_Final = (new_socre + Avrege_3) / 2
    if Avrege_Final >=5:
        print("Aluno aprovado.")
    elif Avrege_Final <= 4.9 :
        print("Aluno reprovado.")
    print("Media final: %.1f" %(Avrege_Final))



if Avrege_3 >= 7.0 :
    print("Aluno aprovado.")
elif Avrege_3 < 5.0 :
    print("Aluno reprovado.")



