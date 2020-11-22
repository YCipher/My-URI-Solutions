# problem 1047
iH , iM ,fH, fM = map(int , input().split())

while True :
    if  (iH > 24 or iH < 0 ) and (fH > 24 or fH < 0) and (iM > 59 or iM < 1) and (fM > 59 or fM < 1):
        break
    if  iH == fH and iM == fM :
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(24 , 0))
        break

    if  iH == fH and iM != fM :
        if iM < fM:
            print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( (abs(fH-iH)) , (abs(fM-iM)) ))
        if iM > fM:
            print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(24 - abs(1+abs((fH-iH))) , 60 -(abs(fM-iM))))
        break
#------------------------------------------------------------------------------------
    if (0 < iH < 12) and ( 0 < fH < 12) and iM <= fM:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( (abs(fH-iH)) , (abs(fM-iM)) ))
        break

    if (0 < iH < 12) and ( 0 < fH < 12) and iM >= fM:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( abs(1-abs((fH-iH))) , 60 -(abs(fM-iM)) ))
        break

#------------------------------------------------------------------------------------

    if (12 < iH < 24) and ( 12 < fH < 24) and iM <= fM:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( (abs(abs(24-fH)-abs(24-iH))) , (abs(fM-iM)) ))
        break

    if (12 < iH < 24) and ( 12 < fH < 24) and iM >= fM:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( abs(1-(abs(abs(24-fH)-abs(24-iH)))) , 60 -(abs(fM-iM)) ))
        break

#-------------------------------------------------------------------------------------------

    if (12 < iH < 24) and ( 0 < fH < 12) and iM <= fM :
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( (abs((fH)+abs(24-iH))) , abs(fM - iM) ))
        break

    if (12 < iH < 24) and ( 0 < fH < 12) and iM >= fM :
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( abs(1-(abs((fH)+abs(24-iH)))) , 60 -(abs(fM-iM)) ))
        break

#------------------------------------------------------------------------------------------


    if (0 < iH < 12) and ( 12 < fH < 24) and iM <= fM :
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( (abs(abs(fH-12)+abs(iH-12))) , (abs(fM-iM)) ))
        break

    if (0 < iH < 12) and ( 12 < fH < 24) and iM >= fM :
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %( abs(1-(abs(abs(fH-12)+abs(12 - iH)))) , 60 - (abs(fM-iM)) ))
        break

    break





