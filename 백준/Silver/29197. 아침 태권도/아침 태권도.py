import sys
input = sys.stdin.readline

incline = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    incline.append(y/x)

set_incline = set(incline)
print(len(set_incline))