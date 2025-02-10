import sys
input = sys.stdin.readline

stack = []
N = int(input())

towers = list(map(int, input().split()))
answ = list()

for i in range(N):
    while stack and stack[-1][0] <= towers[i]:
        stack.pop() 
    
    if stack:
        answ.append(str(stack[-1][1]))
        
    else:
        answ.append("0")
    
    stack.append((towers[i], i+1))

print(*answ, sep=' ')