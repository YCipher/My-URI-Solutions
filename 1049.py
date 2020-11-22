animal_I = str(input())
animal_II = str(input())
animal_III = str(input())

if animal_I == "vertebrado" :
    if animal_II == "ave" :
        if animal_III == "carnivoro":
            print("aguia")
        if animal_III == "onivoro":
            print("pomba")
    if animal_II == "mamifero":
        if animal_III == "onivoro":
            print("homem")
        if animal_III == "herbivoro":
            print("vaca")

if animal_I == "invertebrado":
    if animal_II == "inseto":
        if animal_III == "hematofago":
            print("pulga")
        if animal_III == "herbivoro":
            print("lagarta")
    if animal_II == "anelideo":
        if animal_III == "hematofago":
            print("sanguessuga")
        if animal_III == "onivoro":
            print("minhoca")


