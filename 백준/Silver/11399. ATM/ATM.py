N = int(input())
P = list(map(int, input().split()))
P.sort()

total = 0; temp = 0
for item in P:
    temp += item
    total += temp

print(total)