while 1:
    N, M = map(int,input().split())
    if N==0 & M==0:
        break
    if N > M:
        print("Yes")
    else:
        print("No")