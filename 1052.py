m = int(input())

liste = ["January" ,"February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" ,
  "October" , "November" , "December" , " "]

while  1 <= m <= 12 :
        if m == 12 :
            print("December")
            break

        if m == liste.index(liste[m]) and m != 12  :
                print(liste[m-1])
                break
        break
