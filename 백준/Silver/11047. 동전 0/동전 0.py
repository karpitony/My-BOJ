N, K = map(int,input().split())
coin = []
for i in range(N):
    A = int(input())
    coin.append(A)
    
coin.sort(reverse=True)

cnt = 0
for item in coin:
    while True:
        if item > K:
            break
        else:
            K -= item
            cnt += 1
    if K==0:
        print(cnt)
        break