T = int(input())
for _ in range(T):
    vps = list(input().strip())
    stack = []
    is_valid = True
    for v in vps:
        if v == "(":
            stack.append(v)
        else:
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
    
    if is_valid and not stack:
        print("YES")
    else:
        print("NO")