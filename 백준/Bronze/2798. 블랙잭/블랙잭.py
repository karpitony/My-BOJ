N, M = map(int,input().split())
number = list(map(int,input().split()))
number.sort()
BlackJack=0

for i in range(0,N-2):
    A = number[i]
    for f in range(i+1,N-1):
        B = number[f]
        for g in range(f+1,N):
            C = number[g]
            topnumber = A+B+C
            if topnumber <= M:
                if BlackJack < topnumber:
                    BlackJack = topnumber

print(BlackJack)