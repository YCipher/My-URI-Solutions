# problem 1046

start , end = map(int , input().split())
while True:
    if end > 24 or start > 24 :
        break
    if (end == start) :
        print("O JOGO DUROU %d HORA(S)" %(24))
        break
    if  (0 <= end <= 12) and (0 <= start <= 12) :
        print("O JOGO DUROU %d HORA(S)" %(abs(end - start)))
        break

    if (12 <= end <= 24) and (12 <= start <= 24)  :
        print("O JOGO DUROU %d HORA(S)" %(abs((24-end) - (24 - start))))
        break

    if  (0 <= end < 12) and  (12 <= start <= 24) :
        print("O JOGO DUROU %d HORA(S)" %((end + (24 - start))))
        break

    if  (0 <= start <= 12) and  (12 <= end <= 24) :
        print("O JOGO DUROU %d HORA(S)" %((end - 12) + (12-start)))
        break

    break


