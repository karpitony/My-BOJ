import sys
input = sys.stdin.readline

n = int(input())
coin = 0
if n % 5 == 0:
    print(n//5)
else:
    while n > 0:
        n -= 2
        coin += 1
        if n % 5 == 0:
            coin += n // 5
            print(coin)
            break
    else:
        print(-1)  