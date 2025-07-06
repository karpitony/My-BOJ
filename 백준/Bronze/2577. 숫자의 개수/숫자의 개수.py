import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
result = A * B * C

result = str(result)
_dict = dict()
for n in "0123456789":
    _dict[n] = 0
for r in result:
    _dict[r] += 1
    
for n in "0123456789":
    print(_dict[n])