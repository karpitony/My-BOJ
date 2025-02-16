import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

_deque = deque(range(1, N+1))

for _ in range(N-1):
    _deque.popleft()
    _deque.rotate(-1)

print(_deque[0])