import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
oil_cost = list(map(int, input().split()))

# 첫 기름은 무조건 사야하니까
cost = oil_cost[0] * road[0]
min_oil_cost = oil_cost[0]

for i in range(1, N-1):
    if oil_cost[i] < min_oil_cost:
        min_oil_cost = oil_cost[i]
    cost += min_oil_cost * road[i]
    
print(cost)