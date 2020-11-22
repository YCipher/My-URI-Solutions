# problem 3101

N , K = map(int , input().split())
while 1<= N <= 100000 and 1 <= K <= 100000 :
    box = []
    for i in range(N):
        box.append(int(input())) # enter elements of Your list with size N
        if -100 <= box[i] <= 100 :
            continue
        else:
            break

    for i in range(K):
        letter = str(input())
        T , V = map(int , input().split())
        if letter == 'C' and T <= N and  1 <= T and -100<=V<=100  :
            box[T-1] = V

        print(box[i]*box[i+1])
        print(box)

    break
