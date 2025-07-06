import sys
input = sys.stdin.readline

_dict = dict()
for a in "abcdefghijklmnopqrstuvwxyz":
    _dict[a] = -1

S = input().strip()
for i in range(len(S)):
    if _dict[S[i]] == -1:
        _dict[S[i]] = i

for a in "abcdefghijklmnopqrstuvwxyz":
    print(_dict[a], end=" ")