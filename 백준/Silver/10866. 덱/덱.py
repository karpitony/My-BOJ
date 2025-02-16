import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
_deque = deque()
size = 0

for _ in range(N):
    oper = input().rstrip()
    if oper == "pop_front":
        print(_deque.popleft() if size != 0 else -1)
        size = size -1 if size!= 0 else 0
    elif oper == "pop_back":
        print(_deque.pop() if size != 0 else -1)
        size = size -1 if size!= 0 else 0
    elif oper == "size":
        print(size)
    elif oper == "empty":
        print(1 if size == 0 else 0)
    elif oper == "front":
        print(_deque[0] if size != 0 else -1)
    elif oper == "back":
        print(_deque[size-1] if size != 0 else -1)
    else:
        _oper, X = oper.split()
        X = int(X)
        if _oper == "push_front":
            _deque.appendleft(X)
            size += 1
        else:
            _deque.append(X)
            size += 1
