import sys
from collections import deque
input = sys.stdin.readline

parentheses = input().strip()
stack = deque()

result = 0
flag = True

for p in parentheses:
    if p == '(':
        stack.append(p)
    elif p == '[':
        stack.append(p)
        
    elif p == ']':
        if not stack:
            flag = False
            break
        temp = stack.pop()
        if temp == '[':
            stack.append(3)
        elif type(temp) == int:
            while True:
                if not stack:
                    flag = False
                    break
                temp2 = stack.pop()
                if temp2 == '[':
                    temp*=3
                    stack.append(temp)
                    break
                elif type(temp2) == int:
                    temp += temp2
                else:
                    flag = False
                    break
            if not flag:
                break
        else:
            flag = False
            break
        
    elif p == ')':
        if not stack:
            flag = False
            break
        temp = stack.pop()
        if temp == '(':
            stack.append(2)
        elif type(temp) == int:
            while True:
                if not stack:
                    flag = False
                    break
                temp2 = stack.pop()
                if temp2 == '(':
                    temp*=2
                    stack.append(temp)
                    break
                elif type(temp2) == int:
                    temp += temp2
                else:
                    flag = False
                    break
            if not flag:
                break
        else:
            flag = False
            break

if not flag or any(type(x) != int for x in stack):
    result = 0
else:
    result = sum(stack)
print(result)