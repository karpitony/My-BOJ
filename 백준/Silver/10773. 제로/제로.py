import sys
input = sys.stdin.readline

stack = list()
K = int(input())

for _ in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
        
print(sum(stack))