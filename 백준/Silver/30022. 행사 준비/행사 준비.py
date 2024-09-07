import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
market = []
for i in range(N):
    m1, m2 = map(int, input().split())
    market.append([m1, m2, abs(m1 - m2)])

market.sort(key=lambda x: x[2], reverse=True)

min_cost=0
for i in range(N):
    l, r = market[i][0], market[i][1]
    if l < r:
        if A > 0:
            min_cost += l
            A -= 1
        else:
            min_cost += r
            B -= 1
    else:
        if B > 0:
            min_cost += r
            B -= 1
        else:
            min_cost += l
            A -= 1

print(min_cost)