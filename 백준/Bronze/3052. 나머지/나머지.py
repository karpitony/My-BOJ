import sys
input = sys.stdin.readline

_set = set()
for _ in range(10):
    n = int(input())
    _set.add(n % 42)
    
print(len(_set))