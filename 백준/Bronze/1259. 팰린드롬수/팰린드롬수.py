while True:
    N = int(input())
    if N == 0:
        break
    else:
        N = str(N)
        num = len(N)
        for i in range(num):
            if N[i] != N[num - (1+i)]:
                print("no")
                break
        else:
            print("yes")
