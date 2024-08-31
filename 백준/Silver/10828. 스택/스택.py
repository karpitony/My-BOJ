
N = int(input())
stack = []

def isStackEmpty() -> bool:
    if not stack:
        return True
    else:
        return False

for _ in range(N):
    user_input = input()
    
    if user_input == "pop":
        if isStackEmpty():
            print(-1)
        else:
            print(stack.pop())
            
    elif user_input == "size":
        print(len(stack))
        
    elif user_input == "empty":
        if isStackEmpty():
            print(1)
        else:
            print(0)
    elif user_input == "top":
        if isStackEmpty():
            print(-1)
        else:
            top = stack.pop()
            print(top)
            stack.append(top)
            
    else:
        stack.append(user_input.split()[1])    