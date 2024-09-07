import sys
input = sys.stdin.readline

S = input().strip()
arr = ["pi", "ka", "chu"]

i = 0
isAble = True

while i < len(S):
    if S[i:i+2] in arr:
        i += 2
    elif S[i:i+3] == "chu":
        i += 3
    else:
        isAble = False
        break
        
        
if isAble:
    print("YES")
else:
    print("NO")