import sys
input = sys.stdin.readline

N = int(input())
arr = input().rstrip()

opers = ['+', '-', '*', '/']
nums = [int(input()) for _ in range(N)]
alphas = [chr(i) for i in range(65,91)]
_stack = []


for a in arr:
    if a in alphas:
        _stack.append(nums[ord(a) - 65])

    else:
        num2 = _stack.pop()
        num1 = _stack.pop()
        if a == '+':
            num1 += num2
        elif a == '-':
            num1 -= num2
        elif a == '*':
            num1 *= num2
        else:
            num1 /= num2
        _stack.append(num1)
            
print("%.2f" % _stack.pop())