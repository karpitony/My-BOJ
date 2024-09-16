import sys
import math
input = sys.stdin.readline

incline = set()
for _ in range(int(input())):
    x, y = map(int, input().split())
    
    g = math.gcd(abs(x), abs(y))
    x, y = x//g, y//g
    incline.add((x, y))

print(len(incline))