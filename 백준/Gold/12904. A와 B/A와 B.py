S = list(input())
T = list(input())

# S + "A" == T.pop()
# S[::-1] + "B" == T.pop() + T.revers()
changeAble = False

for i in range(len(T)):
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T.reverse()

    if T == S:
        changeAble = True
        break

if changeAble:
    print(1)
else:
    print(0)